import numpy as np

def f(h):
    return abs((1 - 5*h)**(0.5/h) - np.exp(-2.5))

hs = np.arange(0.0001, 0.1, 0.0000001)
valid_hs = [h for h in hs if f(h) < 0.001]

h = np.max(valid_hs)
print("h = ",h)
print("n = ", np.ceil(0.5/h))
print(f(h))