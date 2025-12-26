import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

SHOW = False

def extract_booster_id(flight_id):
	"""Extracts the booster ID from the Flight_ID field."""
	if isinstance(flight_id, str) and '/' in flight_id:
		after_slash = flight_id.split('/', 1)[1]
		return after_slash.split()[0] if ' ' in after_slash else after_slash

	return None

def parse_booster_and_flight(booster_id):
	"""Splits booster ID into base and flight count (e.g., B1049.3 -> (B1049, 3))."""
	if isinstance(booster_id, str):
		match = re.match(r"([A-Za-z0-9]+)(?:[.](\d+))?", booster_id)

		if match:
			base = match.group(1)
			flight = int(match.group(2)) if match.group(2) else 1
			return base, flight

	return booster_id, 1

def load_and_prepare_data(csv_path, booster_range=None, date_range=None):
	"""Loads CSV, extracts booster info, filters by booster and date range, and computes days between flights."""
	df = pd.read_csv(csv_path)

	booster_ids = df['Flight_ID'].apply(extract_booster_id)
	launch_dates = pd.to_datetime(df['Launch_Date'], errors='coerce')

	booster_launch_info = pd.DataFrame({
		'Booster_ID': booster_ids,
		'Launch_Date': launch_dates
	}).dropna(subset=['Booster_ID', 'Launch_Date'])

	booster_launch_info[['Booster_Base', 'Flight_Count']] = booster_launch_info['Booster_ID'].apply(
		lambda x: pd.Series(parse_booster_and_flight(x))
	)

	# Filter by booster range if provided
	if booster_range:
		start, end = booster_range
		booster_launch_info = booster_launch_info[
			booster_launch_info['Booster_Base'].apply(lambda b: start <= b <= end)
		]

	# Filter by date range if provided
	if date_range:
		min_date = booster_launch_info['Launch_Date'].min()
		max_date = booster_launch_info['Launch_Date'].max()
		start_date = pd.to_datetime(date_range[0]) if date_range[0] is not None else min_date
		end_date = pd.to_datetime(date_range[1]) if date_range[1] is not None else max_date
		booster_launch_info = booster_launch_info[
			(booster_launch_info['Launch_Date'] >= start_date) &
			(booster_launch_info['Launch_Date'] <= end_date)
		]

	booster_launch_info = booster_launch_info.sort_values(['Booster_Base', 'Flight_Count'])
	booster_launch_info['Days_Between_Flights'] = booster_launch_info.groupby('Booster_Base')['Launch_Date'].diff().dt.days

	return booster_launch_info

def plot_flight_counts_over_time(booster_launch_info, boosters_to_plot=None, show_legend=True, ):
	"""Plots flight count vs date for each booster."""
	table = booster_launch_info.pivot(index='Flight_Count', columns='Booster_Base', values='Launch_Date')

	fig, ax = plt.subplots(figsize=(12, 7))

	color_cycle = plt.get_cmap('tab20', len(table.columns))

	for idx, booster in enumerate(table.columns):
		if boosters_to_plot and booster not in boosters_to_plot:
			continue

		dates = table[booster].dropna()

		if not dates.empty:
			y = dates.index
			x = pd.to_datetime(dates.values)
			ax.plot(x, y, marker='o', label=booster, color=color_cycle(idx))

	ax.set_xlabel('Date', fontsize=12)
	ax.set_ylabel('Flight Count', fontsize=12)
	ax.set_title('Booster Flight Counts Over Time', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
	fig.autofmt_xdate()

	if show_legend:
		ax.legend(title='Booster ID', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8, title_fontsize=9, ncol=1, borderaxespad=0.)

	plt.tight_layout(rect=[0, 0, 1, 1])

	# Save chart and data
	booster_suffix = ""
	if boosters_to_plot:
		sorted_boosters = sorted(str(b) for b in boosters_to_plot)
		booster_suffix = f"_{sorted_boosters[0]}-to-{sorted_boosters[-1]}"

	img_path = f"examples/outputs/chart/f9_matplotlib/f9_flight_counts_over_time{booster_suffix}.png"
	csv_path = f"examples/outputs/csv/f9_matplotlib/f9_flight_counts_over_time{booster_suffix}.csv"

	plt.savefig(img_path)
	booster_launch_info.to_csv(csv_path, index=False)

	if SHOW:
		plt.show()

def plot_days_between_vs_flight_count(booster_launch_info, boosters_to_plot=None, show_legend=True, max_days_between=None):
	"""Plots days between flights vs flight count for each booster. Optionally filter by max_days_between."""
	fig, ax = plt.subplots(figsize=(12, 7))

	color_cycle = plt.get_cmap('tab20', len(booster_launch_info['Booster_Base'].unique()))

	lines = []

	for idx, (booster, group) in enumerate(booster_launch_info.groupby('Booster_Base')):
		if boosters_to_plot and booster not in boosters_to_plot:
			continue

		if group['Flight_Count'].max() > 1:
			y = group['Days_Between_Flights'].copy()

			if max_days_between is not None:
				y = y.where(y <= max_days_between, float('nan'))

			line, = ax.plot(
				group['Flight_Count'],
				y,
				marker='o',
				label=booster,
				color=color_cycle(idx % color_cycle.N)
			)

			lines.append(line)

	ax.set_xlabel('Flight Count', fontsize=12)
	ax.set_ylabel('Days Between Flights', fontsize=12)
	ax.set_title('Days Between Flights vs Flight Count', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)

	if show_legend and lines:
		ax.legend(handles=lines, title='Booster ID', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8, title_fontsize=9, ncol=1, borderaxespad=0.)

	plt.tight_layout(rect=[0, 0, 1, 1])

	# Save chart and data
	booster_suffix = ""
	if boosters_to_plot:
		sorted_boosters = sorted(str(b) for b in boosters_to_plot)
		booster_suffix = f"_{sorted_boosters[0]}-to-{sorted_boosters[-1]}"

	img_path = f"examples/outputs/chart/f9_matplotlib/f9_days_between_vs_flight_count{booster_suffix}.png"
	csv_path = f"examples/outputs/csv/f9_matplotlib/f9_days_between_vs_flight_count{booster_suffix}.csv"

	plt.savefig(img_path)
	booster_launch_info.to_csv(csv_path, index=False)

	if SHOW:
		plt.show()

def plot_days_between_vs_date(booster_launch_info, boosters_to_plot=None, show_legend=True, max_days_between=None):
	"""Plots days between flights vs date for each booster. Optionally filter by max_days_between."""
	fig, ax = plt.subplots(figsize=(12, 7))

	color_cycle = plt.get_cmap('tab20', len(booster_launch_info['Booster_Base'].unique()))

	lines = []

	for idx, (booster, group) in enumerate(booster_launch_info.groupby('Booster_Base')):
		if boosters_to_plot and booster not in boosters_to_plot:
			continue

		if group['Flight_Count'].max() > 1:
			y = group['Days_Between_Flights'].copy()

			if max_days_between is not None:
				y = y.where(y <= max_days_between, float('nan'))

			line, = ax.plot(
				group['Launch_Date'],
				y,
				marker='o',
				label=booster,
				color=color_cycle(idx % color_cycle.N)
			)

			lines.append(line)

	ax.set_xlabel('Date', fontsize=12)
	ax.set_ylabel('Days Between Flights', fontsize=12)
	ax.set_title('Days Between Flights vs Date', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

	if show_legend and lines:
		ax.legend(handles=lines, title='Booster ID', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8, title_fontsize=9, ncol=1, borderaxespad=0.)

	plt.tight_layout(rect=[0, 0, 1, 1])

	# Save chart and data
	booster_suffix = ""
	if boosters_to_plot:
		sorted_boosters = sorted(str(b) for b in boosters_to_plot)
		booster_suffix = f"_{sorted_boosters[0]}-to-{sorted_boosters[-1]}"

	img_path = f"examples/outputs/chart/f9_matplotlib/f9_days_between_vs_date{booster_suffix}.png"
	csv_path = f"examples/outputs/csv/f9_matplotlib/f9_days_between_vs_date{booster_suffix}.csv"

	plt.savefig(img_path)
	booster_launch_info.to_csv(csv_path, index=False)

	if SHOW:
		plt.show()

def plot_booster_groups_of_10(booster_launch_info, min_num=1060, max_num=1100):
	"""Plots charts for each group of 10 boosters (e.g., B1060-B1069, B1070-B1079, ...)."""
	def get_booster_number(booster_base):
		match = re.match(r"B(\d+)", booster_base)

		return int(match.group(1)) if match else None

	unique_boosters = sorted(set(booster_launch_info['Booster_Base']))

	booster_nums = [get_booster_number(b) for b in unique_boosters if get_booster_number(b) is not None]

	for group_start in range(min_num, max_num, 10):
		group_end = group_start + 9
		group_boosters = [f"B{num}" for num in booster_nums if group_start <= num <= group_end]

		if not group_boosters:
			continue

		group_info = booster_launch_info[booster_launch_info['Booster_Base'].isin(group_boosters)]

		if group_info.empty:
			continue

		plot_flight_counts_over_time(group_info, boosters_to_plot=group_boosters, show_legend=True)
		plot_days_between_vs_flight_count(group_info, boosters_to_plot=group_boosters, show_legend=True)
		plot_days_between_vs_date(group_info, boosters_to_plot=group_boosters, show_legend=True)

def plot_days_between_launches_from_site(df, launch_pad_name, show_legend=True, date_range=None):
	"""
	Plots days between launches from a specific launch pad.

	Args:
		df (pd.DataFrame): DataFrame containing launch data. Must include 'Launch_Pad' and 'Launch_Date' columns.
		launch_pad_name (str): The name of the launch pad to filter by (e.g., 'LC40').
		show_legend (bool, optional): Whether to show the legend. Default is True.
		date_range (tuple or list, optional): (start_date, end_date) as strings or None. Filters launches to this date range. Default is None (no filter).
	"""
 
	site_col = "Launch_Pad"
	date_col = "Launch_Date"

	site_df = df[df[site_col] == launch_pad_name].copy()
	site_df[date_col] = pd.to_datetime(site_df[date_col], errors='coerce')

	if date_range is not None:
		start_date = pd.to_datetime(date_range[0]) if date_range[0] is not None else site_df[date_col].min()
		end_date = pd.to_datetime(date_range[1]) if date_range[1] is not None else site_df[date_col].max()
		site_df = site_df[(site_df[date_col] >= start_date) & (site_df[date_col] <= end_date)]

	site_df = site_df.sort_values(by=date_col)
	site_df['days_since_last'] = site_df[date_col].diff().dt.days

	fig, ax = plt.subplots(figsize=(12, 7))

	ax.plot(site_df[date_col], site_df['days_since_last'], marker='o', label=launch_pad_name)


	# Polynomial trendline (degree 3)
	import numpy as np
	x = site_df[date_col].map(pd.Timestamp.toordinal)
	y = site_df['days_since_last']
	mask = ~y.isna()
	x_fit = x[mask]
	y_fit = y[mask]
	if len(x_fit) > 3:
		coeffs = np.polyfit(x_fit, y_fit, 3)
		poly = np.poly1d(coeffs)
		y_trend = poly(x_fit)
		ax.plot(site_df[date_col][mask], y_trend, color='red', linestyle='dashed', linewidth=2.5, label='3rd Degree Polynomial Fit')

	# Moving average trendline
	window = 25
	moving_avg = site_df['days_since_last'].rolling(window=window, center=True, min_periods=1).mean()
	ax.plot(site_df[date_col], moving_avg, color='orange', linestyle='dashed', linewidth=2.5, label=f'{window}-pt Moving Avg')

	ax.set_xlabel('Date', fontsize=12)
	ax.set_ylabel('Days Since Last Launch', fontsize=12)
	ax.set_title(f'Days Between Launches from {launch_pad_name}', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
	fig.autofmt_xdate()

	if show_legend:
		ax.legend(title='Launch Pad', loc='upper left', fontsize=11, title_fontsize=11)

	# Calculate stats for annotation
	last_50 = site_df['days_since_last'].dropna().iloc[-50:]
	min_val = last_50.min()
	perc_10 = last_50.quantile(0.1)
	perc_90 = last_50.quantile(0.9)
	avg_last_50 = last_50.mean()

	note = (
		f"Last 50 Launches:\nMinimum: {min_val:.1f}\n10th percentile: {perc_10:.1f}\nAverage: {avg_last_50:.1f}\n90th percentile: {perc_90:.1f}"
	)
	ax.text(
		0.985, 0.97, note,
		transform=ax.transAxes,
		fontsize=11,
		va='top', ha='right',
		color='black',
		bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.85)
	)

	plt.tight_layout(rect=[0, 0, 1, 1])

	date_suffix = ""
	if date_range is not None:
		start_str = date_range[0] if date_range[0] else "start"
		end_str = date_range[1] if date_range[1] else "present"
		date_suffix = f"_{start_str}_{end_str}"

	img_path = f"examples/outputs/chart/f9_matplotlib/f9_days_between_launches_{launch_pad_name}{date_suffix}.png"
	csv_path = f"examples/outputs/csv/f9_matplotlib/f9_days_between_launches_{launch_pad_name}{date_suffix}.csv"

	plt.savefig(img_path)
	site_df.to_csv(csv_path, index=False)

	if SHOW:
		plt.show()

def plot_days_between_vs_date_all_boosters(booster_launch_info, window=25, show_legend=True):
	"""
	Plots days between flights vs date for all boosters in one color, with a moving average.

	Args:
		booster_launch_info (pd.DataFrame): DataFrame with 'Launch_Date' and 'Days_Between_Flights'.
		window (int): Window size for moving average.
		show_legend (bool): Whether to show the legend.
	"""
	fig, ax = plt.subplots(figsize=(12, 7))
	ax.plot(booster_launch_info['Launch_Date'], booster_launch_info['Days_Between_Flights'], marker='o', linestyle='-', color='tab:blue', alpha=0.5, label='All Boosters')

	# Polynomial trendline (degree 3) and moving average over all boosters, sorted by date
	sorted_df = booster_launch_info.sort_values('Launch_Date')
	x = sorted_df['Launch_Date'].map(pd.Timestamp.toordinal)
	y = sorted_df['Days_Between_Flights']
	mask = ~y.isna()
	x_fit = x[mask]
	y_fit = y[mask]
	# Moving average
	moving_avg = y.rolling(window=window, center=True, min_periods=1).mean()
	ax.plot(sorted_df['Launch_Date'], moving_avg, color='orange', linestyle='dashed', linewidth=2.5, label=f'{window}-pt Moving Avg')
	# Polynomial fit
	if len(x_fit) > 3:
		coeffs = np.polyfit(x_fit, y_fit, 3)
		poly = np.poly1d(coeffs)
		y_trend = poly(x_fit)
		ax.plot(sorted_df['Launch_Date'][mask], y_trend, color='red', linestyle='dashed', linewidth=2.5, label='3rd Degree Polynomial Fit')

	# Calculate stats for annotation
	last_50 = sorted_df['Days_Between_Flights'].dropna().iloc[-50:]
	min_val = last_50.min()
	perc_10 = last_50.quantile(0.1)
	perc_90 = last_50.quantile(0.9)
	avg_last_50 = last_50.mean()

	note = (
		f"Last 50 Launches:\nMinimum: {min_val:.1f}\n10th percentile: {perc_10:.1f}\nAverage: {avg_last_50:.1f}\n90th percentile: {perc_90:.1f}"
	)
	ax.text(
		0.985, 0.97, note,
		transform=ax.transAxes,
		fontsize=11,
		va='top', ha='right',
		color='black',
		bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.85)
	)

	ax.set_xlabel('Date', fontsize=12)
	ax.set_ylabel('Days Between Flights', fontsize=12)
	ax.set_title('Days Between Flights vs Date (All Boosters)', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
	fig.autofmt_xdate()
	if show_legend:
		ax.legend(loc='upper left', fontsize=11)
	plt.tight_layout(rect=[0, 0, 1, 1])

	img_path = 'examples/outputs/chart/f9_matplotlib/f9_days_between_vs_date_all_boosters.png'
	csv_path = 'examples/outputs/csv/f9_matplotlib/f9_days_between_vs_date_all_boosters.csv'
	plt.savefig(img_path)
	booster_launch_info.to_csv(csv_path, index=False)

	if SHOW:
		plt.show()

def plot_f9_launches_vs_month_by_payload_type():
	"""Plots bar chart for F9 launches per month by payload type, with sigmoid overlay for Starlink."""
	csv_path = 'examples/outputs/csv/f9/f9_launches_vs_month_by_general_launch_payload_type_2010_present.csv'
	df = pd.read_csv(csv_path)
	
	# Convert Launch_Month to datetime
	df['Launch_Date'] = pd.to_datetime(df['Launch_Month'], format='%b %Y')
	
	# Extend to Jan 2030
	end_date = pd.to_datetime('2030-01-01')
	current_end = df['Launch_Date'].max()
	if current_end < end_date:
		new_dates = pd.date_range(start=current_end + pd.DateOffset(months=1), end=end_date, freq='MS')
		new_rows = pd.DataFrame({
			'Launch_Month': new_dates.strftime('%b %Y'),
			'Starlink': 0,
			'Commercial': 0,
			'Chinese Commercial': 0,
			'Government': 0,
			'Eastern Government': 0,
			'Military': 0,
			'Eastern Military': 0,
			'Launch_Date': new_dates
		})
		df = pd.concat([df, new_rows], ignore_index=True)
	
	# Calculate months since Jan 2010
	start_date = pd.to_datetime('2010-01-01')
	df['Months_Since_Start'] = ((df['Launch_Date'] - start_date) / pd.Timedelta(days=30.44)).round().astype(int)
	
	x = df['Months_Since_Start']
	y_starlink = df['Starlink']
	y_other = df[['Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']].sum(axis=1)
	
	# Sigmoid parameters (for Starlink)
	x_bias = 168
	x_gain = 1/15
	y_bias = 0.5
	y_gain = 17
	
	y_line = y_gain / (1 + np.exp(-x_gain * (x - x_bias))) + y_bias
	
	# Plot
	fig, ax = plt.subplots(figsize=(12, 7))
	
	# Bar width in days
	bar_width = 30  # slightly wider to eliminate gaps
	
	# Stacked bars
	positions = df['Launch_Date']
	# Starlink bars (bottom)
	ax.bar(positions, y_starlink, width=bar_width, label='Starlink Launches', color='#005eff', alpha=0.7, edgecolor='#005eff')
	# Other bars (on top)
	ax.bar(positions, y_other, width=bar_width, bottom=y_starlink, label='Other Launches', color='#fbbc04', alpha=0.7, edgecolor='#fbbc04')
	
	# Sigmoid fit (on Starlink)
	ax.plot(df['Launch_Date'], y_line, label='Sigmoid Fit', color='red', linewidth=2)
	
	# Add parameters box
	note = (
		f"Sigmoid Parameters:\n"
		f"x_bias: {x_bias}\n"
		f"x_gain: {x_gain:.4f}\n"
		f"y_bias: {y_bias}\n"
		f"y_gain: {y_gain}\n"
		"[x] = months\n"
		"[y] = num launches"
	)
	ax.text(
		0.013, 0.847, note,
		transform=ax.transAxes,
		fontsize=10,
		va='top', ha='left',
		color='black',
		bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.85)
	)
	
	ax.set_xlabel('Launch Month', fontsize=12)
	ax.set_ylabel('Number of Launches', fontsize=12)
	ax.set_title('F9 Monthly Launches: Starlink vs Other with Sigmoid Fit', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	
	# Set x-axis to show Jan of each year
	ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=1))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
	fig.autofmt_xdate()
	
	# Set xlim to include up to 2030
	ax.set_xlim(pd.to_datetime('2010-01-01'), pd.to_datetime('2030-01-01'))
	
	ax.legend()
	
	plt.tight_layout()
	
	# Save
	img_path = 'examples/outputs/chart/f9_matplotlib/f9_starlink_launches_vs_month_with_sigmoid.png'
	csv_out_path = 'examples/outputs/csv/f9_matplotlib/f9_starlink_launches_vs_month_with_sigmoid.csv'
	
	plt.savefig(img_path)
	df.to_csv(csv_out_path, index=False)
	
	if SHOW:
		plt.show()

def plot_f9_and_starship_launches_vs_month():
	"""Plots side-by-side bars for F9 and Starship total launches per month, with F9 sigmoid fit."""
	csv_path = 'examples/outputs/csv/f9/f9_launches_vs_month_by_general_launch_payload_type_2010_present.csv'
	df = pd.read_csv(csv_path)
	
	# Convert Launch_Month to datetime
	df['Launch_Date'] = pd.to_datetime(df['Launch_Month'], format='%b %Y')
	
	# Extend to Jan 2030
	end_date = pd.to_datetime('2030-01-01')
	current_end = df['Launch_Date'].max()
	if current_end < end_date:
		new_dates = pd.date_range(start=current_end + pd.DateOffset(months=1), end=end_date, freq='MS')
		new_rows = pd.DataFrame({
			'Launch_Month': new_dates.strftime('%b %Y'),
			'Starlink': 0,
			'Commercial': 0,
			'Chinese Commercial': 0,
			'Government': 0,
			'Eastern Government': 0,
			'Military': 0,
			'Eastern Military': 0,
			'Launch_Date': new_dates
		})
		df = pd.concat([df, new_rows], ignore_index=True)
	
	# Load Starship data
	starship_csv = 'examples/other/starship_prediction.csv'
	df_starship = pd.read_csv(starship_csv)
	df_starship['Launch_Date'] = pd.to_datetime(df_starship['Launch_Month'], format='%b %Y')
	
	# Use the starship data as the base, since it includes F9 predictions
	df = df_starship.copy()
	df['Launch_Date'] = pd.to_datetime(df['Launch_Month'], format='%b %Y')
	
	# Calculate totals, fill NaN with 0
	y_f9_total = df['F9 Total'].fillna(0)
	y_starship_total = df['Starship Total'].fillna(0)
	
	# Calculate months since Jan 2010 for sigmoid
	start_date = pd.to_datetime('2010-01-01')
	df['Months_Since_Start'] = ((df['Launch_Date'] - start_date) / pd.Timedelta(days=30.44)).round().astype(int)
	x = df['Months_Since_Start']
	
	# Sigmoid parameters (for F9)
	x_bias = 168
	x_gain = 1/15
	y_bias = 0.5
	y_gain = 17
	y_line = y_gain / (1 + np.exp(-x_gain * (x - x_bias))) + y_bias
	
	# Plot
	fig, ax = plt.subplots(figsize=(12, 7))
	
	bar_width = 30  # days, slightly wider to eliminate gaps
	positions = df['Launch_Date']
	
	# Stacked bars: F9 bottom, Starship on top
	ax.bar(positions, y_f9_total, width=bar_width, label='F9 Total Launches', color='#005eff', alpha=0.7, edgecolor='#005eff')
	ax.bar(positions, y_starship_total, width=bar_width, bottom=y_f9_total, label='Starship Total Launches', color='#fbbc04', alpha=0.7, edgecolor='#fbbc04')
	
	# F9 Sigmoid fit
	ax.plot(df['Launch_Date'], y_line, label='F9 Sigmoid Fit', color='red', linewidth=2)
	
	# Add parameters box
	note = (
		f"Sigmoid Parameters:\n"
		f"x_bias: {x_bias}\n"
		f"x_gain: {x_gain:.4f}\n"
		f"y_bias: {y_bias}\n"
		f"y_gain: {y_gain}\n"
		"[x] = months\n"
		"[y] = num launches"
	)
	ax.text(
		0.013, 0.847, note,
		transform=ax.transAxes,
		fontsize=10,
		va='top', ha='left',
		color='black',
		bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.85)
	)
	
	ax.set_xlabel('Launch Month', fontsize=12)
	ax.set_ylabel('Number of Launches', fontsize=12)
	ax.set_title('F9 & Starship Stacked Total Monthly Launches with F9 Sigmoid Fit', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	
	# Set x-axis to show Jan of each year
	ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=1))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
	fig.autofmt_xdate()
	
	# Set xlim to include up to 2030
	ax.set_xlim(pd.to_datetime('2010-01-01'), pd.to_datetime('2030-01-01'))
	
	ax.legend()
	
	plt.tight_layout()
	
	# Save
	img_path = 'examples/outputs/chart/f9_matplotlib/f9_and_starship_total_launches_vs_month.png'
	csv_out_path = 'examples/outputs/csv/f9_matplotlib/f9_and_starship_total_launches_vs_month.csv'
	
	plt.savefig(img_path)
	df.to_csv(csv_out_path, index=False)
	
	if SHOW:
		plt.show()

def plot_starlink_capacity_tbps():
	"""Plots Starlink capacity in Tbps for F9 and Starship."""
	starship_csv = 'examples/other/starship_prediction.csv'
	df = pd.read_csv(starship_csv)
	df['Launch_Date'] = pd.to_datetime(df['Launch_Month'], format='%b %Y')
	
	# Capacity per launch
	f9_tbps_per_launch = 3
	starship_tbps_per_launch = 60
	
	# Monthly Tbps, fill NaN with 0
	df['F9_Starlink_Tbps'] = df['Starlink'].fillna(0) * f9_tbps_per_launch
	df['Starship_Starlink_Tbps'] = df['Starship (Starlink)'].fillna(0) * starship_tbps_per_launch
	
	# Plot
	fig, ax = plt.subplots(figsize=(12, 7))
	
	bar_width = 31
	positions = df['Launch_Date']
	
	# Stacked bars: F9 bottom, Starship on top
	ax.bar(positions, df['F9_Starlink_Tbps'], width=bar_width, label='F9 Starlink Additional Capacity', color='#005eff', alpha=0.7, edgecolor='#005eff')
	ax.bar(positions, df['Starship_Starlink_Tbps'], width=bar_width, bottom=df['F9_Starlink_Tbps'], label='Starship Starlink Additional Capacity', color='#fbbc04', alpha=0.7, edgecolor='#fbbc04')
	
	ax.set_xlabel('Launch Month', fontsize=12)
	ax.set_ylabel('Additional Capacity Launched (Tbps)', fontsize=12)
	ax.set_title('Monthly Additional Starlink Capacity: F9 vs Starship', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	
	# Set x-axis to show Jan of each year
	ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=1))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
	fig.autofmt_xdate()
	
	# Set xlim to include up to 2030
	ax.set_xlim(pd.to_datetime('2010-01-01'), pd.to_datetime('2030-01-01'))
	
	# Add capacity info
	note = (
		f"Capacity per Launch:\n"
		f"F9: {f9_tbps_per_launch} Tbps\n"
		f"Starship: {starship_tbps_per_launch} Tbps"
	)
	ax.text(
		0.013, 0.882, note,
		transform=ax.transAxes,
		fontsize=10,
		va='top', ha='left',
		color='black',
		bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.85)
	)
	
	ax.legend(loc='upper left')
	
	plt.tight_layout()
	
	# Save
	img_path = 'examples/outputs/chart/f9_matplotlib/starlink_capacity_tbps.png'
	csv_out_path = 'examples/outputs/csv/f9_matplotlib/starlink_capacity_tbps.csv'
	
	plt.savefig(img_path)
	df.to_csv(csv_out_path, index=False)
	
	if SHOW:
		plt.show()

def plot_starship_launches_by_type():
	"""Plots stacked bars for Starship launches by type: Starlink vs Other."""
	starship_csv = 'examples/other/starship_prediction.csv'
	df = pd.read_csv(starship_csv)
	df['Launch_Date'] = pd.to_datetime(df['Launch_Month'], format='%b %Y')
	
	# Fill NaN with 0
	y_starlink = df['Starship (Starlink)'].fillna(0)
	y_other = df['Starship'].fillna(0)
	
	# Plot
	fig, ax = plt.subplots(figsize=(12, 7))
	
	bar_width = 31
	positions = df['Launch_Date']
	
	# Stacked bars: Starlink bottom, Other on top
	ax.bar(positions, y_starlink, width=bar_width, label='Starship Starlink Launches', color='#005eff', alpha=0.7, edgecolor='#005eff')
	ax.bar(positions, y_other, width=bar_width, bottom=y_starlink, label='Starship Other Launches', color='#fbbc04', alpha=0.7, edgecolor='#fbbc04')
	
	ax.set_xlabel('Launch Month', fontsize=12)
	ax.set_ylabel('Number of Launches', fontsize=12)
	ax.set_title('Starship Launches by Type: Starlink vs Other', fontsize=14)
	ax.grid(True, linestyle='--', alpha=0.5)
	
	# Set x-axis to show Jan of each year
	ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=1))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
	fig.autofmt_xdate()
	
	# Set xlim to include up to 2030
	ax.set_xlim(pd.to_datetime('2010-01-01'), pd.to_datetime('2030-01-01'))
	
	ax.legend(loc='upper left')
	
	plt.tight_layout()
	
	# Save
	img_path = 'examples/outputs/chart/f9_matplotlib/starship_launches_by_type.png'
	csv_out_path = 'examples/outputs/csv/f9_matplotlib/starship_launches_by_type.csv'
	
	plt.savefig(img_path)
	df.to_csv(csv_out_path, index=False)
	
	if SHOW:
		plt.show()

# F9 Launch Sites: LC40, LC39A, SLC4E 
df = pd.read_csv("examples/outputs/raw_dataframes/f9/raw_dataframe_f9_launches_apogee_vs_date_by_simple_orbit_2010_present.csv")
plot_days_between_launches_from_site(df, "LC40", date_range=("2022-01-01", None))
plot_days_between_launches_from_site(df, "LC39A", date_range=("2022-01-01", None))
plot_days_between_launches_from_site(df, "SLC4E", date_range=("2022-01-01", None))

csv_path = 'examples/outputs/raw_dataframes/f9/raw_dataframe_f9_launches_apogee_vs_date_by_simple_orbit_2010_present.csv'
booster_launch_info = load_and_prepare_data(csv_path)
#plot_booster_groups_of_10(booster_launch_info, min_num=1080, max_num=1100)

# Call the new function
plot_days_between_vs_date_all_boosters(booster_launch_info)

# Call the bar chart function
plot_f9_launches_vs_month_by_payload_type()

# Call the combined F9 and Starship function
plot_f9_and_starship_launches_vs_month()

# Call the Starlink capacity function
plot_starlink_capacity_tbps()

plot_starship_launches_by_type()
