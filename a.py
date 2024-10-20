import serial
import time

def send_signal_to_arduino():
    # Define the serial port and baud rate
    serial_port = 'COM4'  # Change 'COMX' to your Arduino's serial port
    baud_rate = 9600

        # Initialize the serial connection
    ser = serial.Serial(serial_port, baud_rate)
    print("Serial connection established")

        # Send a signal to start Arduino
    ser.write(b'Rice')
    print("Signal sent to Arduino")

        # Close the serial connection
    ser.close()



send_signal_to_arduino()