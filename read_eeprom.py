import struct
import sys
import argparse

from sky_setup import logging,serial_port

parser = argparse.ArgumentParser()
parser.add_argument ("-o", "--output", dest='output_dump', default='temp_eeprom.bin', type=str);
args = parser.parse_args()

if args.output_dump:
    logging.info('State - {}...'.format(serial_port.readline()))
    serial_port.write('r')

    mass=[]
    for i in range(0,256):
        temp_byte = serial_port.readline()
        temp_byte = int(temp_byte)
        mass.append(temp_byte)
        logging.debug('Byte: {}'.format(hex((temp_byte))))

    logging.info('State - {}'.format(serial_port.readline()))
    serial_port.close()

    #--write to binary file
    mass_flat = ''
    output_dump = args.output_dump
    for i in mass:
        mass_flat+=struct.pack("H",i)

    with open(output_dump, "w") as file:
        file.write(mass_flat)