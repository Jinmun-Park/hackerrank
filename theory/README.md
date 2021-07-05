# Knowledge Recap
[Youtube_Starquest][Starquest] <br/>

## Topic 1 : Fundamental knowledge Recap
### PART 1 : P-Value
The area under the curve indicates the probability that a person will have a height within a range of possible values
To calculate p-values, you add up the percentages of areas under the curve, including left and right

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

## Topic 2 : Regression

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

### PART 4 : Elastic Net
If we have a model that includes tons of data.

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/009_ridge.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/010_ridge.PNG" width="450" height="250">

Hyrid Elastic-Net regression is good at dealing with situations when there are correlations between paramenters. This is because ;
* Lasso tends to pick just one of the correlated terms and eliminate the others
* Ridge tends to shrink all of the parameters for the correlated variables together.

By combining Lasso and Ridge shrinks the parameters associated with the correlated variables or remove them at once.


## Topic 3 : Clustering 

***

### 1. PCA 

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

## Topic 4 : Machine Learning Fundamental 

### PART 1 : Confusion Matrix

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_mlfundamental.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_mlfundamental.PNG" width="450" height="250">

<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/003_mlfundamental.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/004_mlfundamental.PNG" width="450" height="250">
***

### PART 2 : Gradient Descent
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

[Starquest]:https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw
