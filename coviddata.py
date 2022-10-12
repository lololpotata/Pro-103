import pandas as gr
import plotly.express as vs

df = gr.read_csv("CountryData.csv")

visual = vs.scatter(df, x = "date", y = "cases" , color = "country")
visual.show()
