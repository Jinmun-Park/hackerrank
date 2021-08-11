# URL
### Youtube
[Youtube_Starquest][Starquest] <br/>

### Fundamental Thetories
[Big_data][Big_data] <br/>
[CRISP_DM][CRISP_DM] <br/>
[Normal_Distribution][Distribution_Usage] <br/>
[Logistic_Pro_Cons][Logistic_Pro_Cons] <br/>
[Boosting vs Bagging][boosting and bagging] <br/>
[Deeplearning vs machinelearning][Deeplearning vs machinelearning] <br/>
[Error_Metrics][Error_Metrics] <br/>
[Confusion_Metrics][Confusion_Metrics]

### Questions & Answers
[Q&A_collection][A_collection] <br/>
[Q&A_collection_2][B_collection] <br/>
[Q_collection][collection] <br/>
[Data Engineer][Data Engineer] <br/>
### Dimension Reduction
[PCA][PCA_Usage] <br/>

### Algorithm
[MLP][MLP_Usage] <br/>
[XGBoost_summary][XGboost] <br/>
[XGBoost_classification][XGboost_classification] <br/>
[KNN][KNN_Usage] <br/>
[KNN_Pro_Cons][KNN_Pro_Cons] <br/>
[Hyperparameter][Hyperparameter] <br/>
[GridSearch][GridSearch] <br/>
[GradientBoosting][Gridentboosting] <br/>
[PCA_Korean][PCA_Korean] <br/>
[Gradient_Descent][Gradient_Descent] 

### Neural Network
[ActivationFunction][ActivationFunction]

# Topic 1 : Fundamental knowledge Recap

***

### PART 1 : P-Value
The area under the curve indicates the probability that a person will have a height within a range of possible values
To calculate p-values, you add up the percentages of areas under the curve, including left and right

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_pvalue.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_pvalue.PNG" width="450" height="250">

***

### PART 2 : Central Limit Theorem
In statistics, we collect more means from more samples, these means will be 'normally distributed.' <br/>
* 0.273 is the likelihood p=0.5 given that 4 out of 7 people would randomly prefer orange juice

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_clt.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_clt.PNG" width="450" height="250">

***

### PART 3 : Maximum Likelihood
In statistics, maximum likelihood estimation (MLE) is a method of estimating the parameters of a statistical model given observations, by finding the parameter values that maximize the likelihood of making the observations given the parameters. <br/>

Logistic Regression uses Maximum Likelihood. <br/>
* 0.273 is the likelihood p=0.5 given that 4 out of 7 people would randomly prefer orange juice

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_mxl.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_mxl.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_mxl.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_mxl.PNG" width="450" height="250">

***

### PART 4 : Cross-Validation
Cross validation allows us to compare different machine learning methods and get a sense of how well they will work in practice.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_cv.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_cv.PNG" width="450" height="250">

***

### PART 5 : Overfitting
Cross validation allows us to compare different machine learning methods and get a sense of how well they will work in practice.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_ml.PNG" width="450" height="250"> 

***

### PART 6 : Error metrics
https://www.jedox.com/en/blog/error-metrics-how-to-evaluate-forecasts/


### PART 7 : Standard & MaxMin scaler
StandardScaler removes the mean and scales the data to unit variance. However, the outliers have an influence when computing the empirical mean and standard deviation which shrink the range of the feature values as shown in the left figure below. Note in particular that because the outliers on each feature have different magnitudes, the spread of the transformed data on each feature is very different: most of the data lie in the [-2, 4] range for the transformed median income feature while the same data is squeezed in the smaller [-0.2, 0.2] range for the transformed number of households. <br/>

StandardScaler therefore cannot guarantee balanced feature scales in the presence of outliers. <br/>

MinMaxScaler rescales the data set such that all feature values are in the range [0, 1] as shown in the right panel below. However, this scaling compress all inliers in the narrow range [0, 0.005] for the transformed number of households.<br/>

Both StandardScaler and MinMaxScaler are very sensitive to the presence of outliers.

# Topic 2 : Regression

***

### PART 1 : Linear Regression
Use a linear squares to fit a line to the data. 
1. First, we calculate the `least squared errors`
2. Then we measure `R squares` : 
  For example, X is mouse weight Y is Mouse size. <br/>
  R-square tells us how much of the variation in mouse sizes can be explained by taking mouse weight into account
  
* R-Square : <img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cfrac%7BVar%28mean%29-Var%28Fit%29%7D%7BVar%28mean%29%7D%20%2C%20%20%201-%20%5Cfrac%7BUnexplained%20variation%7D%7BExplained%20Variation%7D%20%20&bc=White&fc=Black&im=gif&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \frac{Var(mean)-Var(Fit)}{Var(mean)} ,   1- \frac{Unexplained variation}{Explained Variation}  " width="421" height="47" />

***

### PART 2 : Ridge Regression
Lets say we have two variables and we run linear regression. If we have limited data and our linear line may be overfitting but high variance.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_ridge.PNG" width="450" height="250">

We add Weight into regression makes our regression adding bias. In Ridge regression, size of lambda matters to the weight bias on our regression.

* lambda : Postive infinite value. We determine lambda using Cross-Validation which results in the lowest variance.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_ridge.PNG" width="450" height="250">

Least squares cannot find the minimal sum of squared residuals if there are lack of data for a given variables. However, Ridge can help this by :
1. Cross Validation
2. Ridge Regression Penalty (Weight)

***

### PART 3 : Lasso Regressio
Lasso Regression is similar to Ridge, but very important difference.

* Formula adds an absolute value ahead.
* Just like Ridge, Lasso also contains all of the estimated parameters except y-intercept

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_ridge.PNG" width="450" height="250">

The biggest difference is :
* Ridge can only shrink the slope  asymptotically close to 0.
* Lasso can shrink all the slope to 0.

Lasso can exclude useless variables from equation. It is better than Ridge at reducing the variance that contains alot of useless variables.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/007_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/008_ridge.PNG" width="450" height="250">

***

### PART 4 : Elastic Net
If we have a model that includes tons of data.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/009_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/010_ridge.PNG" width="450" height="250">

Hyrid Elastic-Net regression is good at dealing with situations when there are correlations between paramenters. This is because ;
* Lasso tends to pick just one of the correlated terms and eliminate the others
* Ridge tends to shrink all of the parameters for the correlated variables together.

By combining Lasso and Ridge shrinks the parameters associated with the correlated variables or remove them at once.

***

### PART 5 : Naive Bayes

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_naive.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_naive.PNG" width="450" height="250">

Hyrid Elastic-Net regression is good at dealing with situations when there are correlations between paramenters. This is because ;
* Lasso tends to pick just one of the correlated terms and eliminate the others
* Ridge tends to shrink all of the parameters for the correlated variables together.

By combining Lasso and Ridge shrinks the parameters associated with the correlated variables or remove them at once.

***

# Topic 3 : Clustering 

***

### 1. PCA 
[PCA][PCA_Usage] <br/>
A PCA plot converts the correlations among all of the cells(features) into a 2D-graph.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_pca.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_pca.PNG" width="450" height="250">

1. Look at datasets with 2 genes.(X:Gene1, Y:Gene2). Then, we calculate the center of the data.
2. Shift the data to the center, origin (0,0).
3. Draw a random line on the origin and project data onto it.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_pca.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_pca.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_pca.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_pca.PNG" width="450" height="250">

4. We measure sum of squared distance, SS(Distance), to remove negative values.
5. Rotate lines on origin untill we end up with the line with the largest SS(Distnace)
6. This is PC1. Hence, PC1 is linear combination of given variables. 
7. PC2 is simply the line through the origing that is perpendicular to PC1.
8. Rotate PC1 and PC2 as PC1 is on horizontal line.Then we use projected lines to find where samples go in PCA Plot.
9. This is Singular Value Decomposition (SVD)

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/007_pca.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/008_pca.PNG" width="450" height="250">

What if we have 3 variables to be in PCA Plot?
1. We calculate principal componetst 
2. With the eigenvalues, we determines 2D-graph
3. Draw 2D graph with the data 

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/009_pca.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/010_pca.PNG" width="450" height="250">

***

### 2. KNN 

[KNN_URL][KNN_Videos]

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_knn.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_knn.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_knn.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_knn.PNG" width="450" height="250">

***

# Topic 4 : Machine Learning Fundamental 

### PART 1 : Confusion Matrix

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_mlfundamental.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_mlfundamental.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_mlfundamental.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_mlfundamental.PNG" width="450" height="250">

***

### PART 2 : ROC&AUC
In this example, we use logistic regression to build ROC & AUC. Confusion matrix matters in each threshold as it results large number of confusion matrix.
1. ROC graph summarizes all of the confusion matrices that each threshold produced. 
2. AUC helps you decide which categorization method is better. Its same as ROC

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_roc.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_roc.PNG" width="450" height="250">

***

### PART 3 : Gradient Descent
Gradient Descent can optimize all these things ;
* We fit a line with linear regression to optimize the intercept and slope.
* We use logistc regression to optimize squiggle
* We use t-SNE to optimize cluster

1. We find intercept using gradient descent and move our intercepts to get different sum of squared residuals. <br/>

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_gradientdescent.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_gradientdescent.PNG" width="450" height="250">

2. Gradient descent does a few calculations far from the optimal solution. Then, it increases the number of calculations closer to the optimal value. Gradient descent finds
the minimum value by taking steps from an initial guess unitll it reaches the best value.<br/>

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_gradientdescent.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_gradientdescent.PNG" width="450" height="250">

3. To recap, we use the sum of squared residuals as 'residuals' to evaluate how well a line fits the data. Then, we derivate it.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_gradientdescent.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_gradientdescent.PNG" width="450" height="250">

***

### PART 4 : Prune

In this example, we use simple tree to understand Prune. <br/>
Outliers in our tree makes overfits the regression tree. So we replace the split with a leaf that is the average of outliers <br/>

* The point is, how do we decide which tree tou use ? 

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_prune.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_prune.PNG" width="450" height="250">

Cost complexity pruning is to calculate the sum of squared residuals for each tree.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_prune.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_prune.PNG" width="450" height="250">

We calculate tree scores by adding, Tree Complex Penalty. Which results the more trees, more penalty.Then how do we find alpha value ?
1. We use all the data (training + test) to build regression tree.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_prune.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_prune.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/007_prune.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/008_prune.PNG" width="450" height="250">

***


# Topic 5 : Machine Learning

***

### PART 1 : Gradient Boosting (Continuous Value)

Gradient boost is used to predict a continuous value.
1. Gradient boost starts by making a single leaf, instead of tree. The leaf represents an initial guess for the weight of all samples. The first guess is the average value.
2. Then we builds a tree. 
3. Gradient boost scales all trees by the same amount.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_gradientboost.PNG" width="450" height="250">

4. Calculate the residuals on leaf with its average.
5. Predict values by plus the residuals.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_gradientboost.PNG" width="450" height="250">

6. Gradient boost deals with overfitting using learning rate (0~1). We scale them using learning rate.
7. We are making trees untill we reach maximum specified.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_gradientboost.PNG" width="450" height="250">

***

### PART 2 : Gradient Boosting (Regression)
Loss function is just something that evaluates how well we can predict Y. Loss function is sum of squared residuals.

1. The derivation in equation results to the average

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/007_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/008_gradientboost.PNG" width="450" height="250">

2. The steps are complicated to make a summary here. 

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/009_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/010_gradientboost.PNG" width="450" height="250">

***

### PART 3 : Gradient Boosting (Classification)

When we use gradient boost for classification, the initial prediction for every individual is the log. <br/>
NOTE : 0.5 is very common threshhold for making classification decisions based on probability.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/011_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/012_gradientboost.PNG" width="450" height="250">

We cannot just add them to get prediction because our inputs were logged at the ifrst time. So we use the formula to get the output. We use learning rate (Commonly 0.1).

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/013_gradientboost.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/014_gradientboost.PNG" width="450" height="250">


***

### PART 4 : SVM
#### SVM can handle outliers

Lets understand the marign ;
1. When we use the threshold that gives the larges marign, its called Maximal Marginal Classifier.
2. However, Maximal Margin Classifier is very sensitive to outliers.
3. To resolve this, we have to allow misclassification. Then we called Soft Margin

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_svm.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_svm.PNG" width="450" height="250">

4. We use cross validation to determine how many misclassification and observations to allow inside soft margin.
5. Soft Vector Classifier comes from the fact that the observation is on the edge and within soft margin.
6. When data are 4 or more dimensions, SVC (Classification) is hyperplane. 
7. SVM overcomes the data problem that SVC cannot solve.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_svm.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_svm.PNG" width="450" height="250">

8. SVM overcomes the data problem that SVC cannot solve.
9. First, SVM starts with lo dimension. Second, moves data into higher dimension. Then, find SVC.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_svm.PNG" width="450" height="250">

***

### PART 5 : Randome Forest
#### Bagging

1. Create bootstrap dataset. Bootstrap is randomly selected from original dataset.
2. But we only use a random subset of variables at each step

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_rf.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_svm.PNG" width="450" height="250">

3. Repeat the work.
4. Impute the output data into trees we builts.

* Bagging : Bootstrap data with aggregation.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_rf.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_svm.PNG" width="450" height="250">

5. How do we know this model is good. We are using out-of-bag data, data that is not included in bootstrap data,

***

### PART 6 : XGboost
#### It was designed to use in large data, complicated data sets.
#### XGboost uses unique regress tree

#### Hyperparameter : https://www.kaggle.com/felipefiorini/xgboost-hyper-parameter-tuning
1. We get an averge as our initial prediction. 
2. Every tree starts out with a single leaf and we calculate 'Similarity Score.' A single leaf stores all residuals.
3. Labmda is regularization parameter
4. Then we move one step next to measure similarity scores. Then we measure 'gain score.'
5. We repeat till we shift our threshold is over in our tree and get all 'gain scores.'

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_xgb.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_xgb.PNG" width="450" height="250">

6. We choose the best gain threshold.
7. Then we continue spilit threshold one after to get the best gain.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_xgb.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_xgb.PNG" width="450" height="250">

8. Now we have to talk about 'prune'
9. We do this by deducting 'gamma' to our similarity scores.
10. Lambda is intended to reduce the prediction's sensitivity to individual observations.
11. 
<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/005_xgb.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/006_xgb.PNG" width="450" height="250">



[Starquest]:https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw
[PCA_Usage]:https://www.analyticsvidhya.com/blog/2016/03/pca-practical-guide-principal-component-analysis-python/
[MLP_Usage]:https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
[KNN_Videos]:https://www.youtube.com/watch?v=4HKqjENq9OU&ab_channel=Simplilearn
[Distribution_Usage]:https://rpubs.com/Statdoc/204929
[XGboost]:https://blog.naver.com/PostView.naver?blogId=ollehw&logNo=222107432424&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=false&from=postView
[collection]:https://lifeofdori.tistory.com/14
[A_collection]:https://yongwookha.github.io/MachineLearning/2021-01-29-interview-question
[KNN_Usage]:https://blog.naver.com/jaehong7719/221924486981
[Hyperparameter]:https://machinelearningmastery.com/hyperparameters-for-classification-machine-learning-algorithms/
[GridSearch]:https://www.mygreatlearning.com/blog/gridsearchcv/
[Gridentboosting]:https://blog.naver.com/jaehong7719/221950378451
[Logistic_Pro_Cons]:https://www.geeksforgeeks.org/advantages-and-disadvantages-of-logistic-regression/
[KNN_Pro_Cons]:https://dhirajkumarblog.medium.com/top-4-advantages-and-disadvantages-of-support-vector-machine-or-svm-a3c06a2b107
[boosting and bagging]:https://blog.naver.com/ilovelatale/222320553535
[Deeplearning vs machinelearning]:https://blog.naver.com/jalhaja0/222144933457
[Error_Metrics]:https://partrita.github.io/posts/regression-error/
[ActivationFunction]:https://blog.naver.com/wogjs7147/222430756533
[XGboost_classification]:https://www.kaggle.com/lucidlenn/data-analysis-and-classification-using-xgboost
[Confusion_Metrics]:https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
[Data Engineer]:https://ko.myservername.com/top-29-data-engineer-interview-questions
[B_collection]:https://shelling203.tistory.com/35
[Big_data]:https://blog.naver.com/thebaleuncoding/222429049541
[CRISP_DM]:https://blog.naver.com/ji_sung31/222404174799
[PCA_Korean]:https://heung-bae-lee.github.io/2020/04/03/machine_learning_07/
[Gradient_Descent]:[Gradient_Descent]
