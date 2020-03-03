"""
Example for sending data to MQTT server
"""

from mqttUtils import MqttSender

if __name__ == "__main__":

    HOST = 'test.mosquitto.org'

    # sender test
    yee_sender = MqttSender('yee', HOST)
    yoo_sender = MqttSender('yoo', HOST)

    yee_sender.send({'test1': 1234, 'test2': 'yee'})
    yoo_sender.send(1234)
    yoo_sender.send(b'ABCDEFG')
    yoo_sender.send(['1', 'a', 'b'])