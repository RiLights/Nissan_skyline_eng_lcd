import serial
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)

serial_port = serial.Serial('/dev/cu.wchusbserial1410', 9600)
