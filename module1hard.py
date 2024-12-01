grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
std = [[4], [3], [2], [3], [5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_s= sorted (students) # Сортируем имена студентов по алфавиту
my_tuple = tuple(student_s)  # Преобразуем тип
std_1=sum(grades[0])/len(grades[0])
std_2=sum(grades[1])/len(grades[1])
std_3=sum(grades[2])/len(grades[2])
std_4=sum(grades[3])/len(grades[3])
std_5=sum(grades[4])/len(grades[4])
sr_grades=std_1,std_2,std_3,std_4,std_5
mmy_list=dict(zip(student_s, sr_grades))
print(mmy_list)