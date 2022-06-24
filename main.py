import logging

from scenes import Scenes


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',)
    # Scenes.out.apply_scene()
    # Scenes.going_in.apply_scene()
    # Scenes.movie.apply_scene()
    Scenes.sunset.apply_scene()


if __name__ == '__main__':
    main()
