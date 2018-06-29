<p align="center"><img width=15% src="https://github.com/RiLights/Nissan_skyline_eng_lcd/blob/master/eng_lcd.jpg"></p>

# Nissan Skyline English LCD
Programator to change language from Japanese to English for gauge cluster on Nissan Skyline. 

##### Requirements:
- Arduino
- EEPROM 93C66 library for Arduino (https://github.com/TauSolutions/M93Cx6)
- Python 2.7 or higher

#### How to use it
All function here specially focused to read/write 93c66 EEPROM from Nissan Skyline (Infiniti G) that is mean you don't have setup option so everything should be pretty simple :)

```
#Create reserve copy of your original EEPROM
read_dump.py -o original_dump.bin

#Write new dump
write_dump.py -i eng_dump.bin
```

Tested on Nissan Skyline 250GT FOUR 2007 year
But remember, you use this library at your own risk and responsibility.
