import standard_chart_generation as scg
from datetime import datetime

def generate(chart_types, vehicle_name, display_name, file_name, year_x_tick_step_size=5, month_x_tick_step_size=60, mass_step_size=1000):
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

start_time = datetime.now()
print("Start time: ", start_time)

generate("single family scatter", ['Antares 110', 'Antares 120', 'Antares 130', 'Antares 230', 'Antares 230+'], "Antares", "antares", 1, 12)
generate("single scatter", "Falcon 9", "Falcon 9", "f9", 1, 12)
generate("single", "Falcon Heavy", "Falcon Heavy", "f9h", 1, 12)
generate("single family", ['Atlas 1', 'Atlas 2', 'Atlas 3', 'Atlas 5'], "Atlas Orbital", "atlas")
generate("single scatter", "Electron", "Electron", "electron", 1, 12, 10)
generate("single family scatter", ['Titan 2', 'Titan 3', 'Titan 4'], "Titan Orbital", "titan")
generate("single", "Soyuz", "Soyuz", "soyuz")
generate("single family", ['Delta 1', 'Delta 2', 'Delta 3', 'Delta 4M', 'Delta 4H'], "Delta Orbital", "delta")
generate("single family", ["Ariane 1", "Ariane 2", "Ariane 3", "Ariane 4", "Ariane 5", "Ariane 6"], "Ariane", "ariane")

print("End time: ", datetime.now())
print("Elapsed time: ", datetime.now() - start_time)