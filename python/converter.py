import librosa
import numpy as np
from wavefile import WaveFile

def normalize(vector):
    vector = np.array(vector)
    return (vector / np.sqrt(np.sum(vector ** 2)))

def createWaveFileFromPath(path):
    x,sr = librosa.load(path)
    chroma_stft = librosa.feature.chroma_stft(x,sr)
    rms = librosa.feature.rms(x)
    spec_cent = librosa.feature.spectral_centroid(x,sr)
    spec_bw = librosa.feature.spectral_bandwidth(x,sr)
    rolloff = librosa.feature.spectral_rolloff(x,sr)
    zcr = librosa.feature.zero_crossing_rate(x)
    feature_vector = [np.mean(chroma_stft), np.mean(rms), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)]
    
    mfcc = librosa.feature.mfcc(x,sr)
    for e in mfcc:
        feature_vector.append(np.mean(e))
    feature_vector = normalize(feature_vector)
    obj = WaveFile(feature_vector, path)
    return obj   
    
