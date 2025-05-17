import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

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

    def bin_dataframe(df, value_col, bins, labels):
        """
        Sort groups into discrete bins (eg. intervals of payload mass) and count how many data points fall into each bin.
        
        Eg. mass bins and labels:
        bins = [0,1000,2000,3000]
        mass_labels = ['0-1T','1-2T','2-3T']
        
        Notice that labels are between the bins. The bins variable specifies the edges of the bins.
        """
        binned = pd.cut(df[value_col], bins=bins, labels=labels, include_lowest=True).value_counts()
        return binned.reindex(labels)
 
    def plot_histogram(dataframe, title, subtitle, x_label, y_label, output_path, color_map, barmode='stack'):
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
    
    # Example: plot_scatter_plotly(df, 'Payload_Mass', ['LEO', 'SSO', 'MEO'], 'Falcon 9 Launches vs. Payload Mass by Orbit', 'Payload Mass (tonnes)', 'Number of Launches', 'examples/outputs/f9_mass_by_orbit.png')
    def plot_scatter(dataframe, x_col, y_cols, title, subtitle, x_label, y_label, dot_diameter, output_path, color_map):
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
            output_path (string): Full path including filename to save the plot
            color_map (dictionary): y_col to color mapping, eg. {'LC40': '#ff0000', 'LC39A': '#00ff00'}
        """
        
        fig = px.scatter(dataframe,
                         x=x_col,
                         y=y_cols,
                         title=f'<b>{title}</b><br><sup>{subtitle}</sup>',
                         color_discrete_map=color_map,
                         )
        
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