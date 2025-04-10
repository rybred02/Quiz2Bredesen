import time
from gpiozero import LED, Button, RGBLED


buttonRed = Button(17)  
buttonGreen = Button(27) 
buttonBlue = Button(22)  

red_led = LED(23)
green_led = LED(24)
blue_led = LED(25)

def ButtonsAndCombinations():

    if buttonRed.is_pressed:
        red_led.on()  
        print("Red button pressed! RGB LED is Red.")
    else:
        red_led.off()

    if buttonGreen.is_pressed:
        green_led.on() 
        print("Green button pressed! RGB LED is Green.")
    else:
        green_led.off()

    if buttonBlue.is_pressed:
        blue_led.on()   
        print("Blue button pressed! RGB LED is Blue.")
    else:
        blue_led.off()

while True:
    ButtonsAndCombinations()

    time.sleep(0.1)
