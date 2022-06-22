from logging import getLogger
from typing import List

from yeelight import Bulb, LightType, discover_bulbs


class Light:
    def __init__(self, name: str, ip: str):
        self.name = name
        self._light = Bulb(ip)
        self._logger = getLogger()

    def turn_on(self, light_type: LightType = LightType.Main):
        self._logger.info(f"Turning {self.name} {light_type} on")
        self._light.turn_on(light_type=light_type)

    def turn_off(self, light_type: LightType = LightType.Main):
        self._logger.info(f"Turning {self.name} {light_type} off")
        self._light.turn_off(light_type=light_type)

    def configure(self, brightness: int = None, color: List[int] = None, light_type: LightType = LightType.Main):
        if brightness:
            self._logger.info(f"Setting {self.name} brightness to: {brightness}")
            self._light.set_brightness(brightness, light_type=light_type)
        if color:
            self._logger.info(f"Setting {self.name} color to: {color}")
            self._light.set_rgb(*color, light_type=light_type)

    @classmethod
    def get_lights(cls) -> dict:
        return discover_bulbs()

    @classmethod
    def get_lights_ips(cls) -> List[str]:
        # get the IPs of all of the available lights in the local network
        return [light["ip"] for light in cls.get_lights()]

    @classmethod
    def get_light_power(cls, ip: str) -> str:
        lights = cls.get_lights()
        light = [light for light in lights if light["ip"] == ip]
        return light[0]["capabilities"]["power"]

    @classmethod
    def get_light_brightness(cls, ip: str) -> int:
        lights = cls.get_lights()
        light = [light for light in lights if light["ip"] == ip]
        return int(light[0]["capabilities"]["bright"])
