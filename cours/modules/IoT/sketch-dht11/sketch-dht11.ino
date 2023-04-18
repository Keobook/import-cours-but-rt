#include "DHT.h"
#include <painlessMesh.h>
#include "namedMesh.h"

#define   MESH_SSID       "rtbzrtbz"
#define   MESH_PASSWORD   "rtbziom1"
#define   MESH_PORT       5555

Scheduler     userScheduler; // to control your personal task
namedMesh     mesh;

String nodeName = "CentaurusNode"; // Name needs to be unique


void sendMessage() ; // Prototype
// Task to blink the number of nodes
Task blinkNoNodes;
bool onFlag = false;

// DHT setup
DHT dht(25, DHT11);

// One second interval
Task taskSendBroadcastMessage(TASK_SECOND*30, TASK_FOREVER, [](){
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  String message = String("{\"node\":\"") + nodeName + String("\", \"hum\":\"") + String(humidity) + String("\", \"temp\":\"") + String(temperature) + String("\"}");

  mesh.sendBroadcast(message, true);
});


void setup() {

  // start DHT
  dht.begin();
  // Start Serial Output
  Serial.begin(115200);

  mesh.setDebugMsgTypes(ERROR | DEBUG | CONNECTION);  // set before init() so that you can see startup messages

  mesh.init(MESH_SSID, MESH_PASSWORD, &userScheduler, MESH_PORT);

  mesh.setName(nodeName); // This needs to be an unique name! 

  mesh.onReceive([](uint32_t from, String &msg) {
    Serial.printf("Received message by id from: %u, %s\n", from, msg.c_str());
  });

  mesh.onReceive([](String &from, String &msg) {
    Serial.printf("Received message by name from: %s, %s\n", from.c_str(), msg.c_str());
  });

  mesh.onChangedConnections([]() {
    Serial.printf("Changed connection\n");
  });

  userScheduler.addTask(taskSendBroadcastMessage);
  taskSendBroadcastMessage.enable();
}

void loop() {
  // Serial.print("Humidity: ");
  // Serial.println(humidity);
  // Serial.print("Temperature: ");
  // Serial.println(temperature);

  // Update our mesh
  mesh.update();
  // // Sleep for 500 ms
  // delay(500);
}