def api_request(i_d, offset):
    headers = {
    'Authorization': 'Bearer {}'.format(MY_API_KEY),
    }
    url_param = {
        'offset': offset
    }
    url = f'https://api.yelp.com/v3/businesses/{i_d}/reviews'
    return requests.get(url_reviews, headers=headers, params = url_param)


def to_dict(response_object):
    return json.loads(response_object.text)


def to_pandas(json_dict):
    df = pd.DataFrame.from_dict(json_dict['reviews'])
    return df

def concat_df(df1, df2):
    df3 = pd.concat([df1,df2])
    return df3

def create_review_dataframe(master_df, id_list):
    for item in id_list:
        offset = 0
        while offset < 13:
            response_object = api_request(item, offset)
            json_dict = to_dict(response_object)
            df = to_pandas(json_dict)
            master_df = pd.concat([master_df, df])
            offset += 3
    return master_df