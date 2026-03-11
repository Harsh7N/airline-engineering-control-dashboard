import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model():

    data = pd.read_csv("dataset/fleet_data.csv")

    # create artificial features from row index
    data["feature1"] = range(len(data))
    data["feature2"] = data.index % 5

    X = data[["feature1", "feature2"]]

    # simulate failure label
    y = (data.index % 3 == 0).astype(int)

    model = RandomForestClassifier()
    model.fit(X, y)

    return model


model = train_model()


def predict_failure():

    sample = [[5, 2]]

    prediction = model.predict(sample)

    if prediction[0] == 1:
        return "HIGH RISK"
    else:
        return "LOW RISK"