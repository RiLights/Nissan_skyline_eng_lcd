import sys
import argparse

from sky_setup import logging,serial_port

parser = argparse.ArgumentParser()
parser.add_argument ("-i", "--input", dest='input_dump', default='temp_eeprom.bin', type=str);
args = parser.parse_args()

if args.input_dump:
    bytedata=[]
    input_dump = args.input_dump
    with open(input_dump, "rb") as f:
        byte = f.read(2)
        while byte != "":
            # Do stuff with byte.
            if byte:
                bytedata.append(byte)

            byte = f.read(2)

    serial_port.write('w')
    logging.info('State - {}'.format(serial_port.readline()))

    serial_port.write('w')
    for i in bytedata:
        serial_port.write(i)
        logging.debug('Byte: {}'.format(serial_port.readline()))
    logging.info('State - {}'.format(serial_port.readline()))
    serial_port.close()
