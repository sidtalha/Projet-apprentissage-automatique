
import pandas as pd
import os
from scipy.io import loadmat
import re
import sys
import numpy as np


#%%


def load():
    path = 'IMU/'
    files1 = os.listdir(path)
    df = pd.DataFrame([])

    for ind, j in enumerate(files1):
        if (ind+1) % 100 == 0:
            print(str(round((ind+1)/len(files1)*100))+'%')
        D = loadmat(path+j)
        A = pd.DataFrame(D['d_iner'])

        k = list(map(int, re.findall(r'\d+', j)))

        ac = k[0]
        sub = k[1]
        exp = k[2]
        A.insert(6, "subject", sub)
        A.insert(7, "experience", exp)
        A.insert(8, "action", ac)

        df = df.append(A)
    return df