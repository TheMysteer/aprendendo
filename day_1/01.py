import pandas as pd

values = [10, 20, 30, 40, 50]

s = pd.Series(values, index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame({
    'name': ['Mike', 'Job', 'Alice'],
    'age': [18, 17, 16],
    'job': ['Porgrammer', 'Designer', 'Teacher']
})

df = df.set_index('name')

df1 = pd.DataFrame({
    'a': [1,2,3]
}, index=[0,1,2])

df2 = pd.DataFrame({
    'a': [10,20,30]
}, index=[1,2,0])

df = df.reset_index()

df.to_csv('mydata.csv', index=None)
df.to_json('mydata.json')

print(pd.read_csv('mydata.csv', index_col=0))