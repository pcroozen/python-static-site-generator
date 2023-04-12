import shutil
from pathlib import Path
from typing import List


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension: str) -> bool:
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(file=path, mode="r") as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        self.dest = dest
        full_path = self.dest / path.with_suffix(ext).name
        with open(file=full_path, mode="w") as file:
            return file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        return shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
