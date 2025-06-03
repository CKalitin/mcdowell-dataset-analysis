import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import copy

class ChartUtils:
    """
    This class contains utility functions for working with dataframes and generating charts.
    """
    
    orbit_color_map = {
        'LEO': '#ffc000',
        'SSO': "#ffdf80",
        'MEO': '#cc0000',
        'GTO': '#3d85c6',
        'GEO': '#1155cc',
        'HEO': "#51606e",
        'BEO': '#3c4043'
    }
    
    def pivot_dataframe(df, index_col, column_col, value_col):
        """
        Index_col is used as the row index of the pivoted dataframe.
        Column_col specifies the values that become the new columns of the pivoted dataframe.
        Value_col specifies the values that fill the new DataFrame, at the interscetion of the index and column values.
        
        Example:
        >>> df = pd.DataFrame({
        ...     'Launch_Date': ['2020-01-01', '2020-01-01', '2020-02-01'],
        ...     'Launch_Pad': ['SLC4E', 'LC39A', 'SLC4E'],
        ...     'Apogee': [550, 600, 560]
        ... })
        >>> pivot_dataframe(df, 'Launch_Date', 'Launch_Pad', 'Apogee')
           Launch_Date  LC39A  SLC4E
        0  2020-01-01  600.0  550.0
        1  2020-02-01    NaN  560.0
        
        Raises:
            ValueError: If the pivot operation results in duplicate entries for an index-column combination.
        
        See Pandas documentation for more details:
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html
        """
        pivoted = df.pivot(index=index_col, columns=column_col, values=value_col)
        pivoted = pivoted.reset_index().sort_values(by=index_col)
        return pivoted

    def count_values_into_bins(dataframe, value_col, bins, labels, count_values=False, bin_column=None):
        """
        Sort groups (then, count totals if count_values) into discrete bins (eg. intervals of payload mass) and count how many data points fall into each bin.
        
        Args:
            dataframe (Pandas dataframe): Dataframe containing the data to be binned
            value_col (str): Column to be used for binning, eg. 'Payload_Mass'.
            bins (list int): List of bin edges, eg. [0, 1000, 2000, 3000] for payload mass bins.
            labels (list str): List of bin labels, eg. ['0-1T', '1-2T', '2-3T'] for payload mass bins.
            count_values (bool, optional): If True, counts the number of values in each bin and returns this instead of the bin itself. Defaults to False.
            bin_column (str, optional): If provided, adds a new column to the dataframe for the bin of each row. Defaults to None.
            
        Note what bin_column does. If you don't provide a value, it will returns something like this:
        70696      2-3t
        70795      3-4t
        71078      4-5t
        71159      5-6t
        71260      6-7t
        71406      0-1t
        Notice each row only has one value, the bin it belongs to.
        
        If you provide a bin_column, then each row will retain all of its original data, but will have a new column with the bin it belongs to.
        
        Notice that labels are between the bins. The bins variable specifies the edges of the bins.
        """
        
        if bin_column:
            dataframe[bin_column] = pd.cut(dataframe[value_col], bins=bins, labels=labels, include_lowest=True)
            binned = dataframe
        else:
            binned = pd.cut(dataframe[value_col], bins=bins, labels=labels, include_lowest=True)
        if count_values:
            binned = binned.value_counts().reindex(labels)
        return binned
 
    def bin_dataset_into_dictionary_by_filter_function(dataset, filter_function, filter_function_parameters, value_col, bins, bin_labels, keys=None, count_values=True, bin_column=None):
        """Filters a dataset by a given filter function and returns a dataframe for each filter function parameter.
        
        Eg. You can filter by orbit and get a dictionary of dataframes, one for each orbit.
        
        If it doesn't make sense, read Pandas documentation.
        
        Args:
            dataset (launch or satcat): Launch or Satcat dataset (notice this isn't the McDowellDataset, so use dataset.launch or dataset.satcat)
            filter_function (mda.Filters...): Filter function to be applied
            filter_function_parameters (list): List of paramters, eg. ['LEO', 'SSO, ... , 'BEO'] for orbits or ['Falcon9', 'Electron'] for launch vehicles.
            value_col (str): Column to be used for binning, eg. 'Payload_Mass'.
            bins (list int): List of bin edges, eg. [0, 1000, 2000, 3000] for payload mass bins.
            bin_labels (list str): List of bin labels, eg. ['0-1T', '1-2T', '2-3T'] for payload mass bins.
            keys (list str, optional): Use if keys should be different from filter_function_parameters. Eg. for orbits if you want 'Low Earth Orbit' instead of 'LEO'. Must be in same order as filter_function_parameters. Defaults to None.
            count_values (bool, optional): If True, counts the number of values in each bin and returns this instead of the bin itself. Defaults to True.
            bin_column (str, optional): See count_values_into_bins(). If provided, adds a new column to the dataframe for the bin of each row. Defaults to None.

        Returns:
            dictionary(key, binned dataframe): A dictionary where each key is a filter function parameter and the value is a dataframe with binned values.
        """

        if keys is None:
            keys = filter_function_parameters
        output_dict = {}
        for filter_function_parameter, key in zip(filter_function_parameters, keys):
            new_dataset = copy.deepcopy(dataset)  # Create a copy of the dataframe to avoid modifying the original, bad solution tbh. Deep copy is required bc dataset is part of another class (i think this is why).
            filter_function(new_dataset, filter_function_parameter)  # Apply the filter function
            output_dict[key] = ChartUtils.count_values_into_bins(new_dataset.df, value_col, bins, bin_labels, count_values, bin_column)
        return output_dict
 
    # Combines individual dataframes as columns into a single dataframe, with keys as column names.
    def combine_dictionary_of_dataframes(dataframes):
        # .values gives us a list-like object of the counts for each year
        # Concat axis=1 combines each individual dataframe into columns of a single dataframe
        output_df = pd.concat(dataframes.values(), axis=1)
        output_df.columns = dataframes.keys() # Name columns by the orbits
        return output_df

    # Histograms are designed for continuous data, while bar charts are for discrete data.
    def plot_histogram(dataframe, title, subtitle, x_label, y_label, output_path, color_map, barmode='stack', bargap=0):
        fig = px.histogram(dataframe,
                    x=dataframe.index,
                    y=dataframe.columns,
                    title=f'<b>{title}</b><br><sup>{subtitle}</sup>',
                    labels={'x': f'{x_label}', 'y': f'{y_label}'},
                    barmode=barmode,
                    color_discrete_map=color_map,
                    )

        fig.update_layout(
            # Font settings
            font=dict(family='Arial, sans-serif', size=20, color="#000000"),
            title=dict(font=dict(size=40, family='Arial, sans-serif', color="#000000"), x=0.025, xanchor="left"),
            # Background and borders
            plot_bgcolor="white",
            paper_bgcolor="white",
            # Gridlines
            xaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                tickangle=45,
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=x_label,
            ),
            yaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                rangemode='tozero',           # <— force start at 0
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=y_label,
            ),
            # Legend
            showlegend=True,
            legend=dict(
                font=dict(size=24, family="Arial, sans-serif"),
                bordercolor="white",
                borderwidth=1,
                bgcolor="white",
                title=dict(text=""),  # Add this line to remove title: "variable"
            ),
            # Remove hover effects and other embellishments
            hovermode="x",
            bargap=bargap,
        )

        pio.write_image(fig, output_path, format='png', width=1280, height=720)
        
        print(f"Plot saved as '{output_path}'.")
    
    def plot_bar(dataframe, title, subtitle, x_label, y_label, output_path, color_map, barmode='stack', bargap=0, x_tick0=0, x_tick_step_size=1):
        """
        Create a bar chart using Plotly Express.
        Args:
            dataframe (Pandas dataframe): Dataframe containing the data to be plotted
            title (string): Title of the chart
            subtitle (string): Subtitle of the chart, best to include the date of the data cut-off "Date Cutoff: YYYY-MM-DD"
            x_label (string): Label for the x-axis
            y_label (string): Label for the y-axis
            output_path (string): Full path including filename to save the plot
            color_map (dictionary): Column name to color mapping, eg. {'LC40': '#ff0000', 'LC39A': '#00ff00'}
            barmode (string): 'stack' or 'group'
            bargap (float): Gap between bars, 0-1
            x_tick0 (int): First tick on the x axis (x_label). 0 = first index.
            x_tick_step_size (int): tick step size
        """
        
        fig = px.bar(dataframe,
                     x=dataframe.index,
                     y=dataframe.columns,
                     title=f'<b>{title}</b><br><sup>{subtitle}</sup>',
                     labels={'x': f'{x_label}', 'y': f'{y_label}'},
                     barmode=barmode,
                     color_discrete_map=color_map,
                     )
        
        fig.update_layout(
            # Font settings
            font=dict(family='Arial, sans-serif', size=20, color="#000000"),
            title=dict(font=dict(size=40, family='Arial, sans-serif', color="#000000"), x=0.025, xanchor="left"),
            # Background and borders
            plot_bgcolor="white",
            paper_bgcolor="white",
            # Gridlines
            xaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                tickangle=45,
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=x_label,
                tick0=x_tick0,
                dtick=x_tick_step_size # step size
            ),
            yaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                rangemode='tozero',           # <— force start at 0
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=y_label,
            ),
            # Legend
            showlegend=True,
            legend=dict(
                font=dict(size=24, family="Arial, sans-serif"),
                bordercolor="white",
                borderwidth=1,
                bgcolor="white",
                title=dict(text=""),  # Add this line to remove title: "variable"
            ),
            # Remove hover effects and other embellishments
            hovermode="x",
            bargap=bargap,
        )
        pio.write_image(fig, output_path, format='png', width=1280, height=720)
        
        print(f"Plot saved as '{output_path}'.")
    
    def plot_scatter(dataframe, x_col, y_cols, title, subtitle, x_label, y_label, dot_diameter, output_path, color_map, y_scaling_factor=1):
        """
        Create a scatter plot using Plotly Express.
        Args:
            dataframe (Pandas dataframe): Dataframe containing the x_col and y_cols data
            x_col (string): Title of the column to be used for the x-axis
            y_cols (string): Titles of the column to be used for the series data
            title (string): It's simple
            subtitle (string): Best to include the date of the data cut-off "Date Cutoff: YYYY-MM-DD"
            x_label (string): It's simple
            y_label (string): It's simple
            y_scaling_factor (float/int): Multiplicative factor to scale the y-axis
            output_path (string): Full path including filename to save the plot
            color_map (dictionary): y_col to color mapping, eg. {'LC40': '#ff0000', 'LC39A': '#00ff00'}
        """
        
        df = dataframe.copy()
        if y_scaling_factor != 1:
            for col in y_cols:
                df[col] = df[col] * y_scaling_factor
        
        fig = px.scatter(df,
                         x=x_col,
                         y=y_cols,
                         title=f'<b>{title}</b><br><sup>{subtitle}</sup>',
                         color_discrete_map=color_map,
                         )
        
        # Set diameter
        fig.update_traces(marker=dict(size=dot_diameter))
        
        fig.update_layout(
            # Font settings
            font=dict(family='Arial, sans-serif', size=20, color="#000000"),
            title=dict(font=dict(size=40, family='Arial, sans-serif', color="#000000"), x=0.025, xanchor="left"),
            # Background and borders
            plot_bgcolor="white",
            paper_bgcolor="white",
            # Gridlines
            xaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                tickangle=45,
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=x_label,
            ),
            yaxis=dict(
                gridcolor="rgba(200, 200, 200, 0.5)",
                linecolor="#000000",
                rangemode='tozero',           # <— force start at 0
                title_font=dict(size=24, family="Arial, sans-serif"),
                title_text=y_label,
            ),
            # Legend
            showlegend=True,
            legend=dict(
                font=dict(size=24, family="Arial, sans-serif"),
                bordercolor="white",
                borderwidth=1,
                bgcolor="white",
                title=dict(text=""),  # Add this line to remove title: "variable"
            ),
            # Remove hover effects and other embellishments
            hovermode="x",
        )
        pio.write_image(fig, output_path, format='png', width=1280, height=720)
        
        print(f"Plot saved as '{output_path}'.")