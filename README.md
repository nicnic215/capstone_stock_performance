# FACTOR-Based Stock Selection for Portfolio Management

## Data Acquisition

![](https://github.com/nicnic215/capstone_stock_performance/blob/master/stock%20slection.png)

### Data Sources

Bloomberg Terminal, GuruForcus, MorningStar, Yahoo Finance & AlphaVantage

### Features

The features include fundamentals, technical factors and the related indices data.
We used Sharpe Ratio as a means to arrive at our target variable by calculating its Sharpe Ratio value for each stock in each and every month. We then ranked their respective values in four quartiles, with the highest-performing quartile labelled as “buy" and the lowest-performing one as “sell”.


### Dataset

![](https://github.com/nicnic215/capstone_stock_performance/blob/master/full_dataset.png)


![](https://github.com/nicnic215/capstone_stock_performance/blob/master/monthly_dataset.png)


### Sharpe Ratio

![](https://github.com/nicnic215/capstone_stock_performance/blob/master/sharpe_ratio.png)


## Our Approach - Feature and Model Engineering

-Dataset from 1999 through 2019.
-Define two training sets in a walk-forward approach
-The RECENT training set included all data from the prior 12 months
The SEASONAL training set included all data from the same calendar month over the prior 10 years
 Seven different algorithms would be used on each of the training sets
AdaBoost, XGBoost, KNN,  Neural Network, LightGBM, SVM and Random Forest for model stacking

![](https://github.com/nicnic215/capstone_stock_performance/blob/master/walk_forward.png)


### Flow Architecture

![](https://github.com/nicnic215/capstone_stock_performance/blob/master/flow.png)

## Evaluation - Score of Base Models on recent training set


![](https://github.com/nicnic215/capstone_stock_performance/blob/master/score.png)


### Feature Importance of a particular month

The model was fitted with XGBoost from January 2007 to January 2017.


![](https://github.com/nicnic215/capstone_stock_performance/blob/master/feature_importance.png)


## Evaluation - Score of Final Stcking Model (Random Forest) on recent training set


![](https://github.com/nicnic215/capstone_stock_performance/blob/master/final_score.png)


## Deployment


![](https://github.com/nicnic215/capstone_stock_performance/blob/master/deploy.png)



