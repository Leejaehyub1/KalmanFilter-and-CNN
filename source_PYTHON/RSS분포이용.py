from scipy.optimize import fsolve
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math

class Beacon:
    x, y, N, M_Power = 0, 0, 0, 0
    mu_RSS, sigma_RSS = 0, 0
    dataset = []

    def __init__(self, x, y, N, M_Power):
        self.x = x
        self.y = y

        #N은 환경 변수, 2~4사이의 숫자를 선택한다.
        self.N = N
        self.M_Power = M_Power

    def RSSI_to_distance(self, RSSI):
        return math.pow(10, ((self.M_Power - RSSI) / (10 * self.N)))

    def Dist_to_RSSI(self, Dist):
        return ((-10) * self.N * math.log(Dist, 10) + self.M_Power)

    def set_mu_sigma_RSS(self, a, b, c):
        temp = []
        temp.append(a)
        temp.append(b)
        temp.append(c)
        self.mu_RSS, self.sigma_RSS = np.mean(temp), np.std(temp)

    def add_RSS(self, RSS):
        self.dataset.append(RSS)
        self.mu_RSS = np.mean(self.dataset)
        self.sigma_RSS = np.std(self.dataset)


def f(B1, x):
    return ((1 / np.sqrt(2 * np.pi * (B1.sigma_RSS ** 2))) * np.exp(-(x - (B1.mu_RSS)) ** 2 / (2 * B1.sigma_RSS ** 2)))

#x좌표, y좌표, N=2(아무런 제약이 없다고 가정), M_Power
B1 = Beacon(10, 0, 2, -55)

#np.linspac(a,b,c) a부터 시작해서 b까지 총 c등분 한다.
temp = "-71	-65	-65	-66	-69	-67	-66	-74	-66	-65	-77	-66	-64	-76	-67	-69	-72	-64	-67	-71	-71	-70	-69	-68	-68	-67	-69	-68	-69	-68	-65	-74	-79	-66	-65	-65	-64	-65	-66	-65	-71	-69	-66	-72	-71	-65	-64	-66	-66	-65	-66	-69	-66	-65	-67	-65	-68	-68	-65	-66	-70	-65	-69	-66	-68	-65	-68	-70	-68	-68	-77	-75	-66	-66	-81	-65	-65	-66	-69	-65	-66	-65	-63	-66	-66	-63	-71	-45	-68	-42	-68	-65	-71	-69	-80	-79	-69	-69	-68	-70	-73	-71	-69	-69	-68	-65	-63	-65	-65	-63	-66	-68	-65	-67	-69	-64	-66	-63	-69	-67	-65	-67	-67	-67	-64	-67	-68	-68	-66	-66	-66	-68	-74	-64	-65	-65	-66	-86	-64	-65	-67	-66	-69	-66	-65	-65	-63	-67	-67	-65	-67	-67	-66	-67	-69	-68	-67	-65	-67	-67	-67	-68	-65	-73	-65	-67	-78	-68	-76	-68	-72	-74	-68	-67	-68	-67	-66	-72	-67	-66	-67	-68	-69	-67	-68	-65	-69	-65	-69	-64	-64	-68	-69	-66	-66	-65	-68	-65	-68	-69	-65	-66	-67	-66	-68	-65	-67	-66	-66	-45	-71	-40	-68	-65	-75	-67	-78	-68	-70	-75	-69	-71	-68	-64	-67	-67	-64	-62	-63	-65	-63	-65	-64	-64	-64	-66	-63	-64	-67	-69	-63	-67	-65	-66	-66	-73	-69	-69	-74	-74	-70	-68	-73	-67	-66	-64	-64	-66	-67	-66	-64	-62	-64	-62	-65	-67	-64	-63	-64	-67	-66	-64	-63"
temp = temp.split("\t")
x = [(int(i)) for i in temp]
a = [i for i in range(len(x))]
for i in x:
    B1.add_RSS(i)

y = [B1.RSSI_to_distance(i) for i in B1.dataset]
B2 = Beacon(0,0,2,-64)
# print(B2.Dist_to_RSSI(1.2))
arr = [-61.37, -63.19, -65.98, -65.22, -65.80, -70.29, -66.72]
for a in arr:
    print(B2.RSSI_to_distance(a))


# print(B2.RSSI_to_distance(-62.9))
# print(B2.RSSI_to_distance(-81))

# plt.style.use('default')
# plt.rcParams['figure.figsize'] = (20, 20)
# plt.rcParams['font.size'] = 15
# plt.rcParams['lines.linewidth'] = 2
# plt.plot(a,temp)
# plt.plot(a, y)
# plt.show()
# temp = [-61.5248, -62.9714, -65.6001, -64.7888, -65.8452, -70.3113, -66.0177, -67.1526]
# print("asdjflkasdjf")
# for t in temp:
#     print(B2.RSSI_to_distance(t))
