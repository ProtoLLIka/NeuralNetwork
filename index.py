from neuralNet import NeuralNetwork
from dataGenerator import getInputData
net = NeuralNetwork()
inputData = getInputData()
print(net.outNeuron(net.process(inputData)))
