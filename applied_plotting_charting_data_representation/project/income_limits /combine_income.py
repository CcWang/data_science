import pandas as pd
import numpy as np

def clean_data(fy):
  file_name = '17_10_income_limites'+fy+'.xlsx'
  year = pd.read_excel(file_name)

  # year.rename(columns = {'State_Alpha':'state'})
  # print file_name
  print year.head()

clean_data('')