from pathlib import PurePath
import importlib
import sys

f = PurePath(__file__)
print(f)

p = f.parents[1]
print(p)

u = p / 'src' / 'broadcastify_carch'
print(u)

a = PurePath(__file__).parents[1]
b = PurePath(PurePath(__file__).parents[1] / 'src' / 'broadcastify_carch')
print(b)

importlib.util.spec_from_file_location('bca_logger', b)

importlib.import_module('BCALogger', 'bca_logger')

