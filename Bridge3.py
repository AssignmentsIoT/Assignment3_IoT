"""
/*******************************************************************************
 * Copyright (c) 2011, 2013 IBM Corp.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v1.0 which accompany this distribution. 
 *
 * The Eclipse Public License is available at 
 *    http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at 
 *   http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * Contributors:
 *    Ian Craggs - initial API and implementation and/or initial documentation
 *******************************************************************************/
"""

import os
import json
import time 
import random
from datetime import datetime
import paho.mqtt.client as paho

# Settings to connect to ThingsBoard devices YOUR_ACCESS_TOKEN

# Devices' access tokens 
ACCESS_TOKEN_TEMPERATURE_ES_1 = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_TEMPERATURE_ES_2 = 'YOUR_ACCESS_TOKEN'

ACCESS_TOKEN_HUMIDITY_ES_1 = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_HUMIDITY_ES_2 = 'YOUR_ACCESS_TOKEN'

ACCESS_TOKEN_WIND_DIRECTION_ES_1 = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_WIND_DIRECTION_ES_2 = 'YOUR_ACCESS_TOKEN'

ACCESS_TOKEN_WIND_INTENSITY_ES_1 = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_WIND_INTENSITY_ES_2 = 'YOUR_ACCESS_TOKEN'

ACCESS_TOKEN_RAIN_HEIGHT_ES_1 = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_RAIN_HEIGHT_ES_2 = 'YOUR_ACCESS_TOKEN'

# Connect to ThingsBoard
THINGSBOARD_HOST = "demo.thingsboard.io"
THINGSBOARD_PORT = 1883
THINGSBOARD_TOPIC = "v1/devices/me/telemetry"

# Settings to connect to The Things Network devices
THETHINGSNETWORK_HOST = "eu.thethings.network"
THETHINGSNETWORK_PORT = 1883

THETHINGSNETWORK_TOPIC = "+/devices/+/up"
THETHINGSNETWORK_USER = "es-simulator"
THETHINGSNETWORK_ACCESS_KEY = "YOUR_APP_ACCESS_KEY"

THETHINGSNETWORK_ES_1 = "es-1"
THETHINGSNETWORK_ES_2 = "es-2"

# Variables to collect data
data_ES_1 = ""
data_ES_2 = ""

tmp_ES_1 = ""
hum_ES_1 = ""
w_dir_ES_1 = ""
w_int_ES_1 = ""
rn_hgt_ES_1 = ""

tmp_ES_2 = ""
hum_ES_2 = ""
w_dir_ES_2 = ""
w_int_ES_2 = ""
rn_hgt_ES_2 = ""

# Define necessary functions

# on_connect callback for ThingsBoard
def connected_thingsboard():
    print ("Connected to ThingsBoard device")
    pass

# on_publish callback for ThigsBoard
def data_published(client, userdata, result):
    print ("Data successfully published on ThingsBoard\n")
    pass

# on_connect callback for The Things Network
def on_connect(client, userdata, flags, rc):
    print("Connected to The Things Network with result code "+ str(rc) + "\n")

   # Subscribe, so that if the connection is lost when it's recovered our client will automatically subscribe again
    client.subscribe(THETHINGSNETWORK_TOPIC)

# on_message callback for The Things Network
def on_message(client, userdata, msg):

    # Get message from TTN 
    json_payload = json.loads(msg.payload)
    json_fields = json_payload['payload_fields']

    if (json_payload['dev_id'] == THETHINGSNETWORK_ES_1): 
        data_ES_1 = json_fields['string']

        # Message processing 
        print(data_ES_1+"\nStart processing...\n")
        data_ES_1_list = data_ES_1.split(";")

        # Making the variables visible
        global tmp_ES_1
        global hum_ES_1
        global w_dir_ES_1
        global w_int_ES_1
        global rn_hgt_ES_1

        # Putting the information in the right format
        tmp_ES_1 = "{Value: " + data_ES_1_list[0] + "}"
        hum_ES_1 = "{Value: " + data_ES_1_list[1] + "}"
        w_dir_ES_1 = "{Value: " + data_ES_1_list[2] + "}"
        w_int_ES_1 = "{Value: " + data_ES_1_list[3] + "}"
        rn_hgt_ES_1 = "{Value: " + data_ES_1_list[4] + "}"

        # Debug
        print("tmp_ES_1 = " + tmp_ES_1 
            + "\nhum_ES_1 = " + hum_ES_1
            + "\nw_dir_ES_1 = " + w_dir_ES_1
            + "\nw_int_ES_1 = " + w_int_ES_1
            + "\nrn_hgt_ES_1 = " + rn_hgt_ES_1)

    elif (json_payload['dev_id'] == THETHINGSNETWORK_ES_2):
        data_ES_2 = json_fields['string']

        # Message processing 
        print(data_ES_2+"\nStart processing...\n")
        data_ES_2_list = data_ES_2.split(";")

        # Making the variables visible
        global tmp_ES_2
        global hum_ES_2
        global w_dir_ES_2
        global w_int_ES_2
        global rn_hgt_ES_2

        # Putting the information in the right format
        tmp_ES_2 = "{Value: " + data_ES_2_list[0] + "}"
        hum_ES_2 = "{Value: " + data_ES_2_list[1] + "}"
        w_dir_ES_2 = "{Value: " + data_ES_2_list[2] + "}"
        w_int_ES_2 = "{Value: " + data_ES_2_list[3] + "}"
        rn_hgt_ES_2 = "{Value: " + data_ES_2_list[4] + "}"

        # Debug
        print("tmp_ES_2 = " + tmp_ES_2 
            + "\nhum_ES_2 = " + hum_ES_2
            + "\nw_dir_ES_2 = " + w_dir_ES_2
            + "\nw_int_ES_2 = " + w_int_ES_2
            + "\nrn_hgt_ES_2 = " + rn_hgt_ES_2)




#Connect client functions
def connect_thingsboard_client(client_name, device_accesstoken):
  TS_client = paho.Client(client_name)
  TS_client.on_connect = connected_thingsboard()
  TS_client.on_publish = data_published
  TS_client.username_pw_set(device_accesstoken)
  TS_client.connect(THINGSBOARD_HOST, THINGSBOARD_PORT, keepalive=60)
  return TS_client

def connect_thethingsnetwork_client(client_name, access_key):
  TTN_client = paho.Client(client_name)
  TTN_client.on_connect = on_connect
  TTN_client.on_message = on_message
  TTN_client.username_pw_set(THETHINGSNETWORK_USER, password=access_key)
  TTN_client.connect(THETHINGSNETWORK_HOST, THETHINGSNETWORK_PORT, keepalive=60)
  return TTN_client

# Connect to ThingsBoard's devices
client_temperature_1 = connect_thingsboard_client("Temperature Device ES-1", ACCESS_TOKEN_TEMPERATURE_ES_1)
client_temperature_2 = connect_thingsboard_client("Temperature Device ES-2", ACCESS_TOKEN_TEMPERATURE_ES_2)

client_humidity_1 = connect_thingsboard_client("Humidity Device ES-1", ACCESS_TOKEN_HUMIDITY_ES_1)
client_humidity_2 = connect_thingsboard_client("Humidity Device ES-2", ACCESS_TOKEN_HUMIDITY_ES_2)

client_wind_direction_1 = connect_thingsboard_client("Wind Direction Device ES-1", ACCESS_TOKEN_WIND_DIRECTION_ES_1)
client_wind_direction_2 = connect_thingsboard_client("Wind Direction Device ES-2", ACCESS_TOKEN_WIND_DIRECTION_ES_2)

client_wind_intensity_1 = connect_thingsboard_client("Wind Intensity Device ES-1", ACCESS_TOKEN_WIND_INTENSITY_ES_1)
client_wind_intensity_2 = connect_thingsboard_client("Wind Intensity Device ES-2", ACCESS_TOKEN_WIND_INTENSITY_ES_2)

client_rain_height_1 = connect_thingsboard_client("Rain Heigth Device ES-1", ACCESS_TOKEN_RAIN_HEIGHT_ES_1)
client_rain_height_2 = connect_thingsboard_client("Rain Height Device ES-2", ACCESS_TOKEN_RAIN_HEIGHT_ES_2)

# Connect to The Things Network
client_ttn = connect_thethingsnetwork_client("ES Simulator", THETHINGSNETWORK_ACCESS_KEY)

# Start client threads
client_temperature_1.loop_start()
client_temperature_2.loop_start()

client_humidity_1.loop_start()
client_humidity_2.loop_start()

client_wind_direction_1.loop_start()
client_wind_direction_2.loop_start()

client_wind_intensity_1.loop_start()
client_wind_intensity_2.loop_start()

client_rain_height_1.loop_start()
client_rain_height_2.loop_start()

client_ttn.loop_start()

while(True):
    
    # Wait until new data
    while(tmp_ES_1 == "" or hum_ES_1 == "" or w_dir_ES_1 == "" or w_int_ES_1 == "" or rn_hgt_ES_1 == ""
          or tmp_ES_2 == "" or hum_ES_2 == "" or w_dir_ES_2 == "" or w_int_ES_2 == "" or rn_hgt_ES_2 == ""):
        pass
    
    # Publish data on ThingsBoard
    client_temperature_1.publish(THINGSBOARD_TOPIC, tmp_ES_1)
    client_temperature_2.publish(THINGSBOARD_TOPIC, tmp_ES_2)

    client_humidity_1.publish(THINGSBOARD_TOPIC, hum_ES_1)
    client_humidity_2.publish(THINGSBOARD_TOPIC, hum_ES_2)

    client_wind_direction_1.publish(THINGSBOARD_TOPIC, w_dir_ES_1)
    client_wind_direction_2.publish(THINGSBOARD_TOPIC, w_dir_ES_2)

    client_wind_intensity_1.publish(THINGSBOARD_TOPIC, w_int_ES_1)
    client_wind_intensity_2.publish(THINGSBOARD_TOPIC, w_int_ES_2)

    client_rain_height_1.publish(THINGSBOARD_TOPIC, rn_hgt_ES_1)
    client_rain_height_2.publish(THINGSBOARD_TOPIC, rn_hgt_ES_2)

    # Empty variables of old data
    tmp_ES_1 = ""
    hum_ES_1 = ""
    w_dir_ES_1 = ""
    w_int_ES_1 = ""
    rn_hgt_ES_1 = ""

    tmp_ES_2 = ""
    hum_ES_2 = ""
    w_dir_ES_2 = ""
    w_int_ES_2 = ""
    rn_hgt_ES_2 = ""