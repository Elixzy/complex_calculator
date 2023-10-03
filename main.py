import machine
from machine import Pin, SPI
from st7789py import ST7789, color565, BLACK, WHITE
from fonts import vga2_16x16 as font1
from fonts import vga2_8x8 as font2
import time
import cmath
import bluetooth
from BLE1 import BLEUART
import random

machine.freq(240000000)
name='esp'
ble=bluetooth.BLE()
uart= BLEUART(ble, name)

pin_st7789_res = Pin(17, Pin.OUT)
pin_st7789_dc = Pin(5, Pin.OUT)
lista=Pin(21, Pin.IN, Pin.PULL_DOWN)
grafica=Pin(22, Pin.IN, Pin.PULL_DOWN)
zoomh=Pin(32, Pin.IN, Pin.PULL_DOWN)
zooml=Pin(19, Pin.IN, Pin.PULL_DOWN)

spi2 = SPI(2, 60000000, polarity=1)
display = ST7789(spi2, 240, 240, reset=pin_st7789_res, dc=pin_st7789_dc, rotation=0)
counter=0
disp_range=1
numeros={}
block=True

for i in range(4000):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    display.fill_rect(r,g,4,4,color565(r,g,b))

display._text16(font1, "COMPLEX", 65,40)
display._text16(font1, "CALCULATOR", 40,80)
display._text16(font1, "BY", 110,120)
display._text16(font1, "ELI", 103,160)
time.sleep(3)
display.fill(BLACK)

def graficar(n):
    x=230
    display.fill(BLACK)
    display.vline(120,0,240,WHITE)
    display.hline(0,120,240,WHITE)
    display._text8(font2, "R", 0, 105)
    display._text8(font2, "I", 110, 0)
    
    for clave, valor in numeros.items():
        r=random.randint(20,255)
        g=random.randint(20,255)
        b=random.randint(20,255)
        display.line(120,120, int(120+valor.real*n), int(120-valor.imag*n), color565(r,g,b))
        display._text8(font2, f"{clave}: {valor}", 0, x, color565(r,g,b))
        x-=10

def show_nums():
    display.fill(BLACK)
    x=0

    for clave, valor in numeros.items():
        display._text16(font1, f"{clave}: {valor}", 0, x)
        print(f"{clave}: {valor}")
        x+=32

def on_rx():
    global counter
    complejo=str(uart.read().decode().strip())

    if "<" in complejo:
        counter+=1
        partes=complejo.split("<")
        numeros[f"z{counter}"]=cmath.rect(float(partes[0]), float(partes[1]))
        show_nums()

    elif "=" in complejo:
        partes=complejo.split("=")
        zt = eval(partes[1],numeros)
        numeros["zt"]=zt
        show_nums()

    elif "+" in complejo:
        counter+=1
        partes=complejo.split("+")
        numeros[f"z{counter}"]=complex(float(partes[0]), float(partes[1].replace('j', '')))
        show_nums()

    elif "-" in complejo:
        counter+=1
        partes=complejo.split("-")
        numeros[f"z{counter}"]=complex(float(partes[0]), float(partes[1].replace('j', ''))*-1)
        show_nums()

uart.irq(handler=on_rx)

while True:

    if lista.value() and block:
        show_nums()
        block=False
    
    elif grafica.value() and block:
        graficar(disp_range)
        block=False
    
    elif zoomh.value() and block:
        disp_range+=1
        graficar(disp_range)
        block=False

    elif zooml.value() and block:
        disp_range-=1

        if disp_range<1:
            disp_range=1

        graficar(disp_range)
        block=False
    else:
        block=True
    
    time.sleep(0.01)