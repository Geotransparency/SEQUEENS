# pip install sodapy

# importing libraries
import pandas as pd
import numpy as np
from sodapy import Socrata
import os

# nyc open data domain and 311 dataset id
socrata_domain = 'data.cityofnewyork.us'
socrata_dataset_identifier = 'erm2-nwe9'

# If you choose to use a token, run the following command on the terminal (or add it to your .bashrc)
# $ export SODAPY_APPTOKEN=<token>
socrata_token = os.environ.get("TOKENNUMBERHERE")

# connecting to soda api
client = Socrata(socrata_domain, socrata_token)

metadata = client.get_metadata(socrata_dataset_identifier)
print('type: {}'.format(type(metadata)))
print('count of items: {}'.format(len(metadata)))

# preview keys
for key in metadata.keys():
    print(key)

# continue to preview items
print('type: {}'.format(type(metadata['columns'])))
print('length: {}'.format(len(metadata['columns'])))
metadata['columns'][0]

# printing column names
[x['name'] for x in metadata['columns']]

# printing column field names
[x['fieldName'] for x in metadata['columns']]

# preview complaint type column
meta_amount = [x for x in metadata['columns'] if x['name'] == 'Complaint Type']
meta_amount[0]

# preview descriptor column
meta_amount = [x for x in metadata['columns'] if x['name'] == 'Descriptor']
meta_amount[0]

"""##Preview and Explore Data

"""

# practice query using the sodapy client and basic query format
# manually force limit rows to high value that includes ~all rows
# Group and count 311 complaints by complaint_type

client = Socrata("data.cityofnewyork.us", socrata_token, timeout=10000)

query = """
SELECT
    complaint_type,
    count(complaint_type)
GROUP BY
    complaint_type
ORDER BY
    count(complaint_type) DESC
LIMIT
    100
"""

# Returned as JSON from API / converted to Python list of
# dictionaries by sodapy
results = client.get("erm2-nwe9", query=query)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print('shape of data: {}'.format(results_df.shape))
results_df.head(10)

# Group and count 311 complaints by descriptor
# client = Socrata("data.cityofnewyork.us", socrata_token, timeout=1000)

query = """
SELECT
    descriptor,
    count(descriptor)
GROUP BY
    descriptor
ORDER BY
    count(descriptor) DESC
LIMIT
    100
"""

results = client.get("erm2-nwe9", query=query)
results_df = pd.DataFrame.from_records(results)

print('shape of data: {}'.format(results_df.shape))
results_df.head(10)

# Group complaint_type where type has the word water in it
query = """
SELECT
    complaint_type,
    count(complaint_type)
WHERE
    LOWER(complaint_type) LIKE '%water%'
GROUP BY
    complaint_type
ORDER BY
    count(complaint_type) DESC
LIMIT
    100
"""

results = client.get("erm2-nwe9", query=query)
results_df = pd.DataFrame.from_records(results)

print('shape of data: {}'.format(results_df.shape))
results_df

# Group descriptor where type has the word basement in it
# client = Socrata("data.cityofnewyork.us", socrata_token, timeout=1000)

query = """
SELECT
    descriptor,
    count(descriptor)
WHERE
    LOWER(descriptor) LIKE '%basement%'
GROUP BY
    descriptor
ORDER BY
    count(descriptor) DESC
LIMIT
    100
"""

results = client.get("erm2-nwe9", query=query)
results_df = pd.DataFrame.from_records(results)

print('shape of data: {}'.format(results_df.shape))
results_df

# select all rows where descriptor has the word basement in it
# client = Socrata("data.cityofnewyork.us", socrata_token, timeout=10000)

query = """
SELECT
    *
WHERE
    LOWER(descriptor) LIKE '%basement%'
LIMIT
    40000
"""

results = client.get("erm2-nwe9", query=query)
results_df = pd.DataFrame.from_records(results)

print('shape of data: {}'.format(results_df.shape))
results_df.head()

results_df['descriptor'].value_counts()

flooding_df = results_df.loc[results_df['descriptor'] == 'Excessive Water In Basement (WEFB)']
flooding_df = flooding_df.reset_index(drop=True)

flooding_df.head()

flooding_df['descriptor'].value_counts()

flooding_df['complaint_type'].value_counts()

# reviewing what descriptors are in the complaint_type== Water System
# client = Socrata("data.cityofnewyork.us", socrata_token, timeout=1000)

query = """
SELECT
    descriptor,
    count(descriptor)
WHERE
    complaint_type='Water System'
GROUP BY
    descriptor
ORDER BY
    count(descriptor) DESC
LIMIT
    1000
"""
results = client.get("erm2-nwe9", query=query)
results_df = pd.DataFrame.from_records(results)

print(results_df.shape)
results_df.head(len(results_df))

print('Number of total records: {:,}\n'.format(len(flooding_df)))

print('min date:', flooding_df['created_date'].min())
print('max date:', flooding_df['created_date'].max())

# previewing data
(flooding_df
 .loc[flooding_df.created_date < '2023']
 .sort_values(by='created_date', ascending=False)
 .head()
)

flooding_df = flooding_df.loc[flooding_df.created_date < '2023']

print('Number of total records: {:,}\n'.format(len(flooding_df)))

print('min date:', flooding_df['created_date'].min())
print('max date:', flooding_df['created_date'].max())

# # writing output file as a csv
flooding_df.to_csv('/content/basement_flood.csv', index=False)

