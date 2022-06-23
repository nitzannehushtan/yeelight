import telnetlib
from logging import getLogger

from devices_ips import YEELIGHT_PORT


class Connection:
    def __init__(self, ip: str):
        self.ip = ip
        self._logger = getLogger(__name__)
        self._logger.info(f"Opening a connection to {ip}")
        self._telnet = telnetlib.Telnet(ip, port=YEELIGHT_PORT)

    def send_command(self, method: str, params: list):
        self.send_parsed_command(self.parse_command(method, params))

    def send_parsed_command(self, command_string: str):
        self._logger.info(f"Sending command: {command_string[:-1]}")
        self._telnet.write(bytes(command_string, "ascii"))

    @staticmethod
    def parse_command(method: str, params: list) -> str:
        command = str({"id": 1, "method": method, "params": params})
        command = "".join([char if char != "'" else '"' for char in command])
        return f'{command}\r\n'

    def __del__(self):
        self._logger.info(f"Closing connection to {self.ip}")
        self._telnet.close()
