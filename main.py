from threading import Thread
#import RPi.GPIO as GPIO
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_rfid_reader as reader
from hal import hal_servo as servo
from hal import hal_rfid_reader as RFID
from hal import hal_adc as ldr
from hal import hal_buzzer as buzzer
from hal import hal_led as led
import payment as PAYMENT
import time
from time import sleep

# Buy food and drinks  /

#Initialize
lcd = LCD.lcd()
lcd.lcd_clear()
servo.init()
reader = RFID.init()
ldr.init()
buzzer.init()
led.init()


key1=[1] # sprite
key2=[2] # coke
key3=[3]# coconut
key4=[4]# watermelon juice
key0 = [0] #QRCODE
password = [7,8,9]
passwordlist = []

check_key = []
global input
#outstandning_fee=days_expired*0.75?
outstanding_fee=0

def readrfid():
    id = reader.read_id_no_block()
    if id != 0:
        lcd.lcd_display_string("Outstanding Fee paid",1)



def key_press(key):
    check_key = []
    check_key.append(key)

    if check_key == key1:
        lcd.lcd_clear()
        lcd.lcd_display_string("Sprite", 1)
        lcd.lcd_display_string("$1.50", 2)
        time.sleep(2)
        PAYMENT.main()

    elif check_key == key2:
        lcd.lcd_clear()
        lcd.lcd_display_string("Coke", 1)
        lcd.lcd_display_string("$2.00", 2)
        time.sleep(2)
        PAYMENT.main()

    elif check_key == key3:
        lcd.lcd_clear()
        lcd.lcd_display_string("Coconut", 1)
        lcd.lcd_display_string("$1.80", 2)
        time.sleep(2)
        PAYMENT.main()

    elif check_key == key4:
        lcd.lcd_clear()
        lcd.lcd_display_string("Watermelon Juice", 1)
        lcd.lcd_display_string("$1.50", 2)
        time.sleep(2)
        PAYMENT.main()


    elif check_key == key0:
        lcd.lcd_clear()
        lcd.lcd_display_string("Dispensing.....", 1)
        PAYMENT.motor()
        return main()


    passwordlist.append(key)
    print(passwordlist)
    if passwordlist == password:
        lcd.lcd_clear()
        lcd.lcd_display_string("Access Granted", 1)
        buzzer.short_beep(0)
        servo.set_servo_position(90)
        time.sleep(2)
        servo.set_servo_position(1)
        time.sleep(1)
        return main()

def main():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Select Item Or", 1)
    lcd.lcd_display_string("Scan QR code", 2)

    while True:
        adc = ldr.get_adc_value(0)
        print(adc)
        if adc > 650:
            buzzer.short_beep(1)
        else:
            buzzer.short_beep(0)
            keypad.init(key_press)
            keypad.get_key()
            return main()

    while True:

        id = reader.read_id_no_block()
        id = str(id)

        if id != "None":
            print("RFID card ID = " + id)



 # Main entry point
if __name__ == "__main__":
    main()
