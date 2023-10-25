numbersFilePath = 'numbers.txt'
numbersArr = []
with open(numbersFilePath, 'r') as file:
    for line in file:
        numbers = line.strip().split(';')
        numbers = [float(num) for num in numbers]
        numbersArr.extend(numbers)
print(sorted(numbersArr, reverse=True)[0])