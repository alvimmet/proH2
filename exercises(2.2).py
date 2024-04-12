import time
from machine import Pin, I2C
from filefifo import Filefifo


data = Filefifo(10, name='capture_250Hz_01.txt')

samples = [data.get() for _ in range(2 * 250)]  
min_val = min(samples)
max_val = max(samples)

scaled_samples = [(sample - min_val) / (max_val - min_val) * 100 for sample in samples]

for scaled_sample in scaled_samples:
    print(scaled_sample)

for _ in range(10 * 250):  
    sample = data.get()
    scaled_sample = (sample - min_val) / (max_val - min_val) * 100
    print(scaled_sample)
    

