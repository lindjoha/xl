import pandas as pd

def read_excel_file(fn):
	return pd.read_excel(fn)

def main():
	import sys
	fn = sys.argv[1]
	df = read_excel_file(fn)
	columns = list(df.columns)
	print("\n".join(columns))