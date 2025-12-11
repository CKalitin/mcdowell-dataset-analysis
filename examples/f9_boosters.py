import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

def plot_flight_counts_over_time(booster_launch_info, boosters_to_plot=None, show_legend=True):
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


if __name__ == "__main__":
	csv_path = 'examples/outputs/raw_dataframes/f9/raw_dataframe_f9_launches_apogee_vs_date_by_simple_orbit_2010_present.csv'
	booster_launch_info = load_and_prepare_data(csv_path)
	plot_booster_groups_of_10(booster_launch_info, min_num=1080, max_num=1100)
