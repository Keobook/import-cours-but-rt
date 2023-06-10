#!/usr/bin/env python3

import json
import random

def generate_data(current_timestamp):
    global end_timestamp
    data = []

    temperature_data = {
        "type": "temperature",
        "description": "Temperature (in °C) in the current Banzaii",
        "timeline": []
    }

    humidity_data = {
        "type": "humidity",
        "description": "Humidity (in %) in the current Banzaii",
        "timeline": []
    }
    light_data = {
        "type": "light",
        "description": "Light (in lum) in the current Banzaii",
        "timeline": []
    }

    x = 0

    while current_timestamp <= end_timestamp:
        temperature = random.randint(18, 25)
        humidity = random.randint(40, 60)
        light = random.randint(100, 1000)

        temperature_data['timeline'].append(generate_timeline_elements(temperature, current_timestamp))
        humidity_data['timeline'].append(generate_timeline_elements(humidity, current_timestamp))
        light_data['timeline'].append(generate_timeline_elements(light, current_timestamp))

        x += 1
        current_timestamp += time_interval
        print(f"[GenerateData]: x = {x}, Condition: {current_timestamp <= end_timestamp}")

    data.append(temperature_data)
    data.append(humidity_data)
    data.append(light_data)

    save_to_json(data)

    return data

def generate_timeline_elements(value, timestamp):
    timeline_element = {
        "value": str(value),
        "timestamp": str(timestamp)
    }
    return timeline_element

def generate_sql_commands(data):
    commands = []

    print(data)

    for item in data:
        path = "/database/external/data.json"
        start_timestamp = 113131612161
        timestamp = item['timeline'][0]["timestamp"]

        command = f"INSERT INTO external_data (path,created,last_modified ) VALUES ('{path}', '{start_timestamp}', '{timestamp}');"
        commands.append(command)

    save_to_sql(commands)

    return commands

def save_to_sql(commands):
    with open("sql_commands.txt", "w") as file:
        for command in commands:
            file.write(command + "\n")

def save_to_json(data):
    json_data = {
        "id": "001",
        "data": data
    }

    with open("data.json", "w") as file:
        json.dump(json_data, file, indent=4)


start_timestamp = 113131612161
end_timestamp = 113131612587
time_interval = 5

print(start_timestamp < end_timestamp)
print(start_timestamp + 90*time_interval < end_timestamp)

try:
    generated_data = generate_data(start_timestamp)
    sql_commands = generate_sql_commands(generated_data)

    # # save_to_json(generated_data)
    # save_to_sql(sql_commands)

except KeyboardInterrupt:
    print("Programme arrêté")

# 
