DFRobot_UVIndex240370Sensor
===========================

* [中文版](./README_CN.md)

A sensor that reads the intensity of ultraviolet light.

![产品效果图片](../../resources/images/SEN0636.png)
  
## Product Link (https://www.dfrobot.com)
    SKU: SEN0636

## Table of Contents

  * [Summary](#summary)
  * [Installation](#installation)
  * [Methods](#methods)
  * [Compatibility](#compatibility)
  * [History](#history)
  * [Credits](#credits)

## Summary

A sensor that reads the intensity of ultraviolet light.

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
  /**
   * @fn begin
   * @brief Init UVIndex240370Sensor device
   * @return Return value init status
   * @retval ture  Succeed
   * @retval false Failed
   */
  int8_t begin(void);

  /**
   * @fn readUvOriginalData
   * @brief Read the UV voltage value
   * @return voltage value (mV)
   */
  uint16_t readUvOriginalData(void);

  /**
   * @fn readUvIndexData
   * @brief Read the UV Index
   * @return UV Index
   */
  uint16_t readUvIndexData(void);

  /**
   * @fn readRiskLevelData
   * @brief Read the risk level
   * @return 0-4 (Low Risk,Moderate Risk,High Risk,Very High Risk,Extreme Risk)
   */
  uint16_t readRiskLevelData(void);

```

## Compatibility

MCU                | SoftwareSerial | HardwareSerial |      IIC      |
------------------ | :----------: | :----------: | :----------: | 
Arduino Uno        |      √       |      X       |      √       |
Mega2560           |      √       |      √       |      √       |
Leonardo           |      √       |      √       |      √       |
ESP32              |      X       |      √       |      √       |
ESP8266            |      √       |      X       |      √       |
micro:bit          |      X       |      X       |      √       |
FireBeetle M0      |      X       |      √       |      √       |
Raspberry Pi       |      X       |      √       |      √       |

## History

- 2024-10-11 - Version 1.0.0 released.

## Credits

Written by fary(feng.yang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))
