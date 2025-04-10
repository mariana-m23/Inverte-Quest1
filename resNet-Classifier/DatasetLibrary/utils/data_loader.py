import pandas as pd
import json
import os

def load_csv(file_path):  #this will load a csv dataset
    return pd.read_csv(file_path)

def load_json(file_path):  #this loads a json dataset
    with open(file_path, 'r') as f:
        return json.load(f)
    
def load_excel(file_path):
    return pd.read_excel(file_path)

def list_datasets(dataset_folder="datasets"):  # this will lists the datasets in the dataset folder
    return[f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]


