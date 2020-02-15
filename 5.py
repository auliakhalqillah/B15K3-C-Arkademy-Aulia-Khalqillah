# Function to finde profit maximum
def findHighestProfit(stock):
    maximumprofit = 0
    minimumstock = stock[0]
    for i in range(len(stock)):
        profit = stock[i] - minimumstock
        maximumprofit = max(profit,maximumprofit)
        minimumstock = min(minimumstock,stock[i])

    if (maximumprofit != 0):
        print(maximumprofit)
    else:
        print("Tidak bisa mendapatkan profit pada hari-hari ini")


stock = [10, 2, 11, 20, 3, 5]
stock2 = [33, 29, 11, 3]
findHighestProfit(stock2)
