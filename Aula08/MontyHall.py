# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:39:26 2016

@author: sabri
"""


import random

play = 10*(10**5)

door = ["Bode", "Bode", "Carro"]
loss = 0
win = 0

for i in range(play):

    a = random.randrange(0,3)
    choose = door[a]
    #vc escolhe o numero a. Se vc trocar, em a=0 vc ganha, em a=1 vc tb ganha e em a=2 vc perde :(
    #ps: isso somente se o cara te mostrar a porta do bode!
    if a == 0 or a == 1:
        win += 1
    else:
        loss += 1

porcentagem = (win/play) * 100
print("Carros ganhos: {0}".format(win))
print("Bodes ganhos: {0}" .format(loss))
print("Você ganhou um carro {0}% das vezes".format(porcentagem))