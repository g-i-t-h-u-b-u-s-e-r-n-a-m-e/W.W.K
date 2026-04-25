void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
}

void loop() {
    if (digitalRead(10) == LOW){
      digitalWrite(8, HIGH); 
    } else {
      digitalWrite(8, LOW);
    }
    if (digitalRead(3) == LOW){
      digitalWrite(9, HIGH);
    } else {
      digitalWrite(9, LOW);
    }
}