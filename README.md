# MQTT Subscriber and Sender Example

Here's an example for MQTT subscriber and sender.

## Introduction

The MQTT protocol is very simple, which is very suitable for IoT devices with limited processor resources and limited network bandwidth.

## Requirements

- paho-mqtt

## Usage

First, make a subscriber.

You can change the topics and MQTT server address(a.k.a MQTT Broker) in the program.

The default is official server `test.mosquitto.org` with default port `1883`.

```bash
python3 example_subscriber.py
```

And, we can try sender(a.k.a publisher) to send messages. 

The messages can be any format like `JSON`, `list`, `Numpy Array` and so on cause `Sender` will change the data you send to be **binary object** in the backend by using pickle package. 

When the message is sent, all users with subscription related items can receive the message.


```bash
python3 example_sender.py
```

## Result

* Subscriber

```
Connected with result code 0
yee {'test1': 1234, 'test2': 'yee'}
yoo 1234
yoo b'ABCDEFG'
yoo ['1', 'a', 'b']
```
