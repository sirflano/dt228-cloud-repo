

class readin:
  #read in string
  teBeChecked = input("Input string to be checked please: ")
  #strip string of whitespace
  teBeChecked = teBeChecked.replace(" ", "")
  #copy a reverse of the sting
  tempString = teBeChecked[::-1]

  #check if the strings are the same, print result
  if teBeChecked == tempString:
    print("True")
  else:
    print("False")


