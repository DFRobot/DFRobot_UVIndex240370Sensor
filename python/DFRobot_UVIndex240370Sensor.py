# -*- coding: utf-8 -*
'''!
  @file       DFRobot_UVIndex240370Sensor.py
  @brief       This is basic library of UVIndex240370Sensor sensor
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      fary(feng.yang@dfrobot.com)
  @version     V1.0
  @date        2024-10-11
  @url         https://github.com/DFRobor/DFRobot_UVIndex240370Sensor
'''

import serial
import time
import smbus
import os
import math
import RPi.GPIO as GPIO
import math

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

class DFRobot_UVIndex240370Sensor():
  I2C_MODE                  = 0x01
  UART_MODE                 = 0x02
  UVINDEX240370SENSOR_DEVICE_ADDR                            =0X23
  UVINDEX240370SENSOR_INPUTREG_UVS_DATA                      =0x06
  UVINDEX240370SENSOR_INPUTREG_UVS_INDEX                     =0x07
  UVINDEX240370SENSOR_INPUTREG_RISK_LEVEL                    =0x08
  UVINDEX240370SENSOR_DEVICE_PID                             =0x427c
  def __init__(self ,bus = 0 ,baud = 9600, mode = I2C_MODE):
    self.mode = 0
    self.resolution = 0
    self.gain = 0
    if mode == self.I2C_MODE:
      self._uart_i2c = self.I2C_MODE
      self.i2cbus = smbus.SMBus(bus)
    else:
      self._uart_i2c = self.UART_MODE
      self.master = modbus_rtu.RtuMaster(serial.Serial(port="/dev/ttyAMA0",baudrate=baud, bytesize=8, parity='N', stopbits=1))
      self.master.set_timeout(1.0)
      
  def begin(self):
    '''!
      @brief Init UVIndex240370Sensor device
      @return Return value init status
    '''
    ret=False
    if self._uart_i2c == self.I2C_MODE:
      buffer = self._read_reg(0x00,2)
      data = buffer[0]|buffer[1]<<8
    else:
      buffer = self._read_reg(0x00,1)
      data = buffer[0]
    if data == self.UVINDEX240370SENSOR_DEVICE_PID:
      ret =True
    return ret

  def read_UV_original_data(self):
    '''!
      @brief Read the UV voltage value
      @return voltage value (mV)
    '''
    if self._uart_i2c == self.I2C_MODE:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_UVS_DATA,2)
      data = buffer[0]|buffer[1]<<8
    else:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_UVS_DATA,1)
      data = buffer[0]
    return data

  def read_UV_index_data(self):
    '''!
      @brief Read the UV Index
      @return UV Index
    '''
    if self._uart_i2c == self.I2C_MODE:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_UVS_INDEX,2)
      data = buffer[0]|buffer[1]<<8
    else:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_UVS_INDEX,1)
      data = buffer[0]
    return data  


  def read_risk_level_data(self):
    '''!
      @brief Read the risk level
      @return 0-4 (Low Risk,Moderate Risk,High Risk,Very High Risk,Extreme Risk)
    '''
    if self._uart_i2c == self.I2C_MODE:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_RISK_LEVEL,2)
      data = buffer[0]|buffer[1]<<8
    else:
      buffer = self._read_reg(self.UVINDEX240370SENSOR_INPUTREG_RISK_LEVEL,1)
      data = buffer[0]
    return data

class DFRobot_UVIndex240370Sensor_I2C(DFRobot_UVIndex240370Sensor):
  '''!
    @brief An example of an i2c interface module
  '''
  def __init__(self ,bus):
    self._addr = self.UVINDEX240370SENSOR_DEVICE_ADDR
    super().__init__(bus,0,self.I2C_MODE)   
    
  
  def _read_reg(self, reg_addr ,length):
    '''!
      @brief read the data from the register
      @param reg_addr register address
      @param length read data
    '''
    self._reg = reg_addr
    rslt = self.i2cbus.read_i2c_block_data(self._addr ,self._reg , length)
    return rslt
       

class DFRobot_UVIndex240370Sensor_UART(DFRobot_UVIndex240370Sensor):
  '''!
    @brief An example of an UART interface module
  '''
  def __init__(self):
    self._baud = 9600
    self._addr = self.UVINDEX240370SENSOR_DEVICE_ADDR
    try:
      super().__init__(0,self._baud,self.UART_MODE)
    except:
      print ("plese get root!")
   
  
  def _read_reg(self, reg_addr ,length):
    '''!
      @brief Read data from the sensor
    '''
    return list(self.master.execute(self._addr, cst.READ_INPUT_REGISTERS, reg_addr, length))
  
