import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pickle

col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]
def buildModel():
    data = pd.read_csv("kc_house_data.csv")
    outputcolumn = data['price']
    col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]
    clf = GradientBoostingRegressor(n_estimators = 400, max_depth = 10, min_samples_split = 2)
    clf.fit(data[col_imp], outputcolumn)
    pickle.dump(clf , open('model.pkl','wb'))

def predict(dict_values, col_imp=col_imp):
    clf= pickle.load(open('model.pkl','rb'))
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = clf.predict(x)[0]
    return y_pred
