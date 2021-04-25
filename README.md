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



PROJECT PAGES:

CD..#
Project: Make a project that will analyse the iris data set, this project is worth 50% of your grade for this course.


Initial project plan:

Week1: 
1. Reseaarch Iris Dataset- complete
2. Get Iris DataSet (download to readme) -complete
3. Research PANDAS- do the week 11. Research external sources-complete
4. Create a test file similar to fisdher data set and start to 'play' with it- record learnings for readme -ongoing
5. Research websites/forums on ways to analyze the dataset- complete
6. Decision on final plan: MyAnalysis Plan- what attributes will be analysed/ how it will be presented/what histograms/ what are x & y for scattterplots (loook for correlations)- complete
7. Research examples of python code to analyse data (Fisher data set or similar), code repositories, python forums- 05 Apr- ongoing .  reference file created
Week 2:
8. Begin writing the code: -05 Apr started.
9. Pull the data set to VSC file (text file?)-completed
10. Write program to error check
11. Create a simpler data set file to check
12. Write program to:
13. pull the data set-complete
14. Write python program to define: analyse the data
Week 3:
15. Write python program to create histograms- ongoing
16. Write python program to create scatter=plots-ongoing
17. Run program-ongoing
18. Degbug
Week 4: 
19. Look for ways to make code more elegant
20. Create screenshots of histograms/scatterplots
21. Paste screenshots to repository 
22. Update ReadMe file
Week 5: contingency


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

Project Plan:

adapted from 'How to write an Algorithm'

1. Identify the Inputs
2. Identify the Processes
3. Identify the Outputs
4. Develop a HIPO Chart

Step 1: identify the data:
  Project goal: Write s program to analyse the Fisher (Anerson) Dataset 
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

STEP 4: DEVELOP A HIPO CHART
- Hierarchy of Inputs, Processes and Outputs
- Used to develop requirements, construct the design, and support implementation
- Break the problem into smaller more manageable parts (i.e. Divide and Conquer)
- What inputs do the modules need?
- What processes need to happen in the modules?
- What outputs are produced by the modules?