"""
Example for building MQTT Subscriber
"""
from mqttUtils import MqttSubscriber

if __name__ == "__main__":

    # parameters for subcribing mqtt server
    # host server address
    # You can build your one from Docker Hub: https://hub.docker.com/_/eclipse-mosquitto
    HOST = 'test.mosquitto.org'
    # Set topics we subscribe
    #   yoo
    #   yee
    TOPICS = ['yoo', 'yee']

    mc = MqttSubscriber(HOST, TOPICS)

    mc.client.loop_start() # official way to run in background!

    # Avoid stop or you can use mc.client.loop_forever()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Exit!')
