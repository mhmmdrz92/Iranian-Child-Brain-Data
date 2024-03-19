# Cognitive Data Analysis Toolkit

This toolkit provides Python functions for reading, filtering, and exporting cognitive data from a CSV file. It is designed to facilitate the analysis of cognitive data collected from various tasks and questionnaires.

## Dataset Information
This repository contains cognitive feature data corresponding to the study "Iranian 6-11 years age population-based EEG, ERP, and cognition dataset". Raw EEG and ERP files can be downloaded from this link
## Usage

### Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running `pip install pandas`.

### Usage

1. Import the required functions from the toolkit:
```python
from cognitive_toolkit import read_data, filter_data, export_data
```
2. Read the cognitive data from the CSV file
```python
filename = 'iranian_child_EEG_ERP_cognitive_dataset.csv'
df = read_data(filename)
```
3. Apply filters to the data based on specified criteria:
2. Read the cognitive data from the CSV file
```python
filtered_df = filter_data(df, min_age_in_months=110, max_age_in_months=None,
                          gender='Male', education_level='5th',
                          features=['EO-Absolute Power', 'EC-Power Ratio',
                                    'Ravan Test'])
```
4. Export the filtered data to a new CSV file:
```python
export_data(filtered_df, 'filtered_data.csv')
```


### Functions

- `read_data(filename)`: Reads the cognitive data from the CSV file and returns a pandas DataFrame.
- `filter_data(df, min_age_in_months=None, max_age_in_months=None, gender=None, education_level=None, features=None)`: Filters the cognitive data based on specified criteria such as minimum/maximum age in months, gender, education level, and specific features.
- `export_data(df, filename)`: Exports the filtered cognitive data to a new CSV file.


