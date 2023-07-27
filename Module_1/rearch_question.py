# Compare how student's grades compare to students from a prior semester.
# Thomas D'Angelo
import statistics

csv = "sample_grades.csv"  # Read the file

# Data Variables
spring = []
fall = []

data_file = open(csv, "r")                              # Open csv
for student in data_file:                               # read each line
    st_list = student.rstrip().split(",")               # remove whitespace, split on ","
    if st_list[1] == "Spring 2016":                     # if class is spring 2016
        spring.append(int(st_list[2]))                  # Add grade to spring list
    elif st_list[1] == "Fall 2016":                     # if class is fall 2016
        fall.append(int(st_list[2]))                    # Add grade to fall list

data_file.close()

print("\t\t\t Fall 2016\t\tSpring 2016")
print("Mean:\t\t {s:.2f}\t\t\t{f:.2f}"
      .format(s=statistics.mean(spring), f=statistics.mean(fall)))
print("Median:\t\t {s:.2f}\t\t\t{f:.2f}"
      .format(s=statistics.median(spring), f=statistics.median(fall)))
print("STD:\t\t {s:.2f}\t\t\t{f:.2f}"
      .format(s=statistics.pstdev(spring), f=statistics.pstdev(fall)))
