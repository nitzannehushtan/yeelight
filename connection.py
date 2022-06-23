import telnetlib

from devices_ips import YEELIGHT_PORT


class Connection:
    def __init__(self, ip: str):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip, port=YEELIGHT_PORT)

    def send_command(self, method: str, params: list):
        self.send_parsed_command(self.parse_command(method, params))

    def send_parsed_command(self, command_string: str):
        self.telnet.write(bytes(command_string, "ascii"))

    @staticmethod
    def parse_command(method: str, params: list) -> str:
        command = str({"id":1,"method": method, "params": params})
        command = "".join([char if char != "'" else '"' for char in command])
        return f'{command}\r\n'
