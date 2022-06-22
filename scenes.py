from logging import getLogger
from typing import List, Tuple

from command import Command
from devices_ips import LIVING_ROOM_LIGHT_IP, BEDROOM_LIGHT_IP
from light import Light


class Scene:

    def __init__(self, *lights: Light, config: List[Command] = None):
        self._lights = {light.name: light for light in lights}
        self._config = config
        self._logger = getLogger()
        self._logger.info(f"Created scene with lights: {self._lights.keys()}")

    def apply_scene(self):
        self._logger.info(f"Applying scene: {self._config}")
        for command in self._config:
            self.apply_command(command)

    def configure_scene(self, config: List[Tuple[str, ...]]):
        """
        Set up a config for the scene, to be applied later by apply_scene()
        :param config: List[Tuple[str, ...]] a list of commands, each is a tuple of strings
        For example:
        [("bedroom", "on"), ("living_room", "color", "(1,0,1)", "ambient")]
        """
        config_list = []
        for command in config:
            config_list.append(Command(*command))
        self._logger.info(f"Configured scene: {config_list}")
        self._config = config_list

    def apply_command(self, command: Command):
        if command.command == "on":
            self._lights[command.light].turn_on(command.light_type)
        if command.command == "off":
            self._lights[command.light].turn_off(command.light_type)
        if command.command == "brightness":
            self._lights[command.light].configure(brightness=command.param, light_type=command.light_type)
        if command.command == "color":
            self._lights[command.light].configure(color=command.param, light_type=command.light_type)


class Scenes:

    out = Scene(Light("living_room", LIVING_ROOM_LIGHT_IP), Light("bedroom", BEDROOM_LIGHT_IP))
    out.configure_scene([
        ("living_room", "off"),
        ("bedroom", "off")
    ])

    going_in = Scene(Light("living_room", LIVING_ROOM_LIGHT_IP), Light("bedroom", BEDROOM_LIGHT_IP))
    going_in.configure_scene([
        ("living_room", "on"),
        ("bedroom", "on")
    ])

    movie = Scene(Light("living_room", LIVING_ROOM_LIGHT_IP), Light("bedroom", BEDROOM_LIGHT_IP))
    movie.configure_scene(
        [("living_room", "off"),
         ("living_room", "on", "-", "ambient"),
         ("living_room", "brightness", "100", "ambient"),
         ("living_room", "color", "(1,0,1)", "ambient"),
         ("bedroom", "off")
         ]
    )

    reading = Scene(Light("living_room", LIVING_ROOM_LIGHT_IP), Light("bedroom", BEDROOM_LIGHT_IP))
    reading.configure_scene(
        [("living_room", "on"),
         ("living_room", "brightness", "100"),
         ("bedroom", "on"),
         ("bedroom", "brightness", "100")
         ]
    )
