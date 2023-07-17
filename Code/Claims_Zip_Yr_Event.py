import pandas as pd 

# Read CSV with low_memory=False to ignore mixed dtypes
data = pd.read_csv('/content/drive/MyDrive/GIS Data/QUEENS_A2/NYC Flooding ALL City/FEMA.csv', low_memory=False)  

# Clean and calculate total paid
data = data[data['amountPaidOnBuildingClaim'] != 'NULL']
data = data[data['amountPaidOnContentsClaim'] != 'NULL']

data['total_paid'] = data['amountPaidOnBuildingClaim'].astype(float) + data['amountPaidOnContentsClaim'].astype(float)

# Groupby and sum 
aggregated = data.groupby(['reportedZipCode', 'yearOfLoss', 'floodEvent'])['total_paid'].sum().reset_index()

# Export 
aggregated.to_csv('aggregated99.csv', index=False)
