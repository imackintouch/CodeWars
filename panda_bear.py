import pandas as pd

df = pd.DataFrame({
                        'quantity': [3, 5.5, 7],
                        'item':     ['shoe', 'candy', 'book']
                  },
                  index=[0.5, 0.95, 0.99]
                  )
print(df)

# Convert index values of dataframe into a string that represents what percentile the values represent.
df.rename(index=lambda ival: str(int(ival*100))+'th_percentile', inplace=True)
print(df)
