from unittest import TestCase
from light import Light


class TestLight(TestCase):
    def setUp(self) -> None:
        self.light_ip = Light.get_lights_ips()[0]
        self.light = Light("living_room", self.light_ip)
        self.light.turn_off()

    def test_power(self):
        self.light.turn_on()
        assert Light.get_light_power(self.light_ip) == "on", "Light is not on"
        self.light.turn_off()
        assert Light.get_light_power(self.light_ip) == "off", "Light is not off"
        self.light.turn_on()
        assert Light.get_light_power(self.light_ip) == "on", "Light is not on"

    def test_brightness(self):
        self.light.turn_on()
        self.light.set_brightness(100)
        assert Light.get_light_brightness(self.light_ip) == 100, \
            f"Brightness is {Light.get_light_brightness(self.light_ip)} instead of 100"
        self.light.set_brightness(50)
        assert Light.get_light_brightness(self.light_ip) == 50, \
            f"Brightness is {Light.get_light_brightness(self.light_ip)} instead of 50"
        self.light.set_brightness(1)
        assert Light.get_light_brightness(self.light_ip) == 1, \
            f"Brightness is {Light.get_light_brightness(self.light_ip)} instead of 1"
