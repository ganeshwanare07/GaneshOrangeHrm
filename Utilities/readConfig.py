import configparser
import os

config = configparser.ConfigParser()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_path = os.path.join(
    base_dir,
    "Configurations",
    "config.ini"
)

config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_username():
        return config.get("login", "username")

    @staticmethod
    def get_password():
        return config.get("login", "password")

    @staticmethod
    def get_login_url():
        return config.get("login", "login_url")