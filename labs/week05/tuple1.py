#tuple1
#author: PaulMcGrath
# jus messing with Tuples
# once start the tuple can continue tuple indexes in a new line without issue
months = ("January",
 "February",
  "March" , "April" , "May",
   "June" , "July" , "August" , "September" ,
    "October" , "November" , "December")
submonths = months [1:8]
 # submonths for [1:7] defined as indexes 1 (2nd in list i.e. Feb up to but not including index 7 (i.e. Jul but not Aug)
for month in submonths:
     print (months)
     # it doesnt matter if you say 'for month in months' or 'for months in months' 
     # but if you say for month in submonths: print (months) it prints the integer value of 'for month in submonths' i.e. 6
     #i.e. it prints 6 lines of the complete index set (Jan..Dec)
     # if chsnge submonths = months [-1:]  and then for month in submonths: print (months)  it prints 1 line (Jan.. Dec)
