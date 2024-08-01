def define_parameters(crop_data):
    unique_crops = crop_data['Crop'].unique()
    Ci = {crop: 100 + i*50 for i, crop in enumerate(unique_crops)}
    si = {crop: crop_data[crop_data['Crop'] == crop]['Sowing month'].values[0] for crop in unique_crops}
    ti = {crop: (crop_data[crop_data['Crop'] == crop]['Harvesting month'].values[0] -
                 crop_data[crop_data['Crop'] == crop]['Sowing month'].values[0]) for crop in unique_crops}
    Ei = {crop: crop_data[crop_data['Crop'] == crop]['Harvesting month'].values[0] for crop in unique_crops}
    Yi = {crop: 50 + i*10 for i, crop in enumerate(unique_crops)}
    Di = {crop: 100 + i*20 for i, crop in enumerate(unique_crops)}
    Bi = {crop: 2 for crop in unique_crops}
    Wi = {crop: crop_data[crop_data['Crop'] == crop]['P'].values[0] / 10 for crop in unique_crops}
    W = 150
    return Ci, si, ti, Ei, Yi, Di, Bi, Wi, W

if __name__ == "__main__":
    from load_data import load_and_process_data

    file_path = '../Data/Database.csv'
    crop_data = load_and_process_data(file_path)
    parameters = define_parameters(crop_data)
    for name, param in zip(['Ci', 'si', 'ti', 'Ei', 'Yi', 'Di', 'Bi', 'Wi', 'W'], parameters):
        print(f"{name}: {param}")
