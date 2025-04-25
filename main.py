
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import pandas as pd

app = FastAPI()

data = pd.DataFrame({
    "mile_pr": [300, 290, 280, 270],
    "lap1": [75, 73, 72, 69],
    "lap2": [78, 74, 71, 70],
    "lap3": [80, 76, 72, 69],
    "lap4": [82, 77, 72, 70]
})
X = data[["mile_pr"]]
y = data.drop("mile_pr", axis=1)
model = LinearRegression().fit(X, y)

class RaceInput(BaseModel):
    mile_pr: float

@app.post("/predict")
def predict_pace(race: RaceInput):
    prediction = model.predict([[race.mile_pr]])
    return {"recommended_splits": prediction[0].tolist()}
