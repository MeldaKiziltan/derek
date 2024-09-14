import serial
import time

# Set up serial connections for both LACs
lac1 = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # First LAC
lac2 = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)  # Second LAC

def send_command(ser, command):
    ser.write(command.encode())
    time.sleep(0.1)
    response = ser.readline().decode('utf-8').strip()
    return response

# Example: Move first actuator to 50% position
command1 = 'P5000\r'  # Adjust as per your actuator
response1 = send_command(lac1, command1)
print(f'LAC1 Response: {response1}')

# Example: Move second actuator to 75% position
command2 = 'P7500\r'
response2 = send_command(lac2, command2)
print(f'LAC2 Response: {response2}')

lac1.close()
lac2.close()
