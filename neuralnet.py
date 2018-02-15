# Load Dependency:
import numpy as np


# Activation Function:
def activate(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    

# Input Dataset:
_input = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    


# Output Dataset            
output = np.array([[0,0,1,1]]).T


# Set Seed - For reproducibility 
np.random.seed(5)


# Synaptic Random Weights With Mean 0
synapse = 2*np.random.random((3,1)) - 1


# Putting It Together:
for j in xrange(70000):

  # Layers
    
    # Forward propagation
    layer1 = _input
    layer2 = activate(np.dot(layer1,synapse))

    # Calculate Error (Actual - Predicted Values)
    error = output - layer2

    # Multiply The Error By Slope of The Sigmoids (Here we calculate the Sigmoid's derivative) 
    delta = error * activate(layer2,True)

    # Update Weights
    synapse += np.dot(layer1.T,delta)

print "Output After Training:"
print layer2

