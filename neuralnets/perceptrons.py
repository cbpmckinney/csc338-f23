import numpy as np


class Perceptron:

    def __init__(self, numinputs, biasbool=True, actfunc=None):
        
        self.numinputs = numinputs
        self.biasbool = biasbool
        self.actfunc = actfunc
        
        self.weights = np.random.default_rng().random(self.numinputs)

        if self.biasbool:
            self.bias = np.random.default_rng().random(1)
        else:
            self.bias = 0

    def evaluate(self, inputs):
        try:
            output = self.weights @ inputs + self.bias
            return output
        except:
            print("Dimension mismatch!")




Spam = Perceptron(10,True,None)

print(Spam.weights)

inputs1 = np.random.default_rng().random(10)
inputs2 = np.random.default_rng().random(20)

output1 = Spam.evaluate(inputs1)
output2 = Spam.evaluate(inputs2)

print(output1)
print(type(output1))
print(output2)









