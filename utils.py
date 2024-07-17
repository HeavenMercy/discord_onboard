import itertools
import json

VERBOSE = True


class Config:
    def __init__(self) -> None:
        self._config = {}

    def load(self, filepath: str = './data/config.json'):
        """load a configuration from a json file.

        Returns:
            dict: the configuration loaded
        """
        with open(filepath, 'r') as f:
            self._config = json.load(f)

        return self

    def get(self, key: str) -> str | None:
        """returns the config corresponding to that key.

        Args:
            key (str): the key of the config to get.

        Returns:
            str | None: the config obtained.
        """
        return self._config[key] if key in self._config else None


def get_bot_key(filepath: str = './data/config.json'):
    with open(filepath, 'r') as f:
        key = f.read()

    return key


def dprint(msg: str, src: str = None, end: str = '\n', with_src: bool = True):
    """prints the message if the constant VERBOSE is True.

    Args:
        msg (str): the message to print
        src (str, optional): the source of the message. Defaults to None.
        end (str, optional): the end of the message printed. Defaults to '\n'.
        with_src (bool, optional): can show `src`? Defaults to True.
    """
    if VERBOSE:
        print(f"[{src if src else 'MAIN'}]: {
              msg}" if with_src else msg, end=end)


def get_statuses():
    """provides a list of funny statuses to use.

    Returns:
        List[str]: the list of statuses
    """
    funny_statuses = [
        "Just a bot, standing in front of a user, asking for a command.",
        "Living on a prayer.",
        "Here for a good time, not a long time.",
        "Keeping it real in the virtual world.",
        "I’m not procrastinating, I’m doing side quests.",
        "In a relationship with WiFi.",
        "Running on coffee and code.",
        "Do not disturb, I’m already disturbed enough.",
        "Loading... please wait.",
        "Spreading chaos, one command at a time."
    ]

    return itertools.cycle(funny_statuses)
