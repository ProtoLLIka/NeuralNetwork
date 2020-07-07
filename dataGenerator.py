import numpy as np
from normFunction import normalization
#Рандом данных для дисциплины из 100 пар, в группе с 20 студентами
#Функция возвращает вектор из 4х параметров
def getInputData():
    inputData = []
    # Посещение
    schedule = np.random.randint(10, 20, 100)
    schedule = normalization(schedule)
    inputData.append(schedule)
    # Посещение преподавателя
    teacherVisit = np.array([1] * 100)
    # 3 раза преподаватель не явился на пару
    for i in range(3):
        teacherVisit[np.random.randint(0, 100)] = 0; 
    teacherVisit = normalization(teacherVisit)
    inputData.append(teacherVisit)
    # Номера пар. Пары с случайным номером
    numbers = np.random.randint(1, 9, 100) # Посещение
    numbers = normalization(numbers)
    inputData.append(numbers)
    # Номера дней недели.
    days = np.random.randint(1, 6, 100) # Посещение
    days = normalization(days)
    inputData.append(days)
    return inputData

print(getInputData())