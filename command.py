from typing import List, Union, Tuple

from yeelight import LightType

COMMANDS = ["on", "off", "brightness", "color", "main", "moon"]


class Command:

    def __init__(self, command: Tuple[str, ...]):
        """
        Configure a command to be applied to a light.

        :param command: (light, command, param, light_type) or (light, command, param) or
                        (light, command) or (light, command, light_type) all params in the tuple are strings
        For example:
        ("bedroom", "on")
        ("living_room", "color", "(1,0,1)", "ambient")
        """
        assert command[1] in COMMANDS, f"Command {command[1]} is not valid"
        self.light = command[0]
        self.command = command[1]
        self.param = self.parse_param(command[2]) if len(command) > 2 else None
        self.light_type = None

        if len(command) > 3:
            self.light_type = LightType.Main if command[3] == "main" else LightType.Ambient

    @staticmethod
    def parse_param(param: str) -> Union[int, str, List[int]]:
        if param[0] == '(':
            try:
                idx1 = param.index(',')
                idx2 = idx1 + param[idx1+1:].index(',') + 1
                idx3 = param.index(')')
                return [int(param[1:idx1]), int(param[idx1+1:idx2]), int(param[idx2+1:idx3])]
            except ValueError:
                print(f"Could not parse param {param}")
        try:
            return int(param)
        except ValueError:
            return param

    def __repr__(self) -> str:
        return f"{self.light} {self.command} {self.param} {self.light_type}"
