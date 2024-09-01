import os
import pandas as pd

filename= os.path.join("rd", 'example.csv')
# Read the CSV file
df = pd.read_csv(filename)

# Convert the 'Date' column to datetime format
df['mTIMESTAMP'] = pd.to_datetime(df['mTIMESTAMP'])

# Calculate the time difference between consecutive rows
df['TimeDiff'] = df['mTIMESTAMP'].diff()

print(df['TimeDiff'])

# Filter rows where the time difference is less than or equal to 1 day (consecutive dates)
consecutive_dates_mask = df['TimeDiff'] == pd.Timedelta(days = 1 )
filtered_df = df[consecutive_dates_mask]

print(consecutive_dates_mask);

# filtered_df['COP_DELIV_PERC'] = filtered_df['COP_DELIV_PERC'].str.strip().replace('-', '0')
# filtered_df['COP_DELIV_PERC'] = pd.to_numeric(filtered_df['COP_DELIV_PERC'])

# Ensure you're working with a copy of the DataFrame
filtered_df = filtered_df.copy()

# Use .loc to modify the DataFrame
filtered_df.loc[:, 'COP_DELIV_PERC'] = filtered_df['COP_DELIV_PERC'].str.strip().replace('-', '0')
filtered_df.loc[:, 'COP_DELIV_PERC'] = pd.to_numeric(filtered_df['COP_DELIV_PERC'])


filtered_df = filtered_df[filtered_df['COP_DELIV_PERC'] > 60];
# filtered_df = filtered_df.groupby('CH_SYMBOL').filter(lambda group: len(group) >= 3)

# filtered_df = filtered_df[filtered_df['COP_DELIV_PERC'] > 60];
filtered_df = filtered_df.sort_values(by=[ 'CH_SYMBOL','mTIMESTAMP'])
# filtered_df = filtered_df.groupby('CH_SYMBOL').filter(lambda group: len(group) >= 3)
# filtered_df = filtered_df.groupby(['CH_SYMBOL']).filter(lambda group: len(group) >= 3)

#converting dataframe to csv file.
filtered_df.to_csv('output.csv', index=False)

print(filtered_df);