
# coding: utf-8

# In[33]:

import pymongo
import charts


# In[30]:

client = pymongo.MongoClient('localhost', 27017)
Movies = client['Movies']
item_infoX = Movies['item_infoX']


# In[31]:

for i in item_infoX.find().limit(50):
    print(i['rank'],i['title'])


# In[32]:

for i in item_infoX.find():
    if i['rank']:
        rank = i['rank']
    else:
        rank = '0'
    item_infoX.update({'_id':i['_id']},{'$set':{'rank': rank}})


# In[40]:

series = [
    {
        'name' : 'os X',
        'data' : [8],
        'type' : 'column'
    },
    {
        'name' : 'windows',
        'data' : [11],
        'type' : 'column'
    },
    {
        'name' : 'Ubuntu',
        'data' : [5],
        'type' : 'column'
    }
]
charts.plot(series, show='inline', options=dict(title=dict(text='This is test！')))


# In[42]:

rank_list = []
for i in item_infoX.find():
    rank_list.append(i['rank'])
rank_index = list(set(rank_list))
print(rank_index)


# In[45]:

rank_index.sort()
print(rank_index)


# In[47]:

counts = []
for index in rank_index:
    counts.append(rank_list.count(index))
print(counts)


# In[50]:

def data_gen(types):
    length = 0
    if length <= len(rank_index):
        for rank, count in zip(rank_index, counts):
            data = {
                'name' : rank,
                'data' : [count],
                'type' : types
            }
            yield data
            length += 1
    


# In[51]:

data_gen('column')


# In[52]:

for i in data_gen('column'):
    print(i)


# In[53]:

series = [i for i in data_gen('column')]
charts.plot(series, options=dict(title=dict(text='Movies rank.')))


# In[ ]:



