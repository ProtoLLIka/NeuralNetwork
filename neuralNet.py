import numpy as np
from neuron import Neuron
from settings import layer_count

class NeuralNetwork:
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        # Скрытый слой из 6 нейронов
        self.hidden1 = Neuron(weights, bias)
        self.hidden2 = Neuron(weights, bias)
        self.hidden3 = Neuron(weights, bias)
        self.hidden4 = Neuron(weights, bias)
        self.hidden5 = Neuron(weights, bias)
        self.hidden6 = Neuron(weights, bias)