import numpy as np
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, confusion_matrix, r2_score, \
    mean_squared_error
import pandas as pd


class Classification:
    def train(y_train, y_pred_train):
        accuracy = accuracy_score(y_train, y_pred_train)
        f1 = f1_score(y_train, y_pred_train)
        recall = recall_score(y_train, y_pred_train)
        precision = precision_score(y_train, y_pred_train)
        tn, fp, fn, tp = confusion_matrix(y_train, y_pred_train).ravel()
        specificity = tn / (tn + fp)

        print("Train Accuracy:", accuracy)
        print("Train F1 Score:", f1)
        print("Train Recall:", recall)
        print("Train Precision:", precision)
        print("Train Confusion Matrix:\n", confusion_matrix(y_train, y_pred_train))
        print("Train Specificity:", specificity)

    def test(y_test, y_pred_test):
        accuracy = accuracy_score(y_test, y_pred_test)
        f1 = f1_score(y_test, y_pred_test)
        recall = recall_score(y_test, y_pred_test)
        precision = precision_score(y_test, y_pred_test)
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred_test).ravel()
        specificity = tn / (tn + fp)

        print("Accuracy:", accuracy)
        print("F1 Score:", f1)
        print("Recall:", recall)
        print("Precision:", precision)
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_test))
        print("Specificity:", specificity)


class Regression:
    def train(y_train, y_pred_train):
        r2 = r2_score(y_train, y_pred_train)
        mse = mean_squared_error(y_train, y_pred_train)
        accuracy = 1 - mse / np.var(y_train)

        print("Train R2 Score:", r2)
        print("Train Mean Squared Error:", mse)
        print("Train Accuracy:", accuracy)

    def test(y_test, y_pred_test):
        r2 = r2_score(y_test, y_pred_test)
        mse = mean_squared_error(y_test, y_pred_test)
        accuracy = 1 - mse / np.var(y_test)

        print("R2 Score:", r2)
        print("Mean Squared Error:", mse)
        print("Accuracy:", accuracy)


def data_info(dataset):
    cols = []
    unique = []
    n_uniques = []
    dtypes = []
    nulls = []

    for col in dataset.columns:
        cols.append(col)
        dtypes.append(dataset[col].dtype)
        n_uniques.append(dataset[col].nunique())
        unique.append(dataset[col].unique())
        nulls.append(dataset[col].isna().sum())

    return pd.DataFrame({'Columns': cols, 'n_uniques': n_uniques,
                         'unique': unique, 'dtypes': dtypes, "NULLS": nulls
                         })
