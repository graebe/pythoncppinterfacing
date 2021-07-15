import numpy as np
data = np.arange(0,10)
class processor():
    def __init__(self, exp):
        self.exp = exp
    def process(self, d):
        return d**self.exp
p = processor(exp=2)
data_processed = p.process(data)
print('data_processed: {}'.format(data_processed))