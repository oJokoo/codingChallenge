import sys
import pandas as pd

fileNames = sys.argv[1:]

finalDF = pd.DataFrame()

for file in fileNames:
    tempDF = pd.read_csv(file)
    tempDF['filename'] = f'{file}'
    finalDF = finalDF.append(tempDF, ignore_index=True)

print(finalDF)

finalDF.to_csv('combinedCSV.csv', index=False)
