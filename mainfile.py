# Урок 10 (финальный): построение графиков
# В задаче поставлено условие: нам дан код, генерирующий DataFrame, которая состоит из одного столбца
# Наша задача - перевести этот код в one hot вид, не используя get_dummies

# Исходные данные:
# 1st = ['robot'] * 10
# 1st += ['human'] * 10
# random.shuffle(1st)
# data = pd.DataFrame({'whoAmI':1st})
# data.head()

# Чтобы решить задачу с минимальным количеством команд и оптимизацией кода, можно попробовать использовать pandas и random

import pandas as pd
import random

# Пишем решение, исходя из данных условий

1st = ['robot'] * 10
1st += ['human'] * 10
random.shuffle(1st)
data = pd.DataFrame({'whoAmI : 1st'})

# Пишем решение по one_hot, используя полученную программу

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)

# Подобный метод (astype) в pandas мы используем для преобразования столбцов в другой тип данных.
# Здесь мы преобразовываем логические значения (True/False) в численные значения (1/0)

one_hot.to_csv('graphic.csv')
print(one_hot.head(20))