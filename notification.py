import paho.mqtt.client as mqtt

class Notification:
    def __init__(self, broker="mqtt.eclipse.org", port=1883):
        self.client = mqtt.Client()
        self.client.connect(broker, port, 60)

    def send_alert(self, message):
        self.client.publish("smart_fence/alert", message)
