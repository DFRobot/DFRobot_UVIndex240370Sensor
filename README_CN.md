DFRobot_UVIndex240370Sensor
===========================

* [English Version](./README.md)

一个读取紫外线强度的传感器。

![产品效果图片](../../resources/images/SEN0636.png)

## 产品链接（https://www.dfrobot.com）

    SKU：SEN0636
  
## 目录

  * [概述](#概述)
  * [库安装](#库安装)
  * [方法](#方法)
  * [兼容性](#兼容性)
  * [历史](#历史)
  * [创作者](#创作者)

## 概述

一个读取紫外线强度的传感器。

## 库安装

使用此库前，请首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开examples文件夹并在该文件夹中运行演示。

## 方法

```C++
  /**
   * @fn begin
   * @brief 初始化传感器
   * @return 初始化结果
   * @retval true  成功
   * @retval false 失败
   */
  int8_t begin(void);

  /**
   * @fn readUvOriginalData
   * @brief 读取紫外线电压值
   * @return 电压值 (单位：mV)
   */
  uint16_t readUvOriginalData(void);

  /**
   * @fn readUvIndexData
   * @brief 读取紫外线指数
   * @return 紫外线指数（0-11）
   */
  uint16_t readUvIndexData(void);

  /**
   * @fn readRiskLevelData
   * @brief 读取风险等级
   * @return 0-4 (低风险，中风险，高风险，很高风险，极高风险)
   */
  uint16_t readRiskLevelData(void);

```


## 兼容性

MCU                | SoftwareSerial | HardwareSerial |      IIC      |
------------------ | :----------: | :----------: | :----------: | 
Arduino Uno        |      √       |      X       |      √       |
Mega2560           |      √       |      √       |      √       |
Leonardo           |      √       |      √       |      √       |
ESP32              |      X       |      √       |      √       |
ESP8266            |      √       |      X       |      √       |
micro:bit          |      X       |      X       |      √       |
FireBeetle M0      |      X       |      √       |      X        |
raspberry          |      X       |      √       |      √       |

## 历史
- 2024-10-11 - 1.0.0 版本

## 创作者

Written by fary(feng.yang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))