# SEQUEENS



## Code 
Here is a sample README for the Python code to query and extract basement flooding data from NYC OpenData:

### NYC Basement Flooding Analysis

This code retrieves and analyzes basement flooding complaints from the NYC OpenData 311 complaint dataset.

#### Data Source

The data is sourced from the NYC OpenData portal, specifically the 311 complaint dataset:

- Domain: `data.cityofnewyork.us`
- Dataset ID: `erm2-nwe9`

#### Usage

The script performs the following:

1. Connects to the Socrata OpenData API using the sodapy library
2. Queries the dataset to retrieve complaints with the word "basement" in the descriptor
3. Filters down to only "Excessive Water in Basement" complaints 
4. Analyzes and explores the filtered dataframe
5. Exports filtered data to a CSV file

#### Requirements

The script requires the following libraries:

- pandas 
- sodapy
- numpy

#### Configuration

A Socrata API token is required to access the API. This should be set as an environment variable:

```
export SODAPY_APPTOKEN=<your_token>
```

#### Output

The script outputs a filtered CSV file containing only basement flooding complaints. This can be used for further analysis and visualization.

#### Resources

- NYC OpenData: https://opendata.cityofnewyork.us
- NYC 311 Dataset: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
- sodapy documentation: https://readthedocs.org/projects/sodapy/


