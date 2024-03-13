# Cognitive Data Analysis Toolkit

This toolkit provides Python functions for reading, filtering, and exporting cognitive data from a CSV file. It is designed to facilitate the analysis of cognitive data collected from various tasks and questionnaires.

## Dataset Information
This repository contains cognitive feature data corresponding to the study "Iranian 6-11 years age population-based EEG, ERP, and cognition dataset". Raw EEG files can be downloaded from this link
## Usage

### Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.

### Usage

1. 
2. 
3. 
4. The filtered data will be exported to a new CSV file named `filtered_data.csv`.

### Functions

- `read_data(filename)`: Reads the cognitive data from a CSV file and returns a pandas DataFrame.
- `filter_data(df, min_age=None, max_age=None, gender=None, education_level=None, eye_condition=None, disorders=None)`: Filters the cognitive data based on specified criteria such as age, gender, education level, eye condition, and specific disorders.
- `export_data(df, filename)`: Exports the filtered cognitive data to a new CSV file.

## Example

```python

# Read data from CSV file
filename = 'your_dataset.csv'
df = read_data(filename)

# Apply filters
filtered_df = filter_data(df, min_age=7, eye_condition=True, gender=0, education_level='2nd')

# Export filtered data
export_data(filtered_df, 'filtered_data.csv')
```

