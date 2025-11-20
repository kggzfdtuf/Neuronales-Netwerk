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
        for i in range(len(inputs)):
            for j in range(len(self.weights["input-hidden"][i])):
                hidden_inputs[j] += (x, y)
        for i in range(len(hidden_inputs)):
            for j in range(len(self.weights["hidden-output"][i])):
                output += self.weights["hidden-output"][i][j] * (inputs[i] + self.biases["hidden"][i])
        return output + self.biases["output"][0]