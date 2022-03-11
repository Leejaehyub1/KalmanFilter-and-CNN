from scipy.optimize import fsolve
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math


class Beacon:
    x, y, N, M_Power = 0, 0, 0, 0
    mu, sigma = 0, 0


    def __init__(self, x, y, N, M_Power):
        self.x = x
        self.y = y
        self.N = N
        self.M_Power = M_Power

    def distance(self, RSSI):
        return math.pow(self.N, (self.M_Power - RSSI) / (10 * self.N))

    def set_mu_sigma(self, a, b, c):
        temp = []

        temp.append(self.distance(a))
        temp.append(self.distance(b))
        temp.append(self.distance(c))
        self.mu, self.sigma = np.mean(temp), np.std(temp)




def findIntersection(fun1, fun2, x0):
    return fsolve(lambda x: fun1(x) - fun2(x), x0)




B1 = Beacon(10, 0, 2, -55)
B2 = Beacon(15, 0, 2, -55)

B1.set_mu_sigma(-69, -72, -75)
B2.set_mu_sigma(-80, -85, -87)

np.random.seed(0)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5



mu1, sigma1 = B1.mu, B1.sigma
mu2, sigma2 = B2.mu, B2.sigma







x = np.linspace(0, 10, 1000)
g3 = (1 / np.sqrt(2 * np.pi * B2.sigma ** 2)) * np.exp(-(x - (B2.mu)) ** 2 / (2 * B2.sigma ** 2))

x = np.linspace(5, 20, 1000)
g4 = (1 / np.sqrt(2 * np.pi * B2.sigma ** 2)) * np.exp(-(x - (-B2.mu + B2.x)) ** 2 / (2 * B2.sigma ** 2))

line = lambda x: ((1 / np.sqrt(2 * np.pi * B1.sigma ** 2)) * np.exp(-(x - (B1.mu + B1.x)) ** 2 / (2 * B1.sigma ** 2))) - (1 / np.sqrt(2 * np.pi * B2.sigma ** 2)) * np.exp(-(x - (-B2.mu + B2.x)) ** 2 / (2 * B2.sigma ** 2))
solution = fsolve(line, (B1.x + B2.x)//2)
print(solution)

plt.subplot(2, 3, 1)
x = np.linspace(0, 10, 1000)
plt.plot(x, stats.norm.pdf(x, loc=B1.mu, scale= B1.sigma))

plt.subplot(2, 3, 2)
x = np.linspace(5, 20, 1000)
plt.plot(x, stats.norm.pdf(x, loc=B1.mu + B1.x, scale= B1.sigma))

plt.subplot(2, 3, 3)
x = np.linspace(0, 10, 1000)
plt.plot(x, stats.norm.pdf(x, loc=B2.mu, scale=B2.sigma))

plt.subplot(2, 3, 4)
x = np.linspace(5, 20, 1000)
plt.plot(x, stats.norm.pdf(x, loc=-B2.mu + B2.x, scale= B2.sigma))

plt.subplot(2, 3, 5)
x = np.linspace(5, 20, 1000)
plt.plot(x, stats.norm.pdf(x, loc=B1.mu + B1.x, scale= B1.sigma))
plt.plot(x, stats.norm.pdf(x, loc=-B2.mu + B2.x, scale= B2.sigma))

plt.show()
