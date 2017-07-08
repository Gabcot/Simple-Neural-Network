#Single Layer Neural Network

from numpy import exp, array, random, dot


class NeuralNetwork():
	def __init__(self):
		random.seed(1)

		self.synaptic_weights = 2 * random.random((3,1)) - 1

	#Gradient of sigmoid to calculate slope
	def __sigmoid_derivative(self, x):
		return x * (1-x)

	#Sigmoid function to normalise between 1 an 0
	def __sigmoid(self, x):
		return 1 /(1 + exp(-x))

	def train(self, training_set_inputs, training_set_outputs, iterations_number):
		for i in xrange(iterations_number):
			output = self.predict(training_set_inputs)
			error = training_set_outputs - output

			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

			self.synaptic_weights += adjustment

	def predict(self, inputs):
		return self.__sigmoid(dot(inputs, self.synaptic_weights))



if __name__ == '__main__':

	#Init neuron
	neural_network = NeuralNetwork()

	print 'Random weights: '
	print neural_network.synaptic_weights

	training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
	training_set_outputs = array([[0, 1, 1, 0]]).T

	#Training time
	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print 'Trained weights: '
	print neural_network.synaptic_weights

	#Test with new situation
	print 'New test prediction --> [1, 0, 0]'
	print neural_network.predict(array([1, 0, 0]))
