import time
from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_rfid_reader as rfid_reader
from hal import hal_dc_motor as dc_motor
import main as main1
dc_motor.init()
def motor():
    dc_motor.set_motor_speed(50)
    print("DC MOTOR ON")
    time.sleep(1)
    dc_motor.set_motor_speed(0)
    print("DC MOTOR OFF")
    return main1.main()
def main():
    # Get lcd instance
    lcd = LCD.lcd()

    # initialize LED HAL driver
    led.init()

    lcd.backlight(1)
    lcd.lcd_clear()

    # Display message on LCD
    lcd.lcd_display_string("Tap cards", 1)


    # Turn off LED
    led.set_output(0, 0);

    # Initialize RFID card reader
    reader = rfid_reader.init()

    # Infinite loop to scan for RFID cards
    while True:
        id = reader.read_id_no_block()
        id = str(id) #369693405083

        if id != "None":
            time.sleep(3)
            print("RFID card ID = " + id)
            # Display RFID card ID on LCD line 2
            lcd.lcd_display_string("PAYMENT COMPLETE", 2)
            time.sleep(2)
            dc_motor.set_motor_speed(50)
            print ("DC MOTOR ON")
            time.sleep(1)
            dc_motor.set_motor_speed(0)
            print("DC MOTOR OFF")
            return main1.main()



        # Main entry point

if __name__ == "__main__":
    main()
