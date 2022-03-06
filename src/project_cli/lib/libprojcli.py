
import os
import pathlib

class File(os.File):
    
    def __init__(self, path:pathlib.Path) -> None:
        super().__init__(self)


class FileBuilder(object):
    pass

class Directory():
    pass

class StructConf(object):

    def __init__(self):
        self._dirs: list[Directory] = list()

    @property
    def projectdirs():
        return self._dirs



class project:

    @property
    def rootpath(self):
        return self._root

    @rootpath.setter
    def rootpath(self, path: pathlib.Path):
        self._root = path

    @property
    def langs(self):
        if self._langtypes:
            if type(self._langtypes) == str:
                return self._langtypes
            elif type(self._langtypes) == list:
                if len(self._langtypes) == 1:
                    return str(self._langtypes[0])
                else:
                    return self._langtypes
            else:
                raise TypeError

    @rootpath.setter
    def rootpath(self,langs: str):
        self._langtypes = langs

    def build_project(self, location, structure_config):
        
        self.__make_project_dirs(location, structure_config)

    def __add_dir_to_path(dir:Directory):
        pass

    def __make_project_dirs(self, location, structure_config):
        with os.walk