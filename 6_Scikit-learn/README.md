# Scikit-learn (sklearn)

[Scikit-learn](https://scikit-learn.org/stable/) is a popular machine learning library in Python that provides simple and efficient tools for data mining and data analysis. It is built on top of NumPy, SciPy, and Matplotlib.

In this section, we'll use [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html), [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) and [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) from sklearn to build and evaluate machine learning models.

We'll also export the trained model using [joblib](https://joblib.readthedocs.io/en/latest/) for later use.

## Linear Regression

Linear regression is a fundamental algorithm in machine learning used for predicting a continuous target variable based on one or more input features. It assumes a linear relationship between the input features and the target variable.

### Formula

The formula for a simple linear regression model with one feature is:

$$
y = a + bx
$$

Where:

- `y`: Target variable (dependent variable)
- `a`: Intercept (the value of y when x is 0)
- `b`: Coefficient (the change in y for a one-unit change in x)
- `x`: Input feature (independent variable)
