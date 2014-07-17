
int ledRed = 13;      // LED
int button_pin = 2;
int button_state = 0;
boolean pressed = false;

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  pinMode(ledRed, OUTPUT); 
  pinMode(button_pin, INPUT);  
}

void loop(){
  button_state = digitalRead(button_pin);
  if (button_state == LOW) {
    if (pressed == false) {
      Serial.write("x");  
      pressed = true;
      delay(50);
    }
  } else
    pressed = false;
}
