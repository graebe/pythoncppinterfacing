import numpy as np
data = np.random.rand(100)
def pipeline(d):
    return d**2
data_processed = pipeline(data)
