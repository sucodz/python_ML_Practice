# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# add column to dataframe
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# the loop can be replaced by
cars["COUNTRY"] = cars['country'].apply(str.upper)

