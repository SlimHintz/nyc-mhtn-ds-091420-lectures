# import the relevant libraries
import pandas as pd
import numpy as np
import requests
import os
import json
#from yelp.client import Client
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# Functions to aquire business id's of any type of business I wouold like
def businesses_api_request(terms = None, location = None, search_limit = 50, price= None):
    url = 'https://api.yelp.com/v3/businesses/search'
    # Key goes into the headers parameter of the .get method.
    headers = {
        'Authorization': 'Bearer {}'.format(MY_API_KEY),
        }
    try:
        url_params = {
            'price': price,
            'term': terms.replace(' ', '+'), # The search terms should be joined by a "+"
            'location': location.replace(' ', '+'),
            'limit': search_limit
            }
    except Exception as e:
        print(e + 'please include location and search term arguments to the busineeses_api_request function')
    return requests.get(url, headers=headers, params=url_params)

def businesses_to_pandas(json_dict):
    return pd.DataFrame.from_dict(json_dict['businesses'])
                                  
                              
# def create_businesses_dataframe(master_df, number_blocks = 50):
#     for i in range(number_blocks):
#         request = business_api_request(terms = None
#     pass 
                                  
                                  
def review_api_request(i_d, offset = None):
    headers = {
    'Authorization': 'Bearer {}'.format(MY_API_KEY),
    }
    url_param = {
        'offset': offset
    }
    url = f'https://api.yelp.com/v3/businesses/{i_d}/reviews'
    return requests.get(url, headers=headers, params = url_param)


def to_dict(response_object):
    return json.loads(response_object.text)


def reviews_to_pandas(json_dict):
    df = pd.DataFrame.from_dict(json_dict['reviews'])
    return df

def concat_df(df1, df2):
    df3 = pd.concat([df1,df2])
    return df3

def create_review_dataframe(master_df, id_list, no_reveiws = 3):
    for item in id_list:
        offset = 0
        while offset < no_reviews:
            response_object = api_request(item)
            json_dict = to_dict(response_object)
            df = reviews_to_pandas(json_dict)
            # Add a column that is equal to the name associated with the index.
            df['restaurant_id'] = item
            # concatenate the data frames on top of eachother.
            master_df = pd.concat([master_df, df]).copy()
            offset += 3
    return master_df

# Helper function to insert a review len column 
def insert_review_len(dataframe):
    dataframe['review_len'] = dataframe['review'].apply(lambda x: len(x))
    return dataframe
                                  

def to_sql(dataframe, name='my_table'):
    return pd.to_sql(dataframe)
"""
TODO 

Remove all columns but the price and length id

add a new column for the length of each review.

categorize the data frame into expensive and affordable ('1-2','3-4')


group the column by id and affordability and take the average

let y be that object and x be the inner index of the column

make a bar plot of x and y

t-test between the means of the groups

"""