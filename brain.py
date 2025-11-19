import random
class NeuralNetwork():
    def __init__(self, old_brain = None):
        self.weights = []
        if old_brain is None:
            for i in range(6):
                for j in range(5):
                    self.weights["input_layer"][i][j] = random.random()
            for i in range(5):
                self.weights["ouput_layer"][i][0] = random.random()
        else:
            self = old_brain.mutate()