import matplotlib.pyplot as math
students_names = ["Riyad", "Oghuz", "Batu", "Murad", "Hasan", "Muhammad", "Umar", "Uthman"]
students_marks = [240, 238, 224, 230, 234, 240, 212, 218]
marks_perc = []
for x in students_marks:
    perc = (x / 240) * 100
    marks_perc.append(perc)
print(marks_perc)
# Line Chart
def line_chart():
    math.plot(students_names, students_marks)
    math.title("Students Marks Line Graph")
    math.xlabel("Students")
    math.ylabel("Marks")
    math.show()
line_chart()
# Bar Chart
def bar_chart():
    math.bar(students_names, marks_perc)
    math.title("Students Marks Line Graph")
    math.xlabel("Students")
    math.ylabel("Marks")
    math.show()
bar_chart()