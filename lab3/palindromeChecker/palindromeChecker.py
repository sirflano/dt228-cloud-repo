

class readin:
  teBeChecked = input("Input string to be checked please: ")
  teBeChecked = teBeChecked.replace(" ", "")
  tempString = teBeChecked[::-1]
  print(teBeChecked)
  print(tempString)

  if teBeChecked == tempString:
    print("True")
  else:
    print("False")


