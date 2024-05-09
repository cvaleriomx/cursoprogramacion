import turtle as t
from random import random
suma=0
for i in range(100):
    steps = int(random() * 50)
    steps=0.1
    angle = int(random() * 360)
    angle=0
    suma=suma+steps
    print(suma)
    #input()
    t.right(angle)
    t.fd(steps)
    
