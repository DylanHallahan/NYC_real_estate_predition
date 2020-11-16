import pickle
import json
import numpy as np

__area = None
__data_columns = None
__model = None


def get_estimated_price(area, bds, ba, sqft):
    try:
        loc_index = __data_columns.index(area.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bds
    x[1] = ba
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __area

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __area = __data_columns[3:]  # first 3 columns are bds, ba, sqft

    global __model
    if __model is None:
        with open('./artifacts/New_York_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)


def get_area_names(): #get for dropdown on page
    return __area


def get_data_columns(): #get for dropdown on page
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_area_names())
    print(get_estimated_price('bronx', 2, 2, 2000))
    print(get_estimated_price('bronx', 5, 2, 2000))
    print(get_estimated_price('bronx', 1, 2, 2000))
