import os
import pandas as pd

# Creating DataFrame
filename= os.path.join("rd", 'example.csv')
df2 = pd.read_csv(filename)

# Ensure you're working with a copy of the DataFrame
df = df2.copy()

# Use .loc to modify the DataFrame
df.loc[:, 'COP_DELIV_PERC'] = df['COP_DELIV_PERC'].str.strip().replace('-', '0')
df.loc[:, 'COP_DELIV_PERC'] = pd.to_numeric(df['COP_DELIV_PERC'])

df = df[df['COP_DELIV_PERC'] > 60];

# Convert 'Date' column to datetime
df['mTIMESTAMP'] = pd.to_datetime(df['mTIMESTAMP'])

# Calculate the difference in days
df['TimeDiff'] = df['mTIMESTAMP'].diff().dt.days

# Identify groups of consecutive days
df['Group'] = (df['TimeDiff'] != 1).cumsum()

# Count the number of days in each group
group_counts = df['Group'].value_counts()

# Filter groups with at least 3 consecutive days
valid_groups = group_counts[group_counts >= 3].index

# Filter the DataFrame to keep only valid groups
filtered_df = df[df['Group'].isin(valid_groups)]

# Drop the helper columns
filtered_df = filtered_df.drop(columns=['TimeDiff', 'Group'])

print(filtered_df)

# # Filter rows where the time difference is less than or equal to 1 day (consecutive dates)
# consecutive_dates_mask = df['TimeDiff'] == pd.Timedelta(days = 1 )
# filtered_df = df[consecutive_dates_mask]

# print(consecutive_dates_mask);

# # filtered_df['COP_DELIV_PERC'] = filtered_df['COP_DELIV_PERC'].str.strip().replace('-', '0')
# # filtered_df['COP_DELIV_PERC'] = pd.to_numeric(filtered_df['COP_DELIV_PERC'])

# # Ensure you're working with a copy of the DataFrame
# filtered_df = filtered_df.copy()

# # Use .loc to modify the DataFrame
# filtered_df.loc[:, 'COP_DELIV_PERC'] = filtered_df['COP_DELIV_PERC'].str.strip().replace('-', '0')
# filtered_df.loc[:, 'COP_DELIV_PERC'] = pd.to_numeric(filtered_df['COP_DELIV_PERC'])


# filtered_df = filtered_df[filtered_df['COP_DELIV_PERC'] > 60];
# # filtered_df = filtered_df.groupby('CH_SYMBOL').filter(lambda group: len(group) >= 3)

# # filtered_df = filtered_df[filtered_df['COP_DELIV_PERC'] > 60];
# filtered_df = filtered_df.sort_values(by=[ 'CH_SYMBOL','mTIMESTAMP'])
# # filtered_df = filtered_df.groupby('CH_SYMBOL').filter(lambda group: len(group) >= 3)
# # filtered_df = filtered_df.groupby(['CH_SYMBOL']).filter(lambda group: len(group) >= 3)

#converting dataframe to csv file.
filtered_df.to_csv('output.csv', index=False)

# print(filtered_df);
