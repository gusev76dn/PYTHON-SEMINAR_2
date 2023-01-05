# Напишите программу, которая принимает на вход большое число и показывает его цифру.

num = float(input())
sum_digits = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum_digits += num % 10
    num //= 10
print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))