# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:55:20 2023

@author: ks983
"""

import numpy as np
import spotpy
import calibration_setup
from calibration_setup import calibration_setup




calibration_setup = calibration_setup(spotpy.objectivefunctions.nashsutcliffe)


rep = 5000
sampler = spotpy.algorithms.mle(calibration_setup, dbname = 'MLE_mesas', dbformat = 'csv')

sampler.sample(rep)

results = spotpy.analyser.load_csv_results('MLE_mesas')

