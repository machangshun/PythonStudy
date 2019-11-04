import pygame,sys
import pyecharts
import turtle as tr
for i in range(4):
    tr.forward(200)
    tr.right(90)
x = 370
for i in range(0, 600001):
    j = i / 10000
    x += j
    print(int(x))