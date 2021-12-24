import pandas as pd
import plotly.express as px

df = pd.read_csv("p103\Copy+of+data+-+data.csv")
#print(df)
fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()