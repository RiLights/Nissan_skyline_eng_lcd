#include <M93Cx6.h>

#define PWR_PIN   7
#define CS_PIN    10
#define SK_PIN    13
#define DO_PIN    12
#define DI_PIN    11
#define ORG_PIN   8
#define ORG       16
#define CHIP      66

M93Cx6 eeprom = M93Cx6(PWR_PIN, CS_PIN, SK_PIN, DO_PIN, DI_PIN, ORG_PIN);


char state;

void setup() {
  eeprom.setChip(66);
  eeprom.setOrg(ORG_16);
  eeprom.setCheckStatus(1);
  
  Serial.begin ( 9600 );
  Serial.println("Ready");
}

void loop ()
{
  if(Serial.available()){ // only send data back if data has been sent

    state = Serial.read();
    switch ( state )
    {
      case -1:
        break;
      case 't':
        Serial.println ( "test" );
        break;
      case 'r':
        for (size_t i = 0; i < 256; i++) {
          uint16_t val;
          delay(50);
          val = eeprom.read(i);
          Serial.println(val);
        }
        Serial.println("Done");
        break;
      case 'w':
        delay(50);
        
        eeprom.writeEnable();

        for(uint16_t i=0; i<256; i++){
          uint8_t val1, val2;
          delay(50);
          if (Serial.available()>=2){
            val1=Serial.read();
            val2=Serial.read();
            uint16_t val= get16(val1,val2);
            eeprom.write(i, val);
            Serial.println( val,HEX);
          }
        }

        Serial.println("Done");
        break;
    }
  }
  
}
unsigned int get16(uint8_t val1,uint8_t val2){
  return val1 + (val2 << 8);  // convert two 8-bit to one 16-bit int type
}
  

