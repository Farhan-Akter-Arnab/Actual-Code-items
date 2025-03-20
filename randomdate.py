import random
import time
def getRandomDate(startDate, endDate):
    print("Printing random date between ", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2020" , "12/31/2024"))