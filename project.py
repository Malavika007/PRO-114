import pandas as pd
import plotly.express as px
import numpy as np



df = pd.read_csv('main.csv')
TOEFL_Score = df['TOEFL Score'].tolist()
Chances_of_admit = df['Chance of Admit'].tolist()

fig = px.scatter(x = TOEFL_Score, y = Chances_of_admit)
fig.show()

m = 0.01
c = -2.5
y = []
for x in TOEFL_Score:
    y_value = m * x + c
    y.append(y_value)

fig = px.scatter(x = TOEFL_Score, y = Chances_of_admit)
fig.update_layout(shapes= [
    dict(
        type='line',
        y0 = min(y), y1 = max(y),
        x0 = min(TOEFL_Score), x1 = max(TOEFL_Score)
    )
])
fig.show()

x = 600
y = m * x + c
print(f"chances of admit based on toefl score{x} is {y}")
TOEFL_Score_ARRAY = np.array(TOEFL_Score)
Chances_of_admit_ARRAY = np.array(Chances_of_admit)

m, c = np.polyfit(TOEFL_Score_ARRAY, Chances_of_admit_ARRAY, 1)
y = []

for x in TOEFL_Score_ARRAY:
    y_value = m * x + c
    y.append(y_value)


fig = px.scatter(x = TOEFL_Score_ARRAY, y = Chances_of_admit_ARRAY)
fig.update_layout(shapes= [
    dict(
        type='line',
        y0 = min(y), y1 = max(y),
        x0 = min(TOEFL_Score_ARRAY), x1 = max(TOEFL_Score_ARRAY)
    )
])
fig.show()
