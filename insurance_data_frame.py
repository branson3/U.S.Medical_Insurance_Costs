#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
import pandas as pd


# In[2]:


# This function takes the data from the .csv file and sorts it into the lists containing individual columns from the csv file.
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst


# In[4]:


# Empty lists to use to fill in with the data
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# In[5]:


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# In[10]:


insurance = pd.DataFrame(list(zip(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)), 
                         columns = ['Age', 'Sex', 'BMI', 'Num_Children', 'Smoker', 'Regions', 'Insurance_Charges'])
insurance["Insurance_Charges"] = pd.to_numeric(insurance["Insurance_Charges"], downcast="float")
insurance

