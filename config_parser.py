import json

class ConfigParser:
    def __init__(self, filename):
        self._load_config(filename)
    
    def _load_config(self, filename):
        with open(filename, 'r') as file:
            self.config = json.load(file)
    
    def get_config(self):
        return self.config
