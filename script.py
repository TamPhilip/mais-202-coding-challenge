import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('data.csv')
df = df[['purpose','int_rate']]
df = df.groupby('purpose').mean()
df.columns = ['avg_rate']
df.plot.bar(y='avg_rate',rot=0)
plt.show()


