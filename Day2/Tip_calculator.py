print("Welcome to the Tip Calculator\U0001F603")
total_amount=float(input("Enter the total amount :$"))

percentage=int(input("How many percentage do you want to give tip ?(example 10,12,30)\n"))

split_by_people=int(input("How many people to split the amount ?\n"))

each_person_amount=((total_amount*(percentage/100)+total_amount)/split_by_people)

print(f"Each person will give ${each_person_amount} \U0001f600")

