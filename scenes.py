from logging import getLogger
from typing import List, Tuple

from command import Command, COMMANDS
from light import Light


class Scene:

    def __init__(self, lights: List[Light] = None, config: List[Tuple[str]] = None):
        self._lights = {light.name: light if light else None for light in lights} if lights else {}
        self._logger = getLogger(__name__)
        self._logger.info(f"Created scene with lights: {list(self._lights.keys())}")
        self._config = None
        if config:
            self.configure_scene(config)
        self._config_list = config

    def add_light(self, light: Light):
        self._lights[light.name] = light

    def apply_scene(self):
        self._logger.info(f"Applying scene: {self._config_list}")
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
            config_list.append(Command(command))
        self._logger.info(f"Configured scene: {config}")
        self._config = config_list
        self._config_list = config

    def apply_command(self, command: Command):
        assert command.command in COMMANDS, f"Command {command.command} is not valid"
        assert command.light in self._lights.keys(), f"Light {command.light} is not valid"
        if command.command == "on":
            self._lights[command.light].turn_on(command.light_type)
        if command.command == "off":
            self._lights[command.light].turn_off(command.light_type)
        if command.command == "brightness":
            self._lights[command.light].set_brightness(command.param)
        if command.command == "color":
            self._lights[command.light].set_ambient_color(command.param)
        if command.command == "main":
            self._lights[command.light].set_main_light()
        if command.command == "moon":
            self._lights[command.light].set_moonlight()


def create_scene(lights: List[Light] = None, config: List[Tuple[str]] = None) -> Scene:
    """
    Create a scene with the given lights and config.
    For a configured scene to be applied, use scene_object.apply_scene()
    :param lights: list of Light objects. If None, a scene with no lights is created
    :param config: list of tuples of strings, each tuple is a command to be applied to a light. If None, a scene with
        no config is created. Light names of the command must be in the lights list.

    :return: Scene object
    """
    return Scene(lights=lights, config=config)


def create_and_apply_scene(lights: List[Light], config: List[Tuple[str]] = None) -> Scene:
    """
    Create a scene with the given lights and config, and apply it.
    :param lights: list of Light objects. If None, a scene with no lights is created and therefore there will be no
        effect.
    :param config: list of tuples of strings, each tuple is a command to be applied to a light. If None, a scene with
        no config is created and therefore there will be no effect. Light names of the command must be in the lights
        list.
    :return: Scene object
    """
    scene = create_scene(lights=lights, config=config)
    scene.apply_scene()
    return scene


class Scenes:
    """
    Scene configurations class.
    Usage:
    scenes = Scenes(lights=[light_1, light_2], config=Scenes.movie)
    scenes.apply_scene()
    or
    scene = create_and_apply_scene(lights=[light_1, light_2], config=Scenes.reading)
    """
    out = [
        ("living_room", "off"),
        ("bedroom", "off")
    ]

    going_in = [
        ("living_room", "on"),
        ("bedroom", "on")
    ]

    movie = [
        ("living_room", "off"),
        ("living_room", "on", "-", "ambient"),
        ("living_room", "brightness", "100", "ambient"),
        ("living_room", "color", "(1,0,1)", "ambient"),
        ("bedroom", "off")
    ]

    reading = [
        ("living_room", "on"),
        ("living_room", "main"),
        ("living_room", "brightness", "100"),
        ("bedroom", "on"),
        ("bedroom", "main"),
        ("bedroom", "brightness", "100")
    ]

    low_main_light = [
        ("living_room", "on"),
        ("living_room", "main"),
        ("living_room", "brightness", "1"),
        ("bedroom", "on"),
        ("bedroom", "main"),
        ("bedroom", "brightness", "1")
    ]
