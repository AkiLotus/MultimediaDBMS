import os
import librosa
import numpy as np
import pickle

# tinh toan gia tri min,max cho tung feature
def average_energy(arr):
    return np.average(arr*arr)

def createWaveFileFromPath(path):
    x,sr = librosa.load(path)
    # chroma_stft = librosa.feature.chroma_stft(x,sr)
    ave_energy = average_energy(x);
    rms = librosa.feature.rms(x)
    spec_cent = librosa.feature.spectral_centroid(x,sr)
    spec_bw = librosa.feature.spectral_bandwidth(x,sr)
    rolloff = librosa.feature.spectral_rolloff(x,sr)
    zcr = librosa.feature.zero_crossing_rate(x)
    # feature_vector = [np.mean(chroma_stft), np.mean(rms), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]
    feature_vector = [ave_energy, np.mean(rms), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]
    # mfcc = librosa.feature.mfcc(x,sr)
    # for e in mfcc:
        # feature_vector.append(np.mean(e))
    return feature_vector;

path="../bird_sounds"
file_names = os.listdir(path)
arr = []
for f in file_names:
    obj = createWaveFileFromPath(path + "/" + f)
    arr.append(obj)

min_arr = np.vstack(arr).min(axis=0)
max_arrr = np.vstack(arr).max(axis=0)
print("Min value: ",min_arr)
print("Max value: ",max_arrr)

with open('normalize.obj', 'wb') as output:
    pickle.dump(min_arr, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(max_arrr, output, pickle.HIGHEST_PROTOCOL)