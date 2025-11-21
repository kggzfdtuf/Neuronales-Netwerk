import random
class NeuralNetwork():
    def __init__(self, old_brain = None):
        self.weights = []
        if old_brain is None:
            for i in range(8):
                for j in range(5):
                    for k in range(2):
                        self.weights["input-hidden"][i][j][k] = random.random()
            for i in range(5):
                for k in range(2):
                    self.weights["hidden-output"][i][0][k] = random.random()
            for i in range(8):
                for k in range(2):
                    self.biases["input"][i][k] = random.random(-1, 1)
            for i in range(5):
                for k in range(2):
                    self.biases["hidden"][i][k] = random.random(-1, 1)
            for k in range(2):
                self.biases["output"][0][k] = random.random(-1, 1)
        else:
            self = old_brain.mutate()
                    #inputs = [vel, acc, raytracing 6 times]
    def compute(self, inputs):
        hidden_inputs = []
        output_input = []
        output = []
        x = [0, 0]
        for j in range(len(self.weights["input-hidden"][i])):
            for i in range(len(inputs)):
                for k in range(2):
                    x[k] += self.weights["input-hidden"][i][j][k] * (inputs[i][k] + self.biases["input"][i][k])
            hidden_inputs[j] += (x[0], x[1])
        for j in range(len(self.weights["hidden-output"][i])):
            for i in range(len(hidden_inputs)):
                for k in range(2):
                    x[k] += self.weights["hidden-output"][i][j][k] * (hidden_inputs[i][k] + self.biases["hidden"][i][k])
            output_input[j] += (x[0], x[1])
        for i in range(len(output_input)):
            for k in range(2):
                x[k] += self.weights["hidden-output"][i][0][k] * (hidden_inputs[i][k] + self.biases["hidden"][i][k])
        output += (x[0], x[1])
    def mutate(self):
        for i in self.weights:
            for j in self.weights[i]:
                for k in self.weights[i][j]:
                    for l in self.weights[i][j][k]:
                        self.weights[i][j][k][l] += random.random(-1, 1)
                        if self.weights[i][j][k][l] >= 1:
                            self.weights[i][j][k][l] = 1
                        if self.weights[i][j][k][l] <= -1:
                            self.weights[i][j][k][l] = -1
        for i in self.biases:
            for j in self.biases[i]:
                for k in self.biases[i][j]:
                    self.biases[i][j][k] += random.random(-1, 1)
                    if self.biases[i][j][k] >= 1:
                        self.biases[i][j][k] = 1
                    if self.biases[i][j][k] <= -1:
                        self.biases[i][j][k] = -1
