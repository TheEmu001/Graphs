import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

from scipy.spatial.distance import pdist, squareform
from sklearn.metrics.pairwise import euclidean_distances

# prevent numpy exponential
# notation on print, default False
np.set_printoptions(suppress=True)

# path = "Vglut-cre C137 F4+_2DLC_resnet50_VGlutEnclosedBehaviorApr25shuffle1_151500.csv"
# path = "Vglut-cre C137 F3-_2DLC_resnet50_VGlutEnclosedBehaviorApr25shuffle1_151500.csv"
# path = "Vglut-cre C162 F1DLC_resnet50_EnclosedBehaviorMay27shuffle1_307000.csv"
data_df = pd.read_csv(path, skiprows=3, names=['frameNo', 'snoutX', 'snoutY', 'snoutLike',
                                                'LeftEarX', 'LeftEarY', 'LeftEarlikelihood', 'rightearx', 'righteary',
                                                'rightearlikelihood', 'leftforepawx', 'leftforepawy',
                                                'leftforewlikelihood', 'rightforepawx', 'rightforepawy',
                                                'rightforepawlikelihood', 'lefthindpawx', 'lefthindpawy',
                                                'lefthindpawlikelihood', 'righthindpawx', 'righthindpawy',
                                                'righthindpawlikelihood', 'tailbasex', 'tailbasey', 'taillikelihood'])

# calculate the time elapsed per frame and append column
data_df['Time Elapsed'] = data_df['frameNo'] / 30

# calculate the difference from row under to row before
# then calculate absolute value
data_df['|diff X|'] = data_df['snoutX'].diff(-1)
data_df['|diff X|'] = data_df['|diff X|'].abs()

data_df['|diff Y|'] = data_df['snoutY'].diff(-1)
data_df['|diff Y|'] = data_df['|diff Y|'].abs()

# calculating the cummulative sum down the column
data_df['sumX'] = data_df['|diff X|'].cumsum()
data_df['sumY'] = data_df['|diff Y|'].cumsum()

# squaring delta x and y values
data_df['deltax^2'] = data_df['|diff X|']**2
data_df['deltay^2'] = data_df['|diff Y|']**2

# adding deltaX^2 + deltaY^2
data_df['deltaSummed'] = data_df['deltax^2'] + data_df['deltay^2']

# taking square root of deltaX^2 + deltaY^2
data_df['eucDist'] = data_df['deltaSummed']**(1/2)
data_df['eucDistSum'] = data_df['eucDist'].cumsum()

print(data_df)

# what's being plotted
# plt.plot(data_df['Time Elapsed'], data_df['sumX'],color='blue', marker='o', markersize=0.1, linewidth=0.1, label='xSum')
# plt.plot(data_df['Time Elapsed'], data_df['sumY'],color='red', marker='o', markersize=0.1, linewidth=0.1, label='ySum')
plt.plot(data_df['Time Elapsed'], data_df['eucDistSum'],color='green', marker='o', markersize=0.1, linewidth=0.1, label='distance')

# plot formatting
plt.xlabel('time (seconds)')
plt.ylabel('distance travelled (pixels)')
plt.legend(loc=2)
# plt.title('total distance traveled vs. time: ' + path)
animal = []
animal[:] = ' '.join(path.split()[2:5])
plt.title('Total Distance vs. Time for: ' + ' '.join(path.split()[:2]) + " "+ ''.join(animal[:2]))
# plt.axvspan(300, 600, alpha=0.25, color='blue')
plt.show()