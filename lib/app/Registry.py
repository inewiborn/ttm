import os
import json


"""Реестр настроек """
class Registry:
    def __init__(self):
        self.path_to_config = os.path.expanduser('~/.ttm/config.json')
        self.options = {}
        self.file_config()

    def get_option(self, option):
        """ return option """
        return self.options[option]

    def set_option(self, option, value):
        self.options[option] = value

    def file_config(self):
        if(os.path.exists(self.path_to_config)):
            self.readfile()
        else:
            config_dir = os.path.expanduser('~/.ttm/')
            os.mkdir(config_dir)

    def readfile(self):
        with open(self.path_to_config) as f:
            pop_data = json.load(f)

        for pop_dict in pop_data:
            self.options[pop_dict] = pop_data[pop_dict]


if __name__ == "__main__":
    r = Registry()
    print(r.get_option('login'))
