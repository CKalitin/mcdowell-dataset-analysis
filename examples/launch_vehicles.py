import standard_chart_generation as scg

def generate(chart_types, vehicle_name, display_name, file_name, year_x_tick_step_size, month_x_tick_step_size, mass_step_size=1000):
    """ Generates charts for a given launch vehicle using specified chart types.

    Args:
        chart_types (str): String containing chart types to generate (can contain "single", "family", "scatter").
        vehicle_name (str): Simplified name of the launch vehicle.
        display_name (str): Display name for chart titles.
        file_name (str): Prefix for output files.
        year_x_tick_step_size (int): Step size for year ticks on x-axis.
        month_x_tick_step_size (int): Step size for month ticks on x-axis.
    """
    
    if "single" in chart_types:
        scg.generate_launch_vehicle_charts(
            launch_vehicle_simplified_name=vehicle_name,
            chart_title_prefix=display_name,
            output_prefix=file_name,
            mass_step_size_kg=mass_step_size,
            year_x_tick_step_size=year_x_tick_step_size,
            month_x_tick_step_size=month_x_tick_step_size,
        )

    if "scatter" in chart_types:
        scg.generate_launch_vehicle_scatter_plots(
            launch_vehicle_simplified_name=vehicle_name,
            chart_title_prefix=display_name,
            output_prefix=file_name,
            mass_step_size_kg=mass_step_size,
        )

    if "family" in chart_types:
        scg.generate_launch_vehicle_family_charts(
            launch_vehicle_simplified_name=vehicle_name,
            chart_title_prefix=display_name,
            output_prefix=file_name,
            mass_step_size_kg=mass_step_size,
            year_x_tick_step_size=year_x_tick_step_size,
        )
        
generate("single scatter", "Electron", "Electron", "electron", 1, 12, 10)
