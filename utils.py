import yaml
import os
import pathlib
from configparser import ConfigParser

file_path_yaml = os.path.join("data", "info.yaml")
file_path_ini = os.path.join("data", "set.ini")


def loader(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    print(len(data["students"]))
    # print(data)

def config_loader(file_path):    
    config = ConfigParser()
    config.read(file_path)

    print(type(config["player"]["age"]))

    

config_loader(file_path_ini)