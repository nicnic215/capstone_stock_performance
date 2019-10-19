# capstone_stock_performance


## The Problem

For many years, traditional statistical techniques like linear regression model are often used in the finance  in predicting stock momentums and thus investors would be able to generate stock returns , but only few have found successful. This may due to the reasons that financial data are inherently noisy, that factors can be multi-collinear. The relationships between factors and returns can be variable, nonlinear, and/or contextual. 

This comes to the machine learning approach that most investors believe it can uncover subtle, contextual and non-linear relationship, nevertheless, overfitting  of the models poses the major challenges in the area.

The goal of the project is, by training different classes of algorithms on different subsets of the factors to get an outcome of stock trends, so as to determine to BUY, SELL or HOLD from a basket of the 20 largest biophamarcurical companies listed in the New York Stock Exchange.


## Our Approaches - Data Acquisition

![alt text](https://github.com/nicnic215/capstone_stock_performance/blob/master/stock_table.png)


Data Sources:

Bloomberg Terminal, GuruForcus & AlphaVantage 
Over 200 features of each stock were chosen across a time period of 19 years from 2000. 
The features include fundamentals, technical factors and the related indices data.
The target feature is the return calculated based on Fama-French five-factor asset model.


## Our Approaches – Feature & Model Engineering

Use data from 2000-2017 for training sets and 2018-2019 as testing test
Define three training sets in a walk-forward approach
Four different algorithms would be used on each of the training sets

![alt text](https://github.com/nicnic215/capstone_stock_performance/blob/master/graph_flow.png)
