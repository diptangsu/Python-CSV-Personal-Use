import csv

input_file = open('input/Python Skill Development Programme Registration FINAL.csv', 'r')
number_of_students = open('outputs/Number of Students.txt', 'w')

depts = ['CSE', 'IT', 'ECE', 'EIE', 'EE', 'ME', 'MCA']
years = 4

# stores the csv writers for each file.
writer = [
    [
        csv.writer(
            open(f'outputs/Year {i + 1} Dept {dept}.csv', 'w')
        )
        for dept in depts
    ] 
    for i in range(years)
]


# stores number of student per stream per year.
counter_of_students = [
    [
        0 
        for j in range(no_of_depts)
    ] 
    for i in range(years)
]

for row in csv.reader(input_file):
	if row[4][0] == 'Y':
		continue
	
	year = int(row[4][0]) - 1  # 5th column of csv stores year, -1 for 0 indexing
	dept = depts.index(row[5])  # 6th column stores the department
	
	writer[year][dept].writerow(row)
	counter_of_students[year][dept] += 1

# Filling up a file with details about number of students per dept per year.
for i in range(years):
	number_of_students.write(f'Year {i + 1}\n')
	s = 0
	for j, dept in enumerate(depts):
		s += counter_of_students[i][j]
		number_of_students.write(f'{dept}\t-> {counter_of_students[i][j]} students\n')
	number_of_students.write(f'Total = {s} students\n\n')

# close all the files
number_of_students.close()
input_file.close()
for i in range(years):
	for j in range(no_of_depts):
		output[i][j].close()
