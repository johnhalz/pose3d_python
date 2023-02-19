from pathlib import Path
from sys import path
path.append(Path(__file__).parents[1].as_posix())

from pose3d import ETAttr

et_1 = ETAttr(name='TR1')
et_1.random()
print(et_1)

et_2 = ETAttr(name='TR2')
et_2.random()
print(et_2)

print(et_1 == et_2)
