import pandas as pd

def load_and_process_data(file_path):
    data = pd.read_csv(file_path)
    relevant_columns = ['Crop', 'Sowing year', 'Harvest year', 'Sowing month', 'Harvesting month', 'P', 'E', 'Location']
    crop_data = data[relevant_columns]
    crop_data.dropna(subset=['Crop', 'Sowing year', 'Harvest year', 'Sowing month', 'Harvesting month'], inplace=True)
    crop_data['Sowing year'] = crop_data['Sowing year'].astype(int)
    crop_data['Harvest year'] = crop_data['Harvest year'].astype(int)
    crop_data['Sowing month'] = crop_data['Sowing month'].astype(int)
    crop_data['Harvesting month'] = crop_data['Harvesting month'].astype(int)
    return crop_data

if __name__ == "__main__":
    file_path = '../Data/Database.csv'
    crop_data = load_and_process_data(file_path)
    print(crop_data.head())
