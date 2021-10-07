int white = 13;
int green = 12;
int blue = 11;
int red = 10;

void setup() {
  Serial.begin(9600);

  pinMode(white, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
}

void loop() {
  int inp = 0;
  if (Serial.available() > 0) {
    inp = Serial.read();
    // For W - Up
    if (inp == 119) {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      
      digitalWrite(white, HIGH);
    }
    // For S - Down
    if (inp == 115) {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(white, LOW);
      
      digitalWrite(green, HIGH);
    }
    // For A - Left
    if (inp == 97) {
      digitalWrite(red, LOW);
      digitalWrite(white, LOW);
      digitalWrite(green, LOW);
      
      digitalWrite(blue, HIGH);
    }
    // For D - Right
    if (inp == 100) {
      digitalWrite(white, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      
      digitalWrite(red, HIGH);
    }
  }
}
