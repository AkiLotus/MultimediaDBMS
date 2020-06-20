import pickle
from sys import argv
from backend_tree import KDTree
from converter import createWaveFileFromPath

with open('premade_tree.obj', 'rb') as input:
    tree = pickle.load(input)
    
    directory = argv[1]
    obj = createWaveFileFromPath(directory)
    output_list = tree.k_search(obj)
    for data_found, distance in output_list: print(data_found.data.location, distance)
