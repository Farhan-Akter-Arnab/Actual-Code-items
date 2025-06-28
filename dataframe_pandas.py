import pandas as pd
import numpy as np
fishy_data = {'name': ['Oghuz', 'Riyad', 'Osman', 'Murad', 'Harith', 'Hasan', 'Ali', 'Abdullah', 'Abdulaziz', 'Abdulrahman', 'Inal', 'Kaykaus', 'Yusuf', 'Yunus', 'Turk', 'Hisham', 'Faruq', 'Umar', 'Abu Bakr', 'Zayd', 'Newton', 'Tariq', 'Arabi', 'Alan'],
    'score': [98.4, 100, 100, 96, 97, 98.8, 99.2, 99.6, 98.4, 88, 92.4, 88, 98.4, 99.2, 71.9, 69, 84, 98.4, 99.2, 68, 97.6, 73.2, 98.4, 100], 'attempts': [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 1, 1], 'qualify': ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 
                'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 
                'yes', 'no', 'yes', 'no', 'yes', 'yes']}
labels = ['student1', 'student2', 'student3', 'student4', 'student5','student6','student7','student8','student9','student10','student11','student12','student13','student14','student15','student16','student17','student18','student19','student20','student21','student22','student23','student24']
df= pd.DataFrame(fishy_data , index=labels)
print("Summary of the basic information about this DataFrame and its data: ")
print(df.info())