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

要使用这个库，首先将库下载到Raspberry Pi，然后打开例程文件夹。要执行一个例程demox.py，请在命令行中输入python demox.py。例如，要执行read_data.py例程，你需要输入:

```python
python read_data.py
```



## 方法

```python
  def begin()
     '''!
      @brief 初始化 UVIndex240370Sensor 设备,
      @return 返回值初始化状态
    '''   
  def read_UV_original_data()
    '''!
      @brief 读取紫外线电压值
      @return 电压值 (单位：mV)
    '''

  def read_UV_index_data()
    '''!
      @brief 读取紫外线指数
      @return 紫外线指数（0-11）
    '''

  def read_risk_level_data()
    '''!
      @brief 读取风险等级
      @return 0-4 (低风险，中风险，高风险，很高风险，极高风险)
    '''
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |     √    |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |

## History

- 2022-10-11 - 1.0.0 版本

## Credits

Written by fary(feng.yang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))