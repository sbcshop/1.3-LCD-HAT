# -*- coding:utf-8 -*-
import spidev as SPI
import ST7789
import RPi.GPIO as GPIO

import time
import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



#GPIO define
RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

KEY_UP_PIN     = 26 
KEY_DOWN_PIN   = 6
KEY_LEFT_PIN   = 13 #
KEY_RIGHT_PIN  = 5
KEY_PRESS_PIN  = 19 #

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16
KEY4_PIN       = 12

RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)
disp.Init()

# Clear display.
disp.clear()

#init GPIO
# for P4:
# sudo vi /boot/config.txt
# gpio=6,19,5,26,13,21,20,16=pu
GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY4_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 240
height = 240
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.ShowImage(image,0,0)

draw.text((80, 220), 'SB-Components ', fill = "WHITE")

# try:
while 1:
    # with canvas(device) as draw:
    if GPIO.input(KEY_UP_PIN): # button is released
        draw.polygon([(120, 50), (100, 100), (140, 100)], outline=255, fill="blue")  #Up
    else: # button is pressed:
        draw.polygon([(120, 50), (100, 100), (140, 100)], outline=255, fill=0)  #Up filled
        print ("Up")
        
    if GPIO.input(KEY_LEFT_PIN): # button is released
        draw.polygon([(50, 120), (100, 100), (100, 140)], outline=255, fill="blue")  #left           
    else: # button is pressed:
        draw.polygon([(50, 120), (100, 100), (100, 140)], outline=255, fill=0)  #left filled
        print ("left") 
        
    if GPIO.input(KEY_RIGHT_PIN): # button is released
        draw.polygon([(190, 120), (140, 100), (140, 140)], outline=255, fill="blue") #right        
    else: # button is pressed:
        draw.polygon([(190, 120), (140, 100), (140, 140)], outline=255, fill=0) #right filled
        print ("right")
        
    if GPIO.input(KEY_DOWN_PIN): # button is released
        draw.polygon([(120, 190), (140, 140), (100, 140)], outline=255, fill="blue") #down        
    else: # button is pressed:
        draw.polygon([(120, 190), (140, 140), (100, 140)], outline=255, fill=0) #down filled
        print ("down")
        
    if GPIO.input(KEY_PRESS_PIN): # button is released
        draw.rectangle((140, 140,100,100), outline=255, fill="red") #center         
    else: # button is pressed:
        draw.rectangle((140, 140,100,100), outline=255, fill=0) #center filled
        print ("center")
        
    if GPIO.input(KEY1_PIN): # button is released
        draw.ellipse((0,0,30,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((0,0,30,30), outline=255, fill=0) #A button filled
        print ("KEY1")
        
    if GPIO.input(KEY2_PIN): # button is released
        draw.ellipse((60,0,90,30), outline=255, fill="orange") #B button]        
    else: # button is pressed:
        draw.ellipse((60,0,90,30), outline=255, fill=0) #B button filled
        print ("KEY2")
        
    if GPIO.input(KEY3_PIN): # button is released
        draw.ellipse((120,0,150,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((120,0,150,30), outline=255, fill=0) #A button filled
        print ("KEY3")


    if GPIO.input(KEY4_PIN): # button is released
        draw.ellipse((180,0,210,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((180,0,210,30), outline=255, fill=0) #A button filled
        print ("KEY4")
    disp.ShowImage(image,0,0)
# except:
	# print("except")
# GPIO.cleanup()
