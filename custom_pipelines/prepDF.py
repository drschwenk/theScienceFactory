__author__ = 'schwenk'

import pandas as pd

def recoverDF(array,original_df):
	''' This function takes an array (typically one returned from a scikit method) and
	the pandas dataframe that generated the array. It returns a pandas dataframe
	created from the array that preserves the column names and datatypes of the original
	dataframe.
	'''
	# preserving the column names and datatypes
	col_heads = list(original_df.columns.values)
	data_type_map = {}
	for col, data_t in original_df.dtypes.iteritems():
		data_type_map[col]=data_t

	new_df = pd.DataFrame(array,columns=col_heads)
	# Mapping the original data types onto the new dataframe
	for col in new_df.columns:
		new_df[col]=new_df[col].astype(data_type_map[col])

	return new_df


def dumCols(df, col_list):
	'''
	Returns new dataframe with dummarized variables replacing catagories found in columns
	:param df: dataframe to operate on
	:param col_list: list of columns containing catagorical variables
	:return: A new dataframe with dummy variables in columns
	'''
	try:
		for col in col_list:
			df = pd.concat([df,pd.get_dummies(df[col])], axis=1)
		for col in col_list:
			df = df.drop(col,1)
		return  df
	except:
		raise