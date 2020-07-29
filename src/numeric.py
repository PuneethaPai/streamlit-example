import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
from collections import defaultdict
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC


def produce_contour_plot(clf, X, y) -> None:
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    class_dict = {c: i for i, c in enumerate(clf.classes_)}
    y = np.array([class_dict[x] for x in y])
    Z = np.array([class_dict[x] for x in Z])
    Z = Z.reshape(xx.shape)

    fig = plt.figure(figsize=(10, 10))
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
    plt.title(f"{clf.__class__.__name__} Decision Boundry")
    plt.xlabel("Component 0")
    plt.ylabel("Component 1")
    st.pyplot(fig)


def produce_confusion_matrix(clf, X, y) -> None:
    matrix = confusion_matrix(y, clf.predict(X))
    fig = plot_confusion_matrix(clf, X, y)
    st.pyplot(fig.figure_)


def single_column_analysis(df: pd.DataFrame) -> None:
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Select Column", options=columns)
    f"### Column `{selected_column}` Distribution: "
    hist_fig = px.histogram(df, x=selected_column, marginal="box")
    st.plotly_chart(hist_fig)


def column_vs_column_analysis(df: pd.DataFrame) -> None:
    f"### Correlation Plot:"
    columns = df.columns.tolist()
    cor_fig = px.scatter_matrix(df, dimensions=columns, color="species")
    st.plotly_chart(cor_fig)


def modelling(df: pd.DataFrame) -> None:
    X, y = df.iloc[:, 2:4].to_numpy(), df.iloc[:, -2]
    selected_model = st.sidebar.selectbox(
        "Select Model", model_options, format_func=lambda x: x.__class__.__name__
    )
    selected_model.fit(X, y)
    produce_contour_plot(selected_model, X, y)
    produce_confusion_matrix(selected_model, X, y)


options_dict = {
    None: lambda x: None,
    "Single Columng Analysis": single_column_analysis,
    "Column VS Column": column_vs_column_analysis,
    "Modelling": modelling,
}
model_options = [LogisticRegression(), RandomForestClassifier(), LinearSVC()]


def main():
    uploaded_file = st.file_uploader("Upload CSV Data", type="csv")
    if uploaded_file is not None:
        df = px.data.iris()
        columns = df.columns.tolist()

        f"## Data:"
        st.dataframe(df)

        "## Table Description:"
        st.table(df.describe())

        "## 3D Plot:"
        fig = px.scatter_3d(
            df, x="sepal_length", y="sepal_width", z="petal_width", color="species"
        )
        st.plotly_chart(fig)

        option_chosen = st.sidebar.selectbox(
            "Analysis Type: ", options=list(options_dict.keys()),
        )
        options_dict[option_chosen](df)


if __name__ == "__main__":
    main()
