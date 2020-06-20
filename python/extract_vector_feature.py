import os
import pickle
from converter import createWaveFileFromPath

path="../bird_sounds"
file_names = os.listdir(path)
wavefiles = []
for f in file_names:
    obj = createWaveFileFromPath(path + "/" + f)
    obj.show()
    wavefiles.append(obj)

    
with open('list_wavefile.obj', 'wb') as output:
    pickle.dump(wavefiles, output, pickle.HIGHEST_PROTOCOL)