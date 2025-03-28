# main.py
from utils.data_loader import load_csv, load_json, load_excel, list_datasets

# Example: list available datasets
datasets = list_datasets()
print("Available datasets:", datasets)

# can load a CSV dataset
csv_data = load_csv("datasets/dataset1.csv")
print("Loaded CSV Data:", csv_data.head())

# Example: load a JSON dataset
json_data = load_json("datasets/dataset2.json")
print("Loaded JSON Data:", json_data)

