from math import exp

B = 50000
k = 0.2
t = 0
C = 9
nt = B/(1 + C*exp(-k*t))

while t <= 24:
    print(f"t = {t:2.0f} nt = {nt:5.0f}")
    t += 1
    nt = B/(1 + C*exp(-k*t))