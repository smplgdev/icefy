from icefy.task import Task, TaskEnum, dicts_to_tasks


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
    
    def _ensure_file_exists(self) -> None:
        if not self.is_initialized():
            raise FileNotFoundError("File %s not found. Create it with command `ice init`" % self.file_name)

    @staticmethod
    def initialized(func):
        def wrapper(self: "ICE", *args, **kwargs):
            self._ensure_file_exists()
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def create_file(self) -> None:
        if self.is_initialized():
            raise FileExistsError("File %s already exists" % self.path)
        with self.path.open("w") as f:
            json.dump([], f)

    @initialized
    def _read(self) -> list:
        with self.path.open("r") as f:
            data = json.load(f)
        return data

    @initialized
    def _write(self, data: list) -> None:
        with self.path.open("w") as f:
            json.dump(data, f)

    def add_task(self, task: Task):
        data = self._read()
        data.append(asdict(task))
        self._write(data)
    
    def get_tasks(
        self, 
        sort_by: TaskEnum | None = None, 
        descending: bool = False, 
        limit: int | None = None
    ) -> list[Task]:
        """Retrieve tasks from the ICE file with sorting and limit options.

        Args:
            sort_by (TaskEnum, optional): Attribute to sort by (impact, confidence, ease).
            descending (bool, optional): If True, sort in descending order.
            limit (int, optional): Maximum number of tasks to return.

        Returns:
            List[Task]: A list of Task objects.
        """
        data = self._read()
        tasks = dicts_to_tasks(data)

        if sort_by and hasattr(Task, sort_by):
            tasks.sort(key=lambda t: getattr(t, sort_by), reverse=descending)

        if limit is not None:
            tasks = tasks[:limit]

        return tasks
