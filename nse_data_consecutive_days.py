import os
import pandas as pd


def consecutive_days(fileNameWithPath, data,percentages, days = 3):
    # print(type(percentages));
    print(percentages)
    print(percentages[0]['percentage'])
    percentage = percentages[0]['percentage'];
    df2 = pd.DataFrame(data);

    # Ensure you're working with a copy of the DataFrame
    df = df2.copy()

    # Use .loc to modify the DataFrame
    df.loc[:, 'COP_DELIV_PERC'] = pd.to_numeric(df['COP_DELIV_PERC'])

    df = df[df['COP_DELIV_PERC'] > percentage];

    # Convert 'Date' column to datetime
    df['mTIMESTAMP'] = pd.to_datetime(df['mTIMESTAMP'])

    # Calculate the difference in days
    df['TimeDiff'] = df['mTIMESTAMP'].diff().dt.days

    # Identify groups of consecutive days
    df['Group'] = (df['TimeDiff'] != 1).cumsum()

    # Count the number of days in each group
    group_counts = df['Group'].value_counts()

    # Filter groups with at least 3 consecutive days
    valid_groups = group_counts[group_counts >= days].index

    # Filter the DataFrame to keep only valid groups
    filtered_df = df[df['Group'].isin(valid_groups)]

    # Drop the helper columns
    filtered_df = filtered_df.drop(columns=['TimeDiff', 'Group'])

    print(fileNameWithPath);

    # Create directory if it doesn't exist
    # os.makedirs(os.path.dirname(fileNameWithPath), exist_ok=True)

    # Convert DataFrame to CSV and save to the specified file path
    filtered_df.to_csv(fileNameWithPath, index=False)

    list_of_dicts = filtered_df.to_dict(orient='records')
    # print(list_of_dicts)

    # print(filtered_df);

    return list_of_dicts;
