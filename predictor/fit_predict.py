__author__ = 'schwenk'

import pickle
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import ElasticNet
import pkgutil

from custom_pipelines import prepDF as prep

picklefile = pkgutil.get_data("predictor", 'franchise_data_proc.pkl')
complete_data_for_pandas = pickle.loads(picklefile)
complete_df = pd.DataFrame(complete_data_for_pandas)

features = ['prev_gross','days_elapsed','act_meta','same_genre','same_dir']

def modelFit(franchise_df):
	cleaned_df = franchise_df.dropna()
	# cleaned_df= cleaned_un.sort(columns='prev_gross')

	train, test = train_test_split(cleaned_df, test_size = 0.10)

	train_df = prep.recoverDF(train,cleaned_df)
	X_train = train_df[features]
	Y_train = train_df[['act_gross']]

	# test_df = prep.recoverDF(train,cleaned_df)
	# X_test = test_df[['prev_gross','act_meta','days_elapsed','same_genre','same_dir']]
	# Y_test = test_df[['act_gross']]

	lin_mod = ElasticNet(1.0, l1_ratio = 0.5)
	lin_mod.fit(X_train,Y_train)

	# print(lin_mod.coef_)
	# print(lin_mod.intercept_)
	# print(lin_mod.score(X_train, Y_train))

	return lin_mod

# This is an example of the x val to pass to the predict function

def make_predict(lin_model, film):
	predicted_gross =lin_model.predict(film)
	return predicted_gross