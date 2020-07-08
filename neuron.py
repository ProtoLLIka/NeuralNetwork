import numpy as np
from sigmoid import sigmoid

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights # Веса нейрона 
        self.bias = bias # Смещение 
        
    def feedForward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total) 