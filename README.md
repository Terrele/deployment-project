# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
Predict whether application forms will have student loans or not.

## Hypothesis
1. If the applicant has returned a loan before, they are more likely to get a loan.
2. If the applicant has a higher education level, they are more likely to get a loan.
3. Gender may or may not affect applicants.
4. Applicants with a good credit score are more likely to get a loan.
5. Applicants with high income are more likely to get a loan.

## EDA 
Applicants that have better education have higher income.
Applicants that have better education also receive bigger loan amounts.
There are significantly more male than female applicants and many that are not self employed.
Many applicants have already graduated.
Males generally have higher loan amounts.
The number of dependents will increase loan amounts as well as being self employed.



## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
1. Check if there was data imbalancing.
2. Check what variables can affect loan status and the amount.
3. Check for outliers. Since the histograms are skewed, it is better to use the median for numerical values.
4. Use the mode for categorical NaN values.
5. Create new features such as the total or taking the log of some other features to remove outliers.
6. Use a logistic regression model since our predicted response is yes or no.
7. Use an accuracy and F1 score to show how good the model is.
8. Use a grid search to tweak the parameters to find a better fit for the model.
9. Use pipelines to make the code easier to maintain, visualize, and to deploy.
10. Push the model onto the cloud using AWS.


## Results/Demo
Using a logistic regression model, found an 82% accuracy on the train and 80% on the testing data. The F1 score is at 86.5%. Using a grid search, the same results were found and there wasn't any improvement.
Put the model into a pipeline to make it easier to work with.

## Future Goals
I would do more data cleaning and visualizations to get better predictions before I start modelling. I would also try out different models to help improve my accuracy on the testing data.