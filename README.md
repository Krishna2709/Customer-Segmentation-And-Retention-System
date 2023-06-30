# Customer Segmentation and Retention System :family_man_woman_girl_boy:
This project involves a data-driven analysis on a customer dataset with the aim of understanding customer segmentation in acquisition. The analysis includes exploratory data analysis, data preprocessing, model building, model evaluation, and A/B testing design. The findings from this analysis can help in tailoring the approach to each customer segment and iterating on the strategies.

## :mag_right: Exploratory Data Analysis
The dataset contains information about customers such as age, income, product owned, competitor product owned, last purchase, whether they churned or not and their product knowledge. The target variable is 'churned', which indicates whether a customer has churned or not.

## :bar_chart: Data Preprocessing
The data preprocessing involved handling missing values and encoding categorical variables. Missing values in the 'product_owned' and 'competitor_product_owned' columns were imputed with the most frequent category in each column. Categorical variables were encoded using one-hot encoding.

## :hammer_and_wrench: Model Building
A baseline model was built using Logistic Regression. The dataset was split into a training set and a testing set and the model was trained on the training set.

## :dart: Model Evaluation
The model was evaluated using metrics such as accuracy, precision, recall, F1 score, and ROC AUC score. The model showed moderate performance, with a relatively high recall but low precision. This indicates that the model is able to identify a good proportion of the positive class (churned customers) correctly, but among the customers that the model predicted as churned, less than half are actually churned.

## :bulb: A/B Testing Design
An A/B test was designed for a new customer retention strategy. The idea is to introduce a new feature or service for a subset of customers and compare their churn rate with the rest of the customers. The results of the A/B test can be analyzed using a chi-square test for independence.

## :detective: Trends and Anomalies
The target variable 'churned' is balanced, which is good for model training.
There were missing values in the 'product_owned' and 'competitor_product_owned' columns, which were handled by imputation.
The numerical variables are not normally distributed, which could be addressed in a more advanced analysis by applying transformations.
The categorical variables do not have high cardinality or rare labels, which simplifies the preprocessing steps.
## :rocket: Future Work
There is room for improvement in the model's performance. Future work could involve trying different models, tuning model parameters, applying transformations to the numerical variables, and performing feature engineering. The A/B test design could also be implemented and the results analyzed to inform the customer retention strategy.

## :memo: Conclusion
This analysis provides a deep understanding of the different segments of customers and can help in tailoring the approach to each segment and iterating on the strategies. The findings from this analysis can be used to inform decisions on customer acquisition and retention.
