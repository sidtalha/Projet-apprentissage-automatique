import numpy as np
import scipy as sp
import pdb
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import pdb


"""
Created on Tue Apr  7 17:11:51 2020

@author: sidahmed.talha
"""


def feature(data):
    nsub = np.unique(data.subject)
    nexp = np.unique(data.experience)
    nac = np.unique(data.action)
    F = np.array([])
    experience = np.array([])
    subject = np.array([])
    lab = np.array([])

    for k1 in nsub:
        print(k1)
        for k2 in nexp:
            for k3 in nac:
                A = data[(data.subject == k1) & (data.experience == k2) & (data.action == k3)]
                S2 = np.array([])
                for k in range(6):
                    S1 = A.iloc[:, k]
                    S1 = np.array([S1.std(), S1.mean(), S1.min(), S1.max()])
                    S1 = S1.reshape((S1.shape[0], 1))
                    if len(S2) != 0:
                        S2 = np.concatenate((S2, S1), axis=0)
                    else:
                        S2 = S1

                if len(F) != 0:
                    F = np.concatenate((F, S2), axis=1)
                else:
                    F = S2

                lab = np.concatenate((lab, k3), axis=None)
                experience = np.concatenate((experience, k2), axis=None)
                subject = np.concatenate((subject, k1), axis=None)


    lab = lab.reshape((len(lab), 1))
    experience = experience.reshape((len(lab), 1))
    subject = subject.reshape((len(lab), 1))


    stat_feature = {"feature": F, "labels": lab, "subject": subject, "experience": experience}

    return stat_feature
