<p align="center"><img width=15% src="https://github.com/RiLights/Nissan_skyline_eng_lcd/blob/master/eng_lcd.jpg"></p>

# Nissan Skyline English LCD
Nissan Skyline Japanese to English conversion.                             
Programator to change language from Japanese to English for gauge cluster on Nissan Skyline. 

##### Requirements:
- Arduino
- EEPROM 93C66 library for Arduino (https://github.com/TauSolutions/M93Cx6)
- Python 2.7 or higher

#### How to use it
All function here specially focused to read/write 93c66 EEPROM from Nissan Skyline (Infiniti G) that is mean you don't have setup option so everything should be pretty simple :)

sky_setup.py - Initial setup where you have to provide port and serial speed to your arduino (arduino/sky_pro.ini - speed also can be configured from arduino side). 

```
#Create copy of your original EEPROM (for any case)
read_eeprom.py -o original_sky_dump.bin

#Write new dump
write_eeprom.py -i dump/eng_sky_dump.bin
```

##### Tested on:
- Nissan Skyline 250GT FOUR 2007 year
>But remember, you use this library at your own risk and responsibility
