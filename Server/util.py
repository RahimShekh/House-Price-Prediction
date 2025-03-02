import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[__data_columns.index('new_total_sqft')] = sqft
    x[__data_columns.index('bath')] = bath
    x[__data_columns.index('bhk')] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./Server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 4 columns are bath, balcony, bhk, new_total_sqft
        print(f"Loaded columns: {__data_columns}")

    global __model
    if __model is None:
        with open('./Server/artifacts/house_price_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(f"Estimated price for 1st Phase JP Nagar, 1000 sqft, 3 BHK, 3 bath: {get_estimated_price('1st Phase JP Nagar', 1000, 3, 3)}")
    print(f"Estimated price for 1st Phase JP Nagar, 1000 sqft, 2 BHK, 2 bath: {get_estimated_price('1st Phase JP Nagar', 1000, 2, 2)}")
    print(f"Estimated price for Kalhalli, 1000 sqft, 2 BHK, 2 bath: {get_estimated_price('Kalhalli', 1000, 2, 2)}")
    print(f"Estimated price for Ejipura, 1000 sqft, 2 BHK, 2 bath: {get_estimated_price('Ejipura', 1000, 2, 2)}")