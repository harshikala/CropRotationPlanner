import numpy as np  # Add this import statement
from scripts.load_data import load_and_process_data
from scripts.define_parameters import define_parameters
from scripts.crop_rotation_planner import crop_rotation_planner
from scripts.visualize_schedule import visualize_schedule, create_rotation_visualization
from scripts.utils import clean_plot_name

def main():
    file_path = 'Data/Database.csv'
    crop_data = load_and_process_data(file_path)
    parameters = define_parameters(crop_data)
    results, total_profit = crop_rotation_planner(*parameters, crop_data)

    print("Results:", results)
    print("Total Profit:", total_profit)

    crops = list(parameters[0].keys())
    time_periods = range(1, 13)
    plots = [clean_plot_name(plot) for plot in crop_data['Location'].unique().tolist()]

    visualize_schedule(results, crops, time_periods, plots)

    # Creating an example schedule for visualization purpose
    example_schedule = np.array([
        [1, 0, 2, 0],
        [0, 1, 0, 2],
        [2, 0, 1, 0],
        [0, 2, 0, 1]
    ])
    create_rotation_visualization(example_schedule, crops, plots)

if __name__ == "__main__":
    main()
