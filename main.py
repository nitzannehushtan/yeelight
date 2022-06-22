import logging

from scenes import Scenes


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    Scenes.out.apply_scene()
    # Scenes.going_in.apply_scene()
    # Scenes.movie.apply_scene()
    # Scenes.reading.apply_scene()


if __name__ == '__main__':
    main()
