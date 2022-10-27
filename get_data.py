#add a google drive folder for the data
# dvc init
#access to drive folder using dvc remote add -d myremote gdrive://1zVTsKaUSqfPIT1lV8kut5DC4fqQUF6oS

# same as git we need to track the data dvc add data.csv


from sklearn.datasets import make_regression
import pandas as pd
import os
import numpy as np

# If there's no dataset in the project directory, create a reasonably large one. 
# If it exists, append some new observations. 
if os.path.isfile("data.csv"):
    n = 1
else:
    n = 50

for i in range(0,n):    
    X, y = make_regression(10000,n_features = 10)
    df = pd.DataFrame(X)
    df.to_csv("data.csv",mode='a')