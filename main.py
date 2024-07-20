
from battery_monitor import BatteryMonitor
from signal_control import SignalControl
from notification import Notification

def main():
    battery_monitor = BatteryMonitor()
    signal_control = SignalControl()
    notification = Notification()

    while True:
        battery_level = battery_monitor.check_battery()
        if battery_level < 20:
            notification.send_alert("Battery low: {}%".format(battery_level))
        
        signal_control.check_and_send_signals()

if __name__ == "__main__":
    main()
