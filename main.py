# *******************************/
# * CS03A - Summer 2024
# * Lab 3 - Challenge 2
# * Student Name: Brandon Senaha
# * SID: 20510375
# *******************************/


# main function
# asks integers > calls max function > prints max
def main():

  # ask integer 1
  while True:
    int1 = input('Enter an integer: ')
    if not int1.isdigit():    # if not integer
      print('Please enter an integer.')
      continue
    else:
      int1 = int(int1)  # assign int
      break

  # ask integer 2
  while True:
    int2 = input('Enter another integer: ')
    if not int2.isdigit():    # if not integer
      print('Please enter an integer.')
      continue
    else:
      int2 = int(int2)  # assign int
      break
    

  # call max function
  max_int = max(int1, int2)
  
  # print result
  if not max_int:  # if equal
    print(f'The numbers are equal: {int1} = {int2}')
  else:            # if not equal
    print(f'The maximum of {int1} and {int2} is: {max_int}')


# max function
# returns maximum int or None if equal
def max(num1, num2):
  if num1 > num2:    # if num1 greatest
    return num1
  elif num2 > num1:  # if num2 greatest
    return num2
  else:
    return None      # if equal

# run main
main()
