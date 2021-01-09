# Given a array of numbers representing the stock prices of a company in 
# chronological order, write a function that calculates the maximum profit 
# you could have made from buying and selling that stock once. You must buy 
# before you can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you 
# could buy the stock at 5 dollars and sell it at 10 dollars.

def calc_max_profit(arr):
    largest = arr[0]
    profit = 0
    max_profit = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            profit = 0
        if arr[i] > arr[i-1]:
            bigger = max(arr[i], largest)
            profit += arr[i] - arr[i-1]
            if bigger == arr[i]:
                max_profit = max(max_profit+arr[i]-largest,profit)
                largest = arr[i]
            else:
                max_profit = max(max_profit, profit)
                if max_profit == profit:
                    largest = arr[i]
    return max_profit
    
import random

arr = []
for i in range(10):
    arr.append(random.randint(1,99))
print(arr)
print(calc_max_profit(arr))