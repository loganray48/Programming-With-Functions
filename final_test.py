import pandas as pd

from final import best_model 


'''
Purpose: Check each data type of the columns to 
         see if they are all numeric and not
         string
'''


def test_against_string(salary_data):
    for column in salary_data:
        assert column != 'string'

        # print(type(salary_data[column]).__name__ != 'string')
'''
Purpose: Check if chosen model has an
         accuracy over 50% or .5
Reason: Need to check the model to make sure that the model is 
        better than random chance. If the model is less than .5
        then the dataset we have doesn't make sense to make a model for
'''


def test_model():
    pass
