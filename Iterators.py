import numpy as np

def sinx_x(x):
    if x == 0:
        return 1
    return np.sin(x) / x


def cosx_x(x):
    if x == 0:
        return 1
    return np.cos(x) / x


t_range = np.arange(-100, 100, 0.01)
for t in t_range:
    sinx_x(t)
    cosx_x(t)

if __name__ == "__main__":
    print(sinx_x(40))
    print(cosx_x(40))
