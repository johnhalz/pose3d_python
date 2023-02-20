from pathlib import Path
from sys import path
path.append(Path(__file__).parents[1].as_posix())

from pose3d import ETAttr

et_1 = ETAttr.in_dim(dim=3)
et_1.random()
print(et_1)

et_2 = ETAttr(name='TR2')
et_2.vector = et_1.vector
print(et_2)

assert (et_1 == et_2)
