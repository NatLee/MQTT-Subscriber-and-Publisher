"""
MQTT Subscriber
"""

import paho.mqtt.client as mqtt

class MqttSubscriber():
    """
    MQTT Subscriber

    ...

    Attributes
    ----------
        host: str
            the mqtt server host
        topic: list
            your subscribe list

    """
    def __init__(self, host, topics, port=1883):
        self.host = host # MQTT server address
        self.topics = topics # subscribe topics
        self.client = mqtt.Client() # make a Clinet to subscribe
        self.client.on_connect = self.on_connect # connect MQTT Server
        self.client.on_message = self.on_message # define the method of processing the message you get

        self.client.connect(host, port, 60) # Link start!

    def on_connect(self, client, userdata, flags, rc):
        '''The callback for when the client receives a CONNACK response from the server.'''
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        for topic in self.topics:
            client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        '''The callback for when a PUBLISH message is received from the server.'''

        # here you can process the message you get
        print(msg.topic + " " + str(msg.payload))
