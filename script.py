import pandas
import matplotlib
# reads the csv using pandas
df = pandas.read_csv('data.csv')
# selects the two columns that are needed
df = df[['purpose','int_rate']]
# groups the dataframe by the purpose and then gets the mean
df = df.groupby('purpose').mean()
# change the column name
df.columns = ['avg_rate']
# plot using values = average rate , rot (rotation of labels) set to 0 for horizontal
df.plot.bar(y='avg_rate',rot=0)
# show using matplotlib
matplotlib.pyplot.show()


