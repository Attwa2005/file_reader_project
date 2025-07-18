from file_reader.base_reader import FileReader
import os

def test_file_reader(tmp_path):
    file1 = tmp_path / "f1.txt"
    file2 = tmp_path / "f2.txt"
    file1.write_text("Line1\nLine2")
    file2.write_text("Line3\nLine4")

    r1 = FileReader(str(file1))
    r2 = FileReader(str(file2))
    r3 = r1 + r2

    lines = list(r3.read_lines())
    assert lines == ["Line1", "Line2", "Line3", "Line4"]
