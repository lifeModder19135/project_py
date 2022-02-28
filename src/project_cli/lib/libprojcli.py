import pathlib

class project:

    @property
    def rootpath(self):
        return self._root

    @rootpath.setter
    def rootpath(self, path: pathlib.Path):
        self._root = path

    @property
    def langs(self):
        return self._langtypes

    @rootpath.setter
    def rootpath(self,langs: str):
        self._langtypes = langs



