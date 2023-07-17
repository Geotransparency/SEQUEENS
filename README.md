# NYC Flooding Data Aggregator - Looking at Queens

This repository contains the Python code needed to pull, process and analyze flooding data from both the NYC311 Open Data Portal and the FEMA Open Data Portal, focusing on the borough of Queens, New York. The purpose of this project is to aid in the understanding and analysis of flooding events in Queens, potentially leading to better preparation, response, and resilience for such events in the future.
  
## Setup and Installation
Clone this repository:

bash
Copy code
git clone https://github.com/<your-username>/nyc-queens-flooding-data.git
cd nyc-queens-flooding-data

Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate

***
## Code File 
Contains code examples for NYC311 (Python) and Open FEMA (R). 


### NYC311 Basement Flooding Analysis (Python)

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

  ***

### FEMA Flood Claims Analysis (R) 
This code retrieves National Flood Insurance Program (NFIP) claims data from FEMA and extracts claims for New York State to a CSV file for analysis.

#### Data Source
The data is sourced from FEMA's OpenFEMA portal using the rfema R package. Specifically the NFIP claims dataset:

Dataset: fimaNfipClaims
#### Usage
The script performs the following:

Loads the rfema package
Queries the NFIP claims dataset fields
Filters claims to only New York State between 2010-2022
Writes the filtered dataframe to a CSV file
Requirements
R and RStudio
rfema package (install.packages("rfema"))
#### Configuration
No additional configuration required.

#### Output
The filtered claims data is written to data.csv in the current working directory.

#### Resources
-OpenFEMA portal: https://www.fema.gov/openfema

-rfema package: https://cran.r-project.org/web/packages/rfema/index.html

-FEMA NFIP claims dataset: https://www.fema.gov/openfema-dataset-national-flood-insurance-program-claims

***
## Contributing
Contributions are welcomed! Please read the CONTRIBUTING.md for the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md 

## Acknowledgments
We would like to thank NYC311 and FEMA for providing open access to their data, making this project possible.

## Contact
If you have any questions, feel free to open an issue or contact us directly.

## Additional Information
This project uses data from the NYC311 Open Data Portal and FEMA Open Data Portal, but is not endorsed or funded by any government entity.

