# pands-2021
this is my read me file
#The readme file.#For telling users what this repository is for.


List of references used in the weekly problems and general further reading from weekly lectures and labs (Note- 'Automate the boring stuff with Python' was printed -all 480 pages enabled by work printer-I found this a good read when sick of screentime and/or internet is down):

weekday.py:
https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python
https://www.w3schools.com/python/python_datetime.asp
 
squareroot.py
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

secondstring.py
https://www.w3schools.com/python/python_howto_reverse_string.asp
https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220

pythoncollatz.py
https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/

How_Many_E.py
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
https://pythonexamples.org/python-count-number-of-characters-in-text-file/

plottask.py
https://www.w3schools.com/python/matplotlib_plotting.asp
https://realpython.com/python-matplotlib-guide/
https://matplotlib.org/stable/
https://github.com/matplotlib/cheatsheets#cheatsheets
https://github.com/pandas-dev/pandas



Pands-Project2021
*****************

What is the Fisher Dataset (Wikipedia): 
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.

The dataset, contains three plant species of iris flower (setosa, virginica, versicolor) and four features measured for each sample. These quantify the morphologic variation of the iris flower in its three species, all measurements given in centimeters.


2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
i.e.for 1.Iris setosa; 2. Iris virginica and 3. Iris versicolor:
measurements of:  sepal length-cm; sepal width-cm; petal length-cm; petal width-c.A 

There are various versions of the data such as:

1. That originally published by Edgar Anderson in 1935 " The irises of the Gaspe Peninsula." Bull.Amer. Iris Soc. 59, 2-5 and reproduced in R. A Fishers seminal paper where the data was analysed using linear discriminatory ana;ysis.
2. Online versions of various form can be found:#
  CSV: https://gist.github.com/curran/a08a1080b88344b0c8a7 or https://www.kaggle.com/uciml/iris
  JSON: https://datahub.io/machine-learning/iris
  

UCI Machine Learning Repository of the Fisher Dataset:  https://archive.ics.uci.edu/ml/datasets/Iris

As can be seen in the pictures in GitHub repository there are similarities in morphology between these species. In the absence of visual information Fisher showed a statistical approach (discriminant function) could itself discriminate between the three species.
The aim of this project was to: 

Research the data set online and write a summary about it in README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
• outputs a summary of each variable to a single text file,
• saves a histogram of each variable to png files, and
• outputs a scatter plot of each pair of variables. 


analysis.py:
************

The program when run:

1. Creates a datframe of an external csv file containign Fishers Iris Dataset
2. Runs analysis on the data set and sub-analysis of the data sliced by species
3. Exports this data to a text file "SummaryOfEachVariable.txt"
4. Creates a histogram of each variable- plots visually shown when run
5. Copies of each histogram are exported as .png images for further use
6. Creates a correlation analysis of each pair of attributes:
    SL-SW
    SL-PL
    SL-PW
    SW-PL
    SW-PW
    PL-PW
7. Each correlation contains the three species- thus allowing to determine if there are correlations (visual)

references at end of README

Summary of analysis:
********************
********************

Review of Histograms:
********************

Iris-Setosa:
************
Attribute     Relative_Spread      SkewLeft      Centered      SkewRight     Comment
*****************************************************************************************
SepalLength       low                                yes
SepalWidth        low               yes                                       One outlier
Petal Length      low               yes                                       one outlier
Petal Width       low                                 yes                     More variability.Some bins empty
                                                                              High Precision

Iris-Versicolor:
****************
Attribute     Relative_Spread      SkewLeft      Centered      SkewRight     Comment
*****************************************************************************************
SepalLength       high                               yes
SepalWidth        high               yes                                      
Petal Length      high               yes                                      
Petal Width       high                                 yes                  Spread left & right
                                                                            No measurements at bin at mean value

Iris-Virginica:
****************
Attribute     Relative_Spread      SkewLeft      Centered      SkewRight     Comment
*****************************************************************************************
SepalLength       med                              yes
SepalWidth        high                             yes                                      
Petal Length      med                                            yes                                      
Petal Width       high                             yes                  
                                                                            
Review of Correlations:
***********************
***********************

Correlation      Iris Setosa      Iris Versicolor      Iris Virginica     Comment
*********************************************************************************

SW-SL            high corr         med corr            med corr           IVE-IVI Data overlap
                                                                          IS data separated from IVE-IVI

SL-PL            low corr           high corr           high corr         IVE-IVI Data overlap
                                                                          IS data separated from IVE-IVI       

SL-PW            low corr           low corr            low corr          IVE-IVI Data overlap
                                                                          IS data separated from IVE-IVI

SW-PL            low corr           low corr            low corr          IVE-IVI Data overlap
                                                                          IS data separated from IVE-IVI

SW-PW            low corr           med corr            med corr          IVE-IVI Data overlap
                                                                          IS data separated from IVE-IVI

PL-PW            high corr          high corr           high corr         IS to IVE-IVI No Data overlap
                                                                          IVE-IVI- practically separated

In summary:
***********

Correlations of the three species using the three measured attributes can be used to diffrentiate from each species.
The correlations of Iris-Setosa betwwen attribues is relatively weak.  Stronger correlations for Iris Versicolor and Iris Virginica.
The relationship of petal length vs petal width show stronger correlations.  In addition this relationship shows a similar slope with a high correlation as viewed in facet plots (r2 not available in seaborn facet.)

For all attributes Iris-Setosa can be separated from the other species owing to the attribute size being much smaller in comparison.
For the majority of measured attributes Iris Versicolor and Iris Virginica data overlap making it more difficult to distinguish using the gathered data.

However all three species can be separated using a plot of petal length vs petal width. If use X axis: PL =0-3 (Iris Setosa), PL= 3-5 (Iris Versicolor), PL >5 (Iris Virginica)

Thus data analysis can be used to analyse measured attribute data for three Iris species. The data can be used to identify the species using correlation analysis of petal length v petal width.



Project Plan:
*************

adapted from 'How to write an Algorithm'

1. Identify the Inputs
2. Identify the Processes
3. Identify the Outputs
4. Develop a HIPO Chart

Step 1: identify the Inputs:
  Project goal: Write a program to analyse the Fisher (Anerson) Dataset 
- What data do I need?
    Fisher dataset
- How will I get the data?
  search online has multiple versions.  Best found was the csv file: iris.csv
- In what format will the data be?
    csv file
STEP 2: IDENTIFY THE PROCESSES
- How can I manipulate data to produce meaningful results?
  The dataset is a csv file.  The task is to execute correltion analysis using python.
  Firstly the data required to be in a format that Python code could be used to analyse i.e. a Dataframe. 
  The initial obvious application was Pandas to convert the csv to a dataframe
  Once a datframe created research ways to execute the following:
    1. Generate a statistical summary data- all
    2. Split the data by flower species
    3. Generate statistical summary data tables per species
    4. Generate histograms of each attribute per species
      - iris-setosa: SL,SW,PL,PW
      - iris-versicolor: SL,SW,PL,PW
      -iris-virginica: SL,SW,PL,PW
    5. Generate visual correlations of attributes (use Seaborn FacetGrid tp plot three species on each plot)
      - sepal length vs sepal width
      - sepal length vs petal length
      - sepal length vs petal width
      - sepal width vs petal length
      - sepal width vs petal width
      - petal length vs petal width

STEP 3: IDENTIFY THE OUTPUTS
-What outputs do I need to return to the user?
  -see above: 1, summary stats tables 2, histograms ,3 correlations (visual)
-What format should the outputs take?
  - a summary of each variable outputted to a single text file (append)
  - a histogram of each variable saved to png files
  - a scatter plot of each pair of variables (as FacetGrid)

STEP 4: DEVELOP A HIPO CHART (Hierarchy of Inputs, Processes and Outputs)
- Break the problem into smaller more manageable parts (i.e. Divide and Conquer):

1. Create Repository on Github
    Pands-project 2021 created.  Pushed regular updates with relevant commit messages.

2. Research Iris Dataset
  A simple google search gave multiple references to various analysis of the dataset. The general information I saved above.  In addition I saved pictures of the three species in my repository.

2. Get Iris DataSet 
  Opensource dasta sets founf text and csv

3. Identify what modules are typically used for dataframe analysis
  PANDAS,MATPLOTLIB,SEABORN,NUMPY

4. Research PANDAS- do the week 11. Research external sources
  Week 11 lessons were a good start. Further research on realpython & W3 schools on modules

5. Create a test file similar to the Fisher data set and start to 'play' with it
  Fisher dats set was ideal. Pandas gives opportunity to analyse by column, species, check for NULL (no NULL), replace Null with Mean or other e.g. df.fillna(x)- not required as Fisher dataset is complete. 

6. Decision on final plan: MyAnalysis Plan- what attributes will be analysed/ how it will be presented/what histograms/ what are x & y for scattterplots.
  Decided to follow project objective i.e. to create a summary of data, backed up by histograms of individual attributes by species, finally a visual correlation analysis

7. Research examples of python code to analyse data (Fisher data set or similar), code repositories, python forums:
   A simple google search gives multiple references to various analysis of the dataset. All tend to use the modules PANDAS,MATPLOTLIP & SEABORN. 
   I trialled various approaches on sample data. Many were more complex than my basis of knowledge. Decision made to keep things simple.  Focus on the objective.  Write the simplest code that delivers on the objective. Once this is shown to work there is always the possibility to revisit the code, look for oppottunity to optimise.
   
8. Begin writing the code
  Analysis.py initiated. Each idea for analysis was added to the script. To test the script the remainder of the file was commented out.  The program was run.  Where there were error codes- debugged by looking for error code onilne (Stackoverflow good resource).  Re-ran piece of code until satisfactory outcome.

9. Create a simpler data set file to check
   python & text files created.  Functions in Python tested.  Test Text file checked periodically.  What was proven to work was pasted to main file "analysis.py"

10. Write python program to define: analyse the data:
    used pandas functions to analyse the dataframe and run stats. The results were sent to an external text file.   The text file starts with an overall summary.
    Therafter the dataset is sliced by species.
    A statistical summary of the sub-dataset was produced using NUMPY and the output exported to the textfile.

15. Write python program to create histograms
  Research showed its possible to create histograms using core python .  However the most appropriaate Python module for histograms was Matplotlib functions

16. Write python program to create scatter plots
    Researching realpython showed  How to visualize data, regression lines, and correlation matrices with Matplotlib
    Numpy also allows correlations.   However I found the best tool to be Seaborn Facetgrid.
    Facetgrid draws multiple instances of the same plot on different subsets of a dataset. This gave visualisations and output closer to the original program objective: " outputs a scatter plot of each pair of variables" while allowing to compare correlations acrss species.

17. Degbug
    To test the script the remainder of the file was commented out.  The program was run.  Where there were error codes- debugged by looking for error code onilne (Stackoverflow good resource).  Re-ran piece of code until satisfactory outcome

19. Look for ways to make code more elegant
    I slimmed down the code by using global variables for species and attribute type.  More automation could be used for sure but this program 'analysis.py' will be run jsut once. If it was required to take in variables or run repeatedly then a more efficient code could be considered.

20. Create screenshots of histograms/scatterplots
    Histograms are output as .png images in Github, or can be reproduced by running the script.

21. Paste screenshots to repository
    Scatterplots are crested by running the script

22. Update ReadMe file
    Created 
    1. Summary of the dataset
    2. Project Summary

23. References:
***************

Python & Iris Dataset:
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/?ref=lbp
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

Petals & Sepals for Iris setosa, Iris versicolor, and Iris virginica (Sources: 1, 2, 3, Licenses: Public Domain, CC BY-SA 3.0 & CC BY-SA 2.0)

Pandas:
#https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html

Matplotlib:
#https://github.com/matplotlib/matplotlib
 
 scatter
 https://www.w3schools.com/python/matplotlib_scatter.asp

 correlations:
 https://datatofish.com/correlation-matrix-pandas/
 https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html

 histograms
 #https://realpython.com/courses/python-histograms/
 #https://www.w3schools.com/python/matplotlib_histograms.asp

 saving files (scatter & histogram)
 https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
 https://futurestud.io/tutorials/matplotlib-save-plots-as-file


 



