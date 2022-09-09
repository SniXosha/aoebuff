import json
import os


def load_obj(path, default):
    if not os.path.exists(path):
        return default

    with open(path, 'r') as file:
        return json.load(file)


def save_obj(history, path):
    with open(path, 'w') as file:
        return json.dump(history, file)
