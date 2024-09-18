
class Device :
    def turn_on(self):
        pass
class TV(Device):
    def turn_on(self):
        return " TV is ON now"
class Fan(Device):
    def turn_on(self):
        return "Fan is spinning now"
class Light(Device):
    def turn_on(self):
        return "Light is On Now"
def active_device(Device):
    print(Device.turn_on())
tv = TV()
fan = Fan()
light = Light()
active_device(tv)
active_device(fan)
active_device(light)

