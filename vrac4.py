# -*- coding: utf-8 -*-
import pathlib
print(pathlib.Path.cwd())
print(pathlib.Path.cwd().parent)


path=pathlib.Path.cwd().parent.joinpath('dataFormationPython')
print(path)