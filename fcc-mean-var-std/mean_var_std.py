import numpy as np

def calculate(list):
    list = np.reshape(list,(3,3))
    calculations = {}
    list_mean = [np.mean(list, axis = 0) ,
                 np.mean(list, axis = 1) ,
                 np.mean(list.flatten())]
    
    list_variance = [np.var(list, axis = 0) ,
                     np.var(list, axis = 1) ,
                     np.var(list.flatten())]
    
    list_std = [np.std(list, axis = 0) ,
                 np.std(list, axis = 1) ,
                 np.std(list.flatten())]
    
    list_max = [np.max(list, axis = 0) ,
                 np.max(list, axis = 1) ,
                 np.max(list.flatten())]
    
    list_min = [np.min(list, axis = 0) ,
                 np.min(list, axis = 1) ,
                 np.min(list.flatten())]
    
    list_sum = [np.sum(list, axis = 0) ,
                 np.sum(list, axis = 1) ,
                 np.sum(list.flatten())]
    
    calculations = {'mean':list_mean,
                    'variance':list_variance,
                    'standard deviation':list_std,
                    'max':list_max,
                    'min':list_min,
                    'sum':list_sum}
    return calculations
