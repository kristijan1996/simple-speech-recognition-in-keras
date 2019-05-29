import librosa  # For audio processing
import os       # Access to file system 
from sklearn.model_selection import train_test_split  # To split the dataset into training and testing sets
from keras.utils import to_categorical  # One-hot encoding of integers
import numpy as np  # Aux functions for dealing with tensors
from tqdm import tqdm  # Verbose progress bar while iterating through loops

# Variable for storing path to folders with audio files
DATA_PATH = './data/'


""" GET_LABELS
    Function which lists names of all folders contained in
    path input variable, and returns tuple containing names
    of folders, associated integer with that name, as well
    as one-hot representation of that integer
    
    input:  path - path to folders which contain audio files
    output: tuple (labels, labelIndices, oneHotIndices)
"""
def getLabels(path=DATA_PATH):
    # List all the folders in ./data/ folder
    labels = os.listdir(path)
    # Associate each folder with a number
    labelIndices = np.arange(0, len(labels))
    # Return the tuple containing folder names, their respective
    # associated numbers, as well as one hot representations of those numbers
    return labels, labelIndices, to_categorical(labelIndices)


""" AUDIO2MFCC
    Function which calculates MFCCs of passed audio file and
    returns matrix with dimensions dim (MxN, M=dim(0), N=dim(1))
    of MFCs
    
    input:  path - path to audio file
            dim - [M,N] list of row and column dimensions
    output: mfcc - MxN matrix containing MFCs
"""
def audio2mfcc(filePath, dim=[20,20]):
    M, N = dim
    # Read the audio and its sampling rate
    signal, fs = librosa.load(filePath, mono=True, sr=None)
    # decimate signal to ease the burden on CPU
    signal = signal[::3]
    # and calculate MFC transform
    mfcc = librosa.feature.mfcc(signal, sr=fs, n_mfcc=M)

    # If N exceeds mfcc lengths then pad the remaining ones
    if (N > mfcc.shape[1]):
        padWidth = N - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, padWidth)), mode='constant')
    # otherwise cut off the remaining parts
    else:
        mfcc = mfcc[:, :N]

    return mfcc


""" TRANSFORM_DATA
    Function which saves all the .wav files into .npy files,
    after transforming them to matrices using mel-frequency
    cepstral transformation
    
    input:  path - path to folders which contain audio files
            dim - MxN dimensions of matrix MFC tranform produces
    output: .npy files saved in path/npy_files/ 
"""
def transformData(path=DATA_PATH, dim=[20,20]):
    # Acquire the dataset labels from the name
    # of the folders .wav files are saved in
    labels, _, _  = getLabels(path)
    
    # For each of those folders
    for label in labels:
        # init list to place all of the matrices in,
        mfccsList = []
        # take out all of the .wav files in them
        wavFiles = [path + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]
        # and for each of those files
        for wavFile in tqdm(wavFiles, "Saving vectors of label - '{}'".format(label)):
            # calculate MFC transform of the signal
            mfcc = audio2mfcc(wavFile, dim)
            # and concatenate it to the mfccsList vector 
            mfccsList.append(mfcc)
        # After processing one class of audio files, each with
        # same spoken word, save the list of matrices in a .npy
        # file which is to be used directly by a CNN
        np.save('./npy_files/' + label + '.npy', mfccsList)
        
        
""" GET_TRAIN_TEST_DATA
    Function which separates saved .npy files containing
    MFCCs of audio files into training and test sets with 6/4
    ratio
    
    input:  path - path to folder with .npy files
            splitRatio - procentage of files which will be
                         contained in the training set
            randomState - arbitrary integer to seed the random
                          number generator
    output: list containing train-test split of inputs
"""
def getTrainTestData(path='./npy_files/', splitRatio=0.6, randomState=42):
    # Get available labels
    labels, indices, _ = getLabels(DATA_PATH)

    # Getting first arrays
    X = np.load(path + labels[0] + '.npy')
    y = np.zeros(X.shape[0])

    # Append all of the dataset into one single array, same goes for y
    for i in indices:
        x = np.load(path + labels[i] + '.npy')
        X = np.vstack((X, x))
        y = np.append(y, i*np.ones(x.shape[0]))

    return train_test_split(X, y, test_size=(1 - splitRatio), random_state=randomState, shuffle=True)

