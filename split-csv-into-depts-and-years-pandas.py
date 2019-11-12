import pandas as pd


file = pd.read_csv('input/Python Skill Development Programme Registration FINAL.csv')
number_of_students = open('pandas-outputs/Number of Students.txt', 'w')

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


total_students = 0
for row in output_dfs:
    for filename, df in row:
        year = ' '.join(filename.split('-')[:2])
        dept = filename.split("-")[2]
        number_of_students.write(f'{year}: {dept}\t-> {len(df):3} students\n')
        total_students += len(df)
              
        df.to_csv(f'pandas-outputs\\{filename}.csv')

    number_of_students.write('\n')

number_of_students.write(f'Total Students: {total_students}')
