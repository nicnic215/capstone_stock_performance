# FACTOR-Based Stock Selection for Portfolio Management

## Data Acquisition

!(screenshots/'stock selection')
### Data Sources

Bloomberg Terminal, GuruForcus, MorningStar, Yahoo Finance & AlphaVantage

### Features

The features include fundamentals, technical factors and the related indices data.
We used Sharpe Ratio as a means to arrive at our target variable by calculating its Sharpe Ratio value for each stock in each and every month. We then ranked their respective values in four quartiles, with the highest-performing quartile labelled as “buy" and the lowest-performing one as “sell”.


### Dataset

## Our Approach - Feature and Model Engineering

-Dataset from 1999 through 2019.
-Define two training sets in a walk-forward approach
-The RECENT training set included all data from the prior 12 months
The SEASONAL training set included all data from the same calendar month over the prior 10 years
 Seven different algorithms would be used on each of the training sets
AdaBoost, XGBoost, KNN,  Neural Network, LightGBM, SVM and Random Forest for model stacking

### Flow Architecture

## Evaluation - Score of Base Models on recent training set

### Feature Importance of a particular month

The model was fitted with XGBoost from January 2007 to January 2017.


## Evaluation - Score of Final Stcking Model (Random Forest) on recent training set


## Deployment



