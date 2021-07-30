import spidev as SPI
import ST7789
import time

from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

# 240x240 display with hardware SPI:
lcd = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
lcd.Init()

# Clear display.
lcd.clear()

# Create blank image for drawing.
image1 = Image.new("RGB", (lcd.width, lcd.height), "WHITE")
draw = ImageDraw.Draw(image1)
font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 22)


draw.text((70, 70), 'Hello World ! ', font=font1, fill = "BLUE")
draw.text((40, 100), 'SB-Components ', font=font2, fill = "Red")

lcd.ShowImage(image1,0,0)
time.sleep(3)

image = Image.open('testimage.jpg')	
lcd.ShowImage(image,0,0)
