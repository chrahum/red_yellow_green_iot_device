from gpiozero import LED
from time import sleep

led_Red = LED(18)
led_Green = LED(4)
led_Yellow = LED(12)
count = 0

while(count < 5):
    led_Red.on()
    sleep(2)
    led_Red.off()
    led_Green.on()
    sleep(3)
    led_Green.off()
    led_Yellow.on()
    sleep(1)
    led_Yellow.off()
    count += 1
