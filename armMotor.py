import pigpio
import time

pi = pigpio.pi()
servo_pin = 16  # GPIO pin connected to the servo signal

def set_angle(angle):
    if angle < 0 or angle > 180:
        raise ValueError("Angle must be between 0 and 180 degrees")
    # Convert angle to pulse width (500µs to 2500µs)
    pulsewidth = (angle / 180.0 * 2000) + 500
    pi.set_servo_pulsewidth(servo_pin, pulsewidth)

set_angle(60)    # Move to 0 degrees
time.sleep(2)
set_angle(0) 
time.sleep(2)

pi.set_servo_pulsewidth(servo_pin, 0)  # Stop the servo
pi.stop()