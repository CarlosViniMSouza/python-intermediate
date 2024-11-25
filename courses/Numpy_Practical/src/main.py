from pathlib import Path
import numpy as np

array = np.zeros((3, 2, 3))
print(id(array))

for file_count, csv_file in enumerate(Path.cwd().glob("file?.csv")):
    array[file_count] = np.loadtxt(csv_file.name, delimiter=",")

print(id(array))
print(array.shape)
print(array)