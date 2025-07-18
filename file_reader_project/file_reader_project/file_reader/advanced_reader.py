from .base_reader import FileReader

class AdvancedFileReader(FileReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def __str__(self):
        return f"AdvancedFileReader => {self.filename}"

    def concat_many_files(self, *others):
        new_file = "concat_all.txt"
        with open(new_file, "w") as f:
            for line in self.read_lines():
                f.write(line + "\n")
            for reader in others:
                for line in reader.read_lines():
                    f.write(line + "\n")
        return AdvancedFileReader(new_file)
