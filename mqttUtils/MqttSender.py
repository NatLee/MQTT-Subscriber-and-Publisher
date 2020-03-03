"""
Example for sending messages to mqtt server

"""
import pickle
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
        send(data=pickle.OBJ)
            send the data to Mqtt server

    """
    def __init__(self, topic: str, hostname: str, port=1883):
        self.topic = topic
        self.hostname = hostname
        self.port = port

    def send(self, data: pickle.OBJ) -> bool:
        """Send data

        Args:
            data(pickle.OBJ): use to send to mqtt server
        """
        msgs = [{'topic': self.topic, 'payload': pickle.dumps(data)}]
        publish.multiple(msgs, hostname=self.hostname, port=self.port)
        return True
