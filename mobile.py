import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff

data=pd.read_csv('mobile.csv')
fig=ff.create_distplot([data['Avg Rating'].tolist()],['Ratings']#,show_hist=False
)
fig.show()