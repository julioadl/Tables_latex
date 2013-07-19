import csv as csv
import sys
import numpy as np

csv_file = csv.reader(open(sys.argv[1], "rb"))
data = []

for row in csv_file:
    data.append(row)

for i in range(len(data)):
    print " & ".join(data[i]) + "\\" + "\\"
