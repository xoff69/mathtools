# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
import numpy as np

h=6.62607015e-34 #J⋅Hz−1
hbar=h/(2*math.pi)
c=3e8
EV=1.602e-19

locarac=1e-15 # femto
print(h)
print(hbar)

E=(hbar*c)/locarac/EV
print("Energie caractéristique: ",E,"eV, ", round(E*1e-6,2)," MeV")