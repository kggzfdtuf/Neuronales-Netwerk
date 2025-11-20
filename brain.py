import random
class NeuralNetwork():
    def __init__(self, old_brain = None):
        self.weights = []
        if old_brain is None:
            for i in range(8):
                for j in range(5):
                    self.weights["input-hidden"][i][j] = random.random()
            for i in range(5):
                self.weights["hidden-output"][i][0] = random.random()
            for i in range(8):
                self.biases["input"][i] = random.random(-1, 1)
            for i in range(5):
                self.biases["hidden"][i] = random.random(-1, 1)
            self.biases["output"][0] = random.random(-1, 1)
        else:
            self = old_brain.mutate()
                    #inputs = [pos, vel, acc, raytracing 5 times]
    def compute(self, inputs):
        for j in range(len(self.weights["input-hidden"][i])):
            for i in range(len(inputs)):
                for k in range(2):
                    x[k] += self.weights["input-hidden"][i][j][0] * (inputs[i][0] + self.biases["input][i][0])
            hidden_inputs[j] += (x[0], x[1])
        for j in range(len(self.weights["hidden-output"][i])):
            for i in range(len(hidden_inputs)):
                for k in range(2):
                    x[k] += self.weights["hidden-output"][i][j][0] * (hidden_inputs[i][0] + self.biases["hidden"][i][0])
            output_input[j] += (x[0], x[1])
        for i in range(len(ouput_inputs)):
            for k in range(2):
                x[k] += self.weights["hidden-output"][i][0][0] * (hidden_inputs[i][0] + self.biases["hidden"][i][0])
        output += (x[0], x[1])