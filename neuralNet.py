import numpy as np
from layer import Layer
from neuron import Neuron
from settings import layer_count, neuron_count, weights_table, bias_table

class NeuralNetwork:
    def __init__(self):
        self.neuralNet = []
        for i in range(layer_count):
            self.layer = Layer(i)
            self.neuralNet.append(self.layer)

    def process(self, data):
        tmpData = self.neuralNet[0].layerResult(data)
        for i in range(1, len(self.neuralNet)):
            tmpData = self.neuralNet[i].layerResult(tmpData)
        return tmpData

    def outNeuron(self, data):
        out = Neuron(weights_table[layer_count], bias_table[layer_count])
        result = out.feedForward(data)
        return result