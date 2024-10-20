from django.shortcuts import render
import serial
import time
from django.http import HttpResponse

def sensor_data(request):
    # Replace 'COM6' with your Arduino's serial port
    serial_port = 'COM4'
    baud_rate = 9600

    try:
        # Establish serial connection
        ser = serial.Serial(serial_port, baud_rate)

        # Read data from Arduino
        data = ser.readline().decode('latin-1').strip()

        # Close serial connection
        ser.close()

        # Pass the data to the template
        return render(request, 'sensor_val.html', {'data': data})
    except serial.SerialException:
        # Handle serial port error
        return HttpResponse("Error: Serial port not available or accessible.")
