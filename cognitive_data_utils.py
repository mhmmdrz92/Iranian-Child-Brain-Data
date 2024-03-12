import pandas as pd


def read_data(filename):
    # Function to read CSV file and return dataframe
    df = pd.read_csv(filename)
    return df


def filter_data(df, min_age=None, max_age=None, gender=None, education_level=None, eye_condition=None, disorders=None):
    # Apply multiple filters based on specified criteria
    filtered_df = df.copy()  # Make a copy to avoid modifying original dataframe

    if min_age is not None:
        filtered_df = filtered_df[filtered_df['Age'] >= min_age]
    if max_age is not None:
        filtered_df = filtered_df[filtered_df['Age'] <= max_age]
    if gender is not None:
        filtered_df = filtered_df[filtered_df['Gender'] == gender]
    if education_level is not None:
        filtered_df = filtered_df[filtered_df['Education Grade'] == education_level]
    if eye_condition is not None:
        filtered_df = filtered_df.iloc[:, 8:17109]  # Assuming eye_condition is in columns 9 to 17108
    if disorders is not None:
        filtered_df = filtered_df[disorders]  # Filter based on specified list of disorders

    return filtered_df


def export_data(df, filename):
    # Export filtered dataframe to a new CSV file
    df.to_csv(filename, index=False)


def main():
    # Main execution code
    filename = 'your_dataset.csv'
    df = read_data(filename)

    # Example usage of functions
    filtered_df = filter_data(df, min_age=7, eye_condition=True, gender=0, education_level='2nd')
    export_data(filtered_df, 'filtered_data.csv')


if __name__ == "__main__":
    main()
