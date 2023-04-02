#!/usr/bin/env python
# coding: utf-8

# ## Проект "Влияние клинико-морфологических показателей на клинико-реабилитационный прогноз больных с остеопорозом"

# In[1]:


# импортируем библиотеку Pandas
import pandas as pd


# In[2]:


# вставляем путь к файлу в переменную path
path = r"E:\Data science\Pet_project\Sveta_data\Kniga1.xlsx"


# In[3]:


# загрузим файлы excel из таблиц
data_osteoporosis = pd.read_excel(path, sheet_name='Остеопороз лаб')
data_related = pd.read_excel(path, sheet_name='Остео сопут')
data_complaints = pd.read_excel(path, sheet_name='Остео жалобы')
data_fracture = pd.read_excel(path, sheet_name='Остео_перелом')
data_other = pd.read_excel(path, sheet_name='СД_прочие')
data_complaints_2 = pd.read_excel(path, sheet_name='СД_остео_жалобы')


# In[4]:


# посмотрим первые пять строк фрейма данных data_osteoporosis
data_osteoporosis.head()


# In[5]:


# посмотрим последние пять строк фрейма данных data_osteoporosis
data_osteoporosis.tail()


# In[ ]:





# In[ ]:





# In[ ]:




