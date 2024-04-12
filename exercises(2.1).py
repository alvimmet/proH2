import time
from machine import Pin, I2C
from filefifo import Filefifo



data = Filefifo(10, name='capture_250Hz_01.txt')

prev_data = data.get()
prev_slope = None
peaks = []
i = 0

while len(peaks) < 3:
    current_data = data.get()
    slope = current_data - prev_data
    if prev_slope is not None and prev_slope > 0 and slope < 0:
        peaks.append(i-1)
    prev_slope = slope
    prev_data = current_data
    i += 1

for i in range(len(peaks)-1):
    interval_samples = peaks[i+1] - peaks[i]
    interval_seconds = interval_samples / 250
    frequency = 1 / interval_seconds

print('interval_samples: {} samples'.format(interval_samples))
print('interval_seconds: {} seconds'.format(interval_seconds))
print('Frequency: {} Hz'.format(frequency))





