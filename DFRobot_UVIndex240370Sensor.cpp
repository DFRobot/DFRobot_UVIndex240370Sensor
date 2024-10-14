/*!
 * @file DFRobot_UVIndex240370Sensor.cpp
 * @brief This is the method implementation file of UVIndex240370Sensor
 * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [fary](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2022-05-17
 * @url https://github.com/DFRobor/DFRobot_UVIndex240370Sensor
 */

#include "DFRobot_UVIndex240370Sensor.h"


DFRobot_UVIndex240370Sensor::DFRobot_UVIndex240370Sensor(TwoWire *pWire)
{
  _pWire = pWire;
};

DFRobot_UVIndex240370Sensor::DFRobot_UVIndex240370Sensor(Stream *s):DFRobot_RTU(s)
{
  _s = s;
}

bool DFRobot_UVIndex240370Sensor::begin(void)
{
  setTimeoutTimeMs(200);
  bool ret = false;
  if(_pWire){
    _pWire->begin();
    _pWire->beginTransmission(_addr);
    if(_pWire->endTransmission() == 0){
      ret=true;
    }
  }else{
    uint8_t buffer[2];
    readReg(0x00,buffer,2);
    uint16_t data= (uint16_t)buffer[0]<<8|buffer[1];
    if(data == UVINDEX240370SENSOR_DEVICE_PID){
      ret=true;
    }
  }
  return ret;
}

uint16_t DFRobot_UVIndex240370Sensor::readUvOriginalData(void)
{
  uint8_t buffer[2];
  readReg(UVINDEX240370SENSOR_INPUTREG_UVS_DATA,buffer,2);
  uint16_t data= (uint16_t)buffer[0]<<8|buffer[1];
  return data;
}

uint16_t DFRobot_UVIndex240370Sensor::readUvIndexData(void)
{
  uint8_t buffer[2];
  readReg(UVINDEX240370SENSOR_INPUTREG_UVS_INDEX,buffer,2);
  uint16_t data= (uint16_t)buffer[0]<<8|buffer[1];
  return data;
}
uint16_t DFRobot_UVIndex240370Sensor::readRiskLevelData(void)
{
  uint8_t buffer[2];
  readReg(UVINDEX240370SENSOR_INPUTREG_RISK_LEVEL,buffer,2);
  uint16_t data= (uint16_t)buffer[0]<<8|buffer[1];
  return data;
}

uint8_t DFRobot_UVIndex240370Sensor::readReg(uint16_t reg, void *pBuf, uint8_t size)
{
  uint8_t* _pBuf = (uint8_t*)pBuf;
  uint8_t _reg  = 0;
    if(pBuf == NULL){
      DBG("data error");
      return 0;
    }
  if(_pWire){
    _pWire->beginTransmission(_addr);
    _pWire->write(reg);
    _pWire->endTransmission();
    _pWire->requestFrom(_addr, size);
    for(uint8_t i = 0; i < size; i++)
      _pBuf[i] = _pWire->read();
    for(uint8_t i = 0; i < size;){
      uint8_t temp = _pBuf[i];
      _pBuf[i] = _pBuf[i+1];
      _pBuf[i+1] = temp;
      i+=2;
    }
    return size;
  }else{
    return readInputRegister(_addr, reg, _pBuf, size);
  }
}

