import pandas as pd


def read_data(filename):
    # Function to read CSV file and return dataframe
    df = pd.read_csv(filename)
    return df


def filter_data(df, min_age_in_months=None, max_age_in_months=None, gender=None, education_level=None, features=None):
    # Apply multiple filters based on specified criteria
    filtered_df = df.copy()  # Make a copy to avoid modifying the original dataframe

    # Filter based on age
    if min_age_in_months is not None:
        filtered_df = filtered_df[filtered_df['Age_months'] >= min_age_in_months]
    if max_age_in_months is not None:
        filtered_df = filtered_df[filtered_df['Age_months'] <= max_age_in_months]

    # Filter based on gender
    if gender is not None:
        filtered_df = filtered_df[filtered_df['Gender'] == gender]

    # Filter based on education level
    if education_level is not None:
        filtered_df = filtered_df[filtered_df['Education level'] == education_level]

    # Collect start and end indices for all features
    selected_columns = []
    if features is not None:
        for feature in features:
            start_col, end_col = feature_columns.get(feature, (None, None))
            if start_col is not None and end_col is not None:
                selected_columns.extend(range(start_col - 1, end_col))

    # Select desired columns from the dataframe
    filtered_df = filtered_df.iloc[:, selected_columns]

    return filtered_df


def export_data(df, filename):
    # Export filtered dataframe to a new CSV file
    df.to_csv(filename, index=False)


feature_columns = {
'QEEG Eyes Open condition':	(9, 17108),
'EO-Absolute Power': (9, 274),
'EO-Z score Absolute Power': (275, 464),
'EO-Relative Power': (465, 730),
'EO-Z score Relative Power': (731, 920),
'EO-Power Ratio': (921, 1110),
'EO-Z score Power Ratio': (1111, 1300),
'EO-Absolute power 1 hertz': (1301, 2250),
'EO-Z score Absolute power 1 hertz': (2251, 2820),
'EO-Ralative power 1 hertz': (2821, 3770),
'EO-Z score Ralative power 1 hertz': (3771, 4340),
'EO-Peak frequency': (4341, 4606),
'EO-Z score Peak frequency:': (4607, 4796),
'EO-Amplitude Asymmetry': (4797, 7190),
'EO-Z score Amplitude Asymmetry': (7191, 8900),
'EO-Coherence': (8901, 11294),
'EO-Z score Coherence': (11295, 13004),
'EO-Phase Lag': (13005, 15398),
'EO-Z score Phase Lag': (15399, 17108),

'QEEG Eyes Close condition': (17109, 34208),
'EC-Absolute Power': (17109, 17374),
'EC-Z score Absolute Power': (17375, 17564),
'EC-Relative Power': (17565, 17830),
'EC-Z score Relative Power': (17831, 18020),
'EC-Power Ratio': (18021, 18210),
'EC-Z score Power Ratio': (18211, 18400),
'EC-Absolute power 1 hertz': (18401, 19350),
'EC-Z score Absolute power 1 hertz': (19351, 19920),
'EC-Ralative power 1 hertz': (19921, 20870),
'EC-Z score Ralative power 1 hertz': (20871, 21440),
'EC-Peak frequency': (21441, 21706),
'EC-Z score Peak frequency:': (21707, 21896),
'EC-Amplitude Asymmetry': (21897, 24290),
'EC-Z score Amplitude Asymmetry': (24291, 26000),
'EC-Coherence': (26001, 28394),
'EC-Z score Coherence': (28395, 30104),
'EC-Phase Lag': (30105, 32498),
'EC-Z score Phase Lag': (32499, 34208),
'IVA-2': (34209, 34259),
'CSI-4': (34260, 34356),
'Handedness': (34357, 34366),
"Parent's Math History": (34369, 34391),
"Parent's Reading History": (34392, 34416),
'Working Memory Task': (34417, 34455),
'Ravan Test': (34456, 34458)
}


def main():
    filename = 'iranian_child_EEG_ERP_cognitive_dataset.csv'
    df = read_data(filename)

    filtered_df = filter_data(df, min_age_in_months=110, max_age_in_months=None,
                              gender='Male', education_level='5th',
                              features=['EO-Absolute Power', 'EC-Power Ratio',
                                        'Ravan Test'])
    export_data(filtered_df, 'filtered_data.csv')


if __name__ == "__main__":
    main()
