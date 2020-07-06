import numpy as np
from neuron import Neuron
from settings import layer_count

class NeuralNetwork:
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0