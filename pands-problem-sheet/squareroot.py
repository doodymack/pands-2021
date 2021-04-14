# squareroot.py
# Author: Paul Mc Grath
# asks for input - calculates the square rot using newtonian method

#Given an integer N and a tolerance level L, the task is to find the square root of that number using Newton’s Method.

#Newton’s Method:
# Let N be any number then the square root of N can be given by the formula:
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.



#In the above formula, X is any assumed square root of N and root is the correct square root of N.
#Tolerance limit is the maximum difference between X and root allowed.
#Approach: The following steps can be followed to compute the answer:

#Assign X to the N itself.
#Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
#Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root 
# and continue.
#If the calculated root comes inside the tolerance allowed then break out of the loop.
#Print the root.
 
def squareRoot(n, l) : 
  
    # Assuming the sqrt of n as n only  
    x = n  
  
    # To count the number of iterations  
    count = 0 
  
    while (1) : 
        count += 1 
  
        # Calculate more closed x  
        root = 0.5 * (x + (n / x))  
  
        # Check for closeness  
        if (abs(root - x) < l) : 
            break 
  
        # Update root  
        x = root 
  
    return root  
  
# Driver code  
if __name__ == "__main__" :  
  
    n = float(input(" Please enter a positive number : "))
    l = 0.00001
  
    print ("The Squareroot of {} is approximately {}" .format(n,(squareRoot(n, l))))