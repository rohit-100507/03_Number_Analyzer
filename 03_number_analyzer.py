total_num = int(input("Enter Total Number To Check: "))
print("=" * 30)

even_count = 0
odd_count = 0

largest = 0
smallest = 0

addition = 0

i = 0

while i < total_num:
    number = int(input("Enter Number : "))

    if number % 2 == 0:
        print("Number is EVEN")
        print("==============")
        even_count += 1

    else:
        print("Number is ODD")
        print("==============")
        odd_count += 1

    if i == 0:
        largest = number
        smallest = number

    if largest < number:
        largest = number

    if smallest > number:
        smallest = number

    addition += number

    i += 1


print("\n" + "=" * 50)
print("              RESULT")
print("=" * 50)

print("Even Count     : ",even_count)
print("Odd Count      : ",odd_count)

print("Largest Number : ",largest)
print("Lowest Number  : ",smallest)

print("Total Sum      : ",addition)
print("Average        : ",addition / total_num)
