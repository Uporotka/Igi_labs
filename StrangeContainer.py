import os
import json
import re


class StrangeContainer:
    _user = str()
    _container: set[str] = set()
    _file = str()

    def __init__(self, user):
        self._user = user
        self._file = f'./users/{user}.json'
        self.load()

    def add(self, elem):
        self._container.add(elem)

    def remove(self, elem):
        self._container.remove(elem)

    def find(self, elem):
        if elem in self._container:
            return elem

    def list(self):
        return list(self._container)

    def grep(self, regex):
        return list(filter(lambda elem: re.match(regex, elem), self._container))

    def save(self):
        os.makedirs(os.path.dirname(self._file), exist_ok=True)
        with open(self._file, 'w') as f:
            json.dump(list(self._container), f)

    def load(self):
        if os.path.exists(self._file):
            with open(self._file, 'r') as f:
                self._container = set(json.load(f))

    def load_from_file(self, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                tmp_container = set(json.load(file))
                for i in tmp_container:
                    self._container.add(i)

    def switch(self, user):
        self._user = user
        self._file = f'./users/{user}.json'
        self._container.clear()
