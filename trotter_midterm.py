"""
==== Alexandra Trotter
==== MAE Department, SEAS GWU
==== Description
======== This program uses the vibration sensor to send an email if a vibration is detected.
"""

# IMPORT MODULES ====================================================

import RPi.GPIO as GPIO
import time
import yagmail

# =====================================================================

# INTIALIZE GPIO-PINS =================================================
# Declare the channels for each device

VIB = 15 #Vibration receiver
RedLED = 12 #Red LED
GreenLED = 11 #Green LED

# =====================================================================

# INTIALIZE VARIABLES =================================================

timeElapsed = 0
vibration = False 
        
# =====================================================================


# DEFINE FUNCTIONS ====================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set up GPIO mode and define input and output pins

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(VIB, GPIO.IN)
    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.setup(GreenLED, GPIO.OUT)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               

def loop():
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        
        time.sleep(30)
        
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        vibration = False
        
        while not vibration:
            # Turns the LED to red if the sensor vibrates, then sends an email. 
            
            if(GPIO.input(VIB) == True):
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                print('red')
                vibration = True
                email()
                
            time.sleep(0.1)
                
                
def email():
    yag_mail = yagmail.SMTP(user='raspberryp019@gmail.com', password="yhka ptvp fmas dsmi", host='smtp.gmail.com')
  
    To= "alex.trotter@gmail.com" # Use temp-mail.org for testing this code
    Subject = "Mouse trap activated"
    Body = """
            Your mouse trap may have been tripped.  
            """
     
    yag_mail.send(to=To, subject=Subject, contents=Body)
    print("Email has been sent successfully to the receiver's address.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
# CLEAR GPIO CHANNELS, STOP Buzzer and close CSV FILEs

def destroy():
    GPIO.cleanup()

# ====================================================================
# MAIN FUNCTION to RUN PROGRAM  ======================================

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Quits out on ctrl+c
        destroy()
    finally:
        destroy()
# ====================================================================


