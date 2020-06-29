import os


def asset(filename):
    return os.path.join(os.path.dirname(__file__), filename)
