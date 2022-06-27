import logging

from scenes import Scenes, create_and_apply_scene
from devices_ips import LIVING_ROOM_LIGHT_IP, BEDROOM_LIGHT_IP
from light import Light


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',)
    create_and_apply_scene(
        lights=[Light("living_room", LIVING_ROOM_LIGHT_IP), Light("bedroom", BEDROOM_LIGHT_IP)],
        config=Scenes.low_main_light
    )


if __name__ == '__main__':
    main()
