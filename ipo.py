'''
    Downalod data from https://www.iposcoop.com/scoop-track-record-from-2000-to-present/

'''
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model


ipos = pd.read_csv('data/ipo_data.csv')
print( ipos.head())