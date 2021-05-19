#1.
t = int(input('Please type the temperture'))
V = int (input('Please type 1 for Celsius or 2 for Farenheit'))
if V == 1:
    print("Conversion is " + str(t * 1.8 + 32) + "F")
elif V == 2:
    print("Conversion is " + str((t - 32) * 5/9) + "C")

#2.
def f(number):
    if number % 5 == 0 and number % 3 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("buzz")
    elif number % 5 == 0:
        print("Fizz")
    else:
        print(number)
f(25)

#3.
grades = {'Math': 15,
          'Physics': 11,
          'Geography': 18,
          'History': 20,
          'Geometry': 19}

def result(y):
    grades = y.values()
    total_result = sum(grades)

    if total_result <= 40:
        print('fail')
    elif 41 <= total_result <= 60:
        print('satisfactory')
    elif 61 <= total_result <= 80:
        print(good)
    elif total_result >= 81:
        print('outstanding')
    else:
        print('wrong output')

grades1 = {'Math': 4,
          'Physics': 10,
          'Geography': 9,
          'History': 10,
          'Geometry': 10}
result(grades1)



