import gpiod
import time

LED_PIN = 17
BUTTON_PIN = 24
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

print("Starting main loop")

try:
    while True:
        button_state = button_line.get_value()
        print(f"Button state: {button_state}")
        if button_state == 1:
            print("Button pressed, executing tes_q()")
            # tes_q()
        else:
            led_line.set_value(0)
        time.sleep(0.1)  # Add a small delay to avoid overwhelming the CPU
finally:
    led_line.release()
    button_line.release()