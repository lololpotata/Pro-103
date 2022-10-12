import pandas as pd
import plotly.express as px
#Sorry but this has been copy pastied from scatterplot.py project
dataFrames = pd.read_csv("covid_data.csv")
framesInGraph = px.scatter(dataFrames, x="country", y="date",
	          size="cases",color="country",
                   size_max=60)
framesInGraph.show()
