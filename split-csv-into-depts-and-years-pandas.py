import pandas as pd


file = pd.read_csv('input/Python Skill Development Programme Registration FINAL.csv')

depts = ['CSE', 'IT', 'ECE', 'EIE', 'EE', 'ME', 'MCA']
years = 4

file['Year'] = file['Year'].apply(lambda y: int(y[0]))

output_dfs = [
    [
        (
            f'Year-{i + 1}-{dept}',
            file[(file['Year'] == i+1) & (file['Department'] == dept)]
        )
        for dept in depts
    ]
    for i in range(years)
]

for row in output_dfs:
    for filename, df in row:
        df.to_csv(f'pandas-outputs\\{filename}.csv')
