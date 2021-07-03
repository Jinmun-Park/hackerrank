# Knowledge Recap

## Quick Recap for the basic statistic knowledges
***
### 1. P-Value
The area under the curve indicates the probability that a person will have a height within a range of possible values
To calculate p-values, you add up the percentages of areas under the curve, including left and right

### Cross-Validation
Cross validation allows us to compare different machine learning methods and get a sense of how well they will work in practice.
<img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/001_cv.PNG" width="450" height="250">  <img src="https://github.com/Jinmun-Park/hackerrank/blob/main/theory/images/002_cv.PNG" width="450" height="250">

### Linear Regression
Use a linear squares to fit a line to the data. 
1. First, we calculate the `least squared errors`
2. Then we measure `R squares` : 
  For example, X is mouse weight Y is Mouse size. <br/>
  R-square tells us how much of the variation in mouse sizes can be explained by taking mouse weight into account
  
* R-Square : <img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cfrac%7BVar%28mean%29-Var%28Fit%29%7D%7BVar%28mean%29%7D%20%2C%20%20%201-%20%5Cfrac%7BUnexplained%20variation%7D%7BExplained%20Variation%7D%20%20&bc=White&fc=Black&im=gif&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \frac{Var(mean)-Var(Fit)}{Var(mean)} ,   1- \frac{Unexplained variation}{Explained Variation}  " width="421" height="47" />

## PCA Basic Idea 
[Youtube_Starquest][PCA] <br/>
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

[PCA]: https://www.youtube.com/watch?v=FgakZw6K1QQ&ab_channel=StatQuestwithJoshStarmer
***
