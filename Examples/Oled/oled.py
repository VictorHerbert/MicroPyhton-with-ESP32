# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
import time

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(19), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def rect(x,y,dx,dy):
    for i in range(x,x+dx):
        oled.pixel(i,y,1)
        oled.pixel(i,y+dy,1)
    for i in range(y,y+dy):
        oled.pixel(x,i,1)
        oled.pixel(x+dx,i,1)
        
'''
    for i in range(x,x+dx):
        for j in range(y+dy):
            oled.pixel(i,j,1)
'''
def circle(x,y,r):
    import math
    def dist(x,y,a,b):
        return math.sqrt((x-a)*(x-a)+(y-b)*(y-b))
    for i in range(oled_width):
        for j in range(oled_height):
            oled.pixel(i,j,abs(dist(x,y,i,j) - r) < .5)




for i in range(50):
    print(i)
    oled.fill(0)
    rect(10,10,i,i)
    oled.show()    
