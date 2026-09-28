first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

if ((first_letter > second_letter and first_letter < third_letter) or
    (first_letter < second_letter and first_letter > third_letter)):
    print(f"The letter in the middle is {first_letter}")

elif ((second_letter > first_letter and second_letter < third_letter) or
      (second_letter < first_letter and second_letter > third_letter)):
    print(f"The letter in the middle is {second_letter}")

else:
    print(f"The letter in the middle is {third_letter}")