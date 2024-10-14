DFRobot_UVIndex240370Sensor
===========================

- [中文版](./README_CN.md)

A sensor that reads the intensity of ultraviolet light.

![产品效果图](../../resources/images/SEN0636.png)

## Product Link (https://www.dfrobot.com)

    SKU：SEN0636

## Table of Contents

  * [summary](#summary)
  * [installation](#installation)
  * [methods](#methods)
  * [compatibility](#compatibility)
  * [history](#history)
  * [credits](#credits)

## Summary

A sensor that reads the intensity of ultraviolet light.


## Installation

Download this library to Raspberry Pi before use, then open the routine folder. Type python demox.py on the command line to execute a routine demox.py. For example, to execute the read_data.py routine, you need to enter:

```python
python read_data.py
```

## Methods

```python
  def begin()
    '''!
      @brief Init UVIndex240370Sensor device
      @return Return value init status
    '''
  def read_UV_original_data()
    '''!
      @brief Read the UV voltage value
      @return voltage value (mV)
    '''

  def read_UV_index_data()
    '''!
      @brief Read the UV Index
      @return UV Index
    '''

  def read_risk_level_data()
    '''!
      @brief Read the risk level
      @return 0-4 (Low Risk,Moderate Risk,High Risk,Very High Risk,Extreme Risk)
    '''
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| Raspberry Pi2 |           |            |    √     |         |
| Raspberry Pi3 |           |            |    √     |         |
| Raspberry Pi4 |       √   |            |          |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |

## History

- 2024-10-11 - Version 1.0.0 released.

## Credits

Written by fary(feng.yang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))
