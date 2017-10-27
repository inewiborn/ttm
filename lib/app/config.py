import json

class Config:
    def __init__(self, path_to_config):
        with open(path_to_config) as f:
            self.pop_data = json.load(f)

        for pop_dict in self.pop_data:
            print(pop_dict + ' : ', end='')
            print(self.pop_data[pop_dict])

    def db(self):
        print(self.pop_data['database'])

    def port(self):
        print(self.pop_data['port'])
