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


    def error(self, outputlist, truelist):
        sum = 0
        n = len(outputlist)
        m = len(outputlist[0])
        for i in range(n):
            for j in range(m):
                sum += (outputlist[i][j]-truelist[i])**2
        sum = sum/n
        return sum
    
    def gradient(self, inputlist, outputlist, truelist):
        n = len(inputlist)
        m = len(inputlist[0])
        partweights = np.zeros(m)
        partbias = 0
        for i in range(n):
            error = self.bias + outputlist[i] - truelist[i]
            partbias += error 
            for j in range(m):
                partweights[j] += error * inputlist[i][j]
        partweights *= 2/n
        partbias *= 2/n

        return (partweights, partbias)

    def updateweights(self, gradient, eta):
        self.weights = self.weights - eta*gradient[0]
        self.bias = self.bias - eta*gradient[1]
            




Spam = Perceptron(10,True,None)

print(Spam.weights)

inputs1 = np.random.default_rng().random(10)
inputs2 = np.random.default_rng().random(10)

output1 = Spam.evaluate(inputs1)
output2 = Spam.evaluate(inputs2)
print(output1, output2)








