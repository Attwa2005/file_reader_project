from .decorators import deco

class FileReader:
    def __init__(self, filename: str):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def read_lines(self):
        with open(self._filename, 'r') as f:
            for line in f:
                yield line.strip()

    def read_as_list(self):
        return [line for line in self.read_lines()]

    @staticmethod
    def file_exists(path):
        try:
            with open(path):
                return True
        except FileNotFoundError:
            return False

    @classmethod
    def from_list(cls, file_list):
        return [cls(f) for f in file_list]

    @deco("blue")
    def __str__(self):
        return f"FileReader({self.filename})"

    def __add__(self, other):
        new_file = "concatenated.txt"
        with open(new_file, "w") as f:
            for line in self.read_lines():
                f.write(line + "\n")
            for line in other.read_lines():
                f.write(line + "\n")
        return FileReader(new_file)
