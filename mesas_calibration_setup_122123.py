# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:52:28 2023

@author: ks983
"""



import os
from spotpy.examples.hymod_python.hymod import hymod
from spotpy.objectivefunctions import rmse
from spotpy.parameter import Uniform
import mesas
from mesas.sas.model import Model
import pandas as pd
import numpy as np 


class calibration_setup (object):
    STmin = Uniform(low = 0, high = 250, optguess = 0)
    STmax = Uniform(low = 250, high = 10000, optguess = 3000)
    
    def __init__(self, obj_func = None):
       df = pd.read_csv('C:/Users/ks983/OneDrive/Documents/EXP1_PL7_testdata_gapfilled.csv')
       self.df = df
       self.obj_func = obj_func
       self.trueObs = self.df.iloc[:,-1]
    
    def simulation(self, x):
    
        sas_specs = {
         "T (mL)":{
            "SAS func": {
                 "ST":[x[0],x[1]]
                 }
             }
         }
                     
              
         
        solute_parameters = {
             "2H_P (permille)":{
                 
                 
                 }
             
             }
        
                
        options = {
                 
                 "verbose" : True
             }


        model = Model(data_df = self.df, sas_specs = sas_specs, solute_parameters = solute_parameters)
        model.run()
        results = model.data_df.iloc[:,-1]
        sim = []
        for val in results:
            sim.append(val)
        return sim

    def evaluation(self):
        return self.trueObs
    
    def objectivefunction(self, simulation, evaluation, params = None):
        if not self.obj_func:
            # This is used if not overwritten by user
            like = rmse(evaluation, simulation)
        else:
            # Way to ensure flexible spot setup class
            like = self.obj_func(evaluation, simulation)
        return like
        
       
