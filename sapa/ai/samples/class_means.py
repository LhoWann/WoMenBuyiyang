import pandas as pd  # noqa: F401
from sklearn.datasets import load_iris


def class_means(min_length):
    iris = load_iris(as_frame=True)
    df = iris.frame
    long_ones = df[df["sepal length (cm)"] > min_length]
    means = long_ones.groupby("target")["petal length (cm)"].mean()
    best = means.idxmax()
    return best