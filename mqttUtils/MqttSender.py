"""
Example for sending messages to mqtt server

"""

import json
import paho.mqtt.publish as publish

class MqttSender():
    """MQTT Sender with topic

    ...

    Attributes
    ----------
        topic: str
            your subscribe
        hostname: str
            the mqtt server host

    Methods
    ----------
        send(data=dict)
            send the data to Mqtt server

    """
    def __init__(self, topic: str, hostname: str, port=1883):
        self.topic = topic
        self.hostname = hostname
        self.port = port

    def send(self, data: dict) -> bool:
        """Send data

        Args:
            data(dict): use to send to mqtt server
        """
        msgs = [{'topic': self.topic, 'payload': json.dumps(data)}]
        publish.multiple(msgs, hostname=self.hostname, port=self.port)
        return True
