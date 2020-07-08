from neuron import Neuron
from settings import weights_table, bias_table, neuron_count

class Layer:
    def __init__(self, layerNumber):
        self.neurons = []
        for i in range(neuron_count):
            self.hidden = Neuron(weights_table[layerNumber][i],
                bias_table[layerNumber][i])
            self.neurons.append(self.hidden)
    
    def layerResult(self, inputData):
        result = []
        for i in self.neurons:
            result.append(i.feedForward(inputData))
            print('Neuron -', i.weights)
        return result

