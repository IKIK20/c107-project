import csv
import plotly_express as px
import pandas as pd 

df= pd.read_csv("data.csv")

studentDf= df.loc[df["student_id"] == 'TRL_xsl']

#print(studentDf)

print(studentDf.groupby('level')['attempt'].mean())

fig = px.scatter ( df,
    x = studentDf.groupby('level')['attempt'].mean(),
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
)

fig.show()