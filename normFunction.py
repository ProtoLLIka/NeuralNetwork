import numpy as np

def normalization(data):
    x = min(data)
    y = max(data)
    result = []
    for i in range(len(data)):
        result.append(float(data[i] - x)/(y - x))
    average = sum(result)/len(result)
    return average