# -*- coding: utf-8 -*
'''!
  @file  read_data.py
  @brief Run the routine to get UV intensity
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      fary(feng.yang@dfrobot.com)
  @version     V1.0
  @date        2024-10-11
  @url         https://github.com/DFRobor/DFRobot_UVIndex240370Sensor
'''
from __future__ import print_function
import sys
import os
sys.path.append("../")
import time
import RPi.GPIO as GPIO

from DFRobot_UVIndex240370Sensor import *

ctype=0
I2C_1= 0x01

if ctype==0:
  UVIndex240370Sensor = DFRobot_UVIndex240370Sensor_I2C(I2C_1)
else:
  UVIndex240370Sensor = DFRobot_UVIndex240370Sensor_UART()
def setup():
  while (UVIndex240370Sensor.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1) 

def loop():
  data = UVIndex240370Sensor.read_UV_original_data()     # Read the UV voltage value
  index = UVIndex240370Sensor.read_UV_index_data()   # Read the UV index,retuen 0-11
  level = UVIndex240370Sensor.read_risk_level_data() # Read the risk level,retren 0-4 (Low Risk,Moderate Risk,High Risk,Very High Risk,Extreme Risk)
  print("voltage: {} mV".format(data))
  print("index: {}".format(index))
  if level==0:
     print("risk_level:Low Risk")
  elif level==1:
    print("risk_level:Moderate Risk")
  elif level==2:
    print("risk_level:High Risk")
  elif level==3:
    print("risk_level:Very High Risk")
  elif level==4:
    print("risk_level:Extreme Risk")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
