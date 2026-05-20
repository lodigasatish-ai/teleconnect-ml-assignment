from sklearn.linear_model import LogisticRegression

def logistic_model():
    model = LogisticRegression(max_iter=1000)
    return model
