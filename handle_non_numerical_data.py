 # Author: Vaisakh Shaj

"""
Script for converting categorical values in a given dataframe to numerical values 
"""


def handle_non_numerical_data(df):
  
"""

INPUTS
- df: dataframe with columns having categorical values
OUTPUTS
- df: datframe with all categorical columns converted to numerical
- catData: dictionary of dictionaries containing information on categorical values and their corresponding integer value 
          


"""
  #class catResult:
      #def __init__(self,cat,df):
          #self.catData = cat
          #self.df = df
  columns = df.columns.values
  catData = dict()
  res = catResult(dict(),catData)
  for column in columns:
      text_digit_vals = {}
      def convert_to_int(val):
          return text_digit_vals[val]

      if df[column].dtype != np.int64 and df[column].dtype != np.float64:
          column_contents = df[column].values.tolist()
          unique_elements = set(column_contents)
          x = 0
          for unique in unique_elements:
              if unique not in text_digit_vals:
                  text_digit_vals[unique] = x
                  x+=1

          df[column] = list(map(convert_to_int, df[column]))
          catData[column]= text_digit_vals

        

  return df,catData
