
import os
from source import load_data
import pickle

#%% load data

item_load = False



if item_load:

    Data = load_data.load()
    pickle_out = open("save\data_init","wb")
    pickle.dump(Data, pickle_out)
    pickle_out.close()

else:
    pickle_in = open("save\data_init","rb")
    Data = pickle.load(pickle_in)
