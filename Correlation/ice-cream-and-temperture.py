import pandas as pd
import plotly.express as px
import csv

with open('Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv', newline='') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df, x="Temperature", y="Ice-cream Sales( ₹ )")
    fig.show()
    