from logging import getLogger
from typing import List

from yeelight import Bulb, LightType, discover_bulbs
from connection import Connection


class Light:
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip
        self._light = Bulb(self.ip)
        self._logger = getLogger(__name__)

    def get_connection(self) -> Connection:
        return Connection(self.ip)

    def turn_on(self, light_type: LightType = LightType.Main):
        self._logger.info(f"Turning {self.name} {light_type} on")
        self._light.turn_on(light_type=light_type)

    def turn_off(self, light_type: LightType = LightType.Main):
        self._logger.info(f"Turning {self.name} {light_type} off")
        self._light.turn_off(light_type=light_type)

    def set_brightness(self, brightness: int = 1):
        self._logger.info(f"Setting {self.name} brightness to: {brightness}")
        self._light.set_brightness(brightness)

    def set_ambient_color(self, ambient_color: List[int] = None):
        self._logger.info(f"Setting {self.name} ambient color to: {ambient_color}")
        self._light.set_rgb(*ambient_color, light_type=LightType.Ambient)

    def set_moonlight(self, brightness: int = 1):
        self._logger.info(f"Setting {self.name} to moonlight")
        self.get_connection().send_command("set_scene", ["nightlight", brightness])

    def set_main_light(self, color_temp: int = 4000):
        self._logger.info(f"Setting {self.name} to main light")
        self.get_connection().send_command("set_ct_abx", [color_temp, "smooth", 30])

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
