# normalise
# #author: paul mc grath
#  This program reads a string and strips
# any leading or trailing spaces
# It also converts all the letters to lower case
# this program also outputs the length of the original string
# and the normal one

rawString = input( " please enter a string ")
normalizedString = rawString.strip() .lower()

lengthOfRawstring = len(rawString)
lengthOfNormalizedString = len(normalizedString)

print ("That string normalized is :{}" .format (normalizedString))
print ("The length of the rawstring is :{}" .format (lengthOfRawstring))
print ("That string normalized is :{}" .format (lengthOfNormalizedString))