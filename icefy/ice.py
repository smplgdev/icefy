from icefy.task import Task


import json
from dataclasses import asdict
from pathlib import Path


class ICE:
    def __init__(
        self,
        dir_path: Path = Path('.'),
        file_name: str = "ice.json"
    ):
        self.file_name = file_name
        self.path = dir_path / self.file_name

    def is_initialized(self) -> bool:
        return self.path.exists()

    def initialized(func):
        def wrapper(self, *args, **kwargs):
            if not self.is_initialized():
                raise FileNotFoundError("File %s not found. Create it with command `ice init`" % self.file_name)
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def create(self):
        if self.is_initialized():
            raise FileExistsError("File %s already exists" % self.path)
        with open(self.file_name, "w") as f:
            json.dump([], f)

    @initialized
    def _read(self) -> list:
        with open(self.file_name, "r") as f:
            data = json.load(f)
        return data

    @initialized
    def _write(self, data: list) -> None:
        with open(self.file_name, "w") as f:
            json.dump(data, f)

    def add_task(self, task: Task):
        data = self._read()
        data.append(asdict(task))
        self._write(data)