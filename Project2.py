import numpy as np
from datetime import datetime
from scipy.stats import chisquare
from scipy.stats import gamma
import math

# # Start of Arrival data
# # read data from a file
# # assuming files are in format requested in project pdf
# # first line is names of team members
# # second line is date the data was collected
# # third line is time the data was collected (start-end)
# # forth line is the station (arrival,order,payment,pickup)
# # fifth line is arrival and departure headings
# # six line and on are the times
# arrivalTimes = []  # array of arrival time data from file (string)
# with open('Project2 Data/Arrival_Roselius.csv', 'r') as infile:
#     numIgnore = 5  # ignore the first five lines of the file
#     for value in infile.readlines():
#         if numIgnore <= 0:
#             value = value.strip("\n")  # there was an extra new line after every line in my file
#             value = value.strip(",")  # there was a bunch of commas after every time in my file
#             arrivalTimes.append(value)
#         else:
#             numIgnore -= 1
#     infile.close()
#
# # calculate values
# s = []  # array of interarrival time data calculated (minutes)
# length = len(arrivalTimes) - 1  # length of array -1 because index starts at 0
# i = 0
# while i < length:
#     d = datetime.strptime(arrivalTimes[i + 1], "%H:%M:%S") - datetime.strptime(arrivalTimes[i], "%H:%M:%S")
#     tD = d.seconds / 60
#     s.append(tD)
#     i += 1
#
# # generate a histogram
# import matplotlib.pyplot as plt
# numBins = 5
# count, bins, ignored = plt.hist(s, numBins, density=True, align='mid')
# print("bins: ", bins)
#
# # superimpose a exponential distribution pdf
# x = np.linspace(min(bins), max(bins), numBins)
# lam = 1
# pdf = (np.exp(-x / lam) / lam)
# plt.plot(x, pdf, linewidth=2, color='r')
#
# # estimate parameters from data
# n = 0
# sum = 0
# for v in s:
#     sum += v
#     n += 1
# lam = sum / n
# x = np.linspace(min(bins), max(bins), numBins)
# pdf = (np.exp(-x / lam) / lam)
# plt.plot(x, pdf, linewidth=2, color='y')
# # end of Arrival data

# # Start of Order data
# # read data from a file
# # assuming files are in format requested in project pdf
# # first line is names of team members
# # second line is date the data was collected
# # third line is time the data was collected (start-end)
# # forth line is the station (arrival,order,payment,pickup)
# # fifth line is arrival and departure headings
# # six line and on are the times
# arrivalTimes = []  # array of arrival time data from file (string)
# departTimes = []  # array of depart time data from file (string)
# with open('Project2 Data/Order_Roselius.csv', 'r') as infile:
#     numIgnore = 5  # ignore the first five lines of the file
#     for value in infile.readlines():
#         if numIgnore <= 0:
#             value = value.strip("\n")  # there was an extra new line after every line in my file
#             value = value.strip(",")  # there was a bunch of commas after every time in my file
#             value = value.split(",")
#             arrivalTimes.append(value[0])
#             departTimes.append(value[1])
#         else:
#             numIgnore -= 1
#     infile.close()
#
# # calculate values
# s = []  # array of mean order time data calculated (minutes)
# length = len(arrivalTimes) - 1  # length of array -1 because index starts at 0
# i = 0
# while i < length:
#     d = datetime.strptime(departTimes[i], "%H:%M:%S") - datetime.strptime(arrivalTimes[i], "%H:%M:%S")
#     tD = d.seconds / 60
#     s.append(tD)
#     i += 1
#
# # generate a histogram
# import matplotlib.pyplot as plt
# numBins = 10
# count, bins, ignored = plt.hist(s, numBins, density=True, align='mid')
#
# # superimpose a gamma distribution pdf
# x = np.linspace(min(bins), max(bins), numBins)
# alpha = .5
# pdf = gamma.pdf(x, alpha)
# plt.plot(x, pdf, linewidth=2, color='r')
#
# # estimate parameters from data
# alpha = gamma.fit(s)[0]
# x = np.linspace(min(bins), max(bins), numBins)
# pdf = gamma.pdf(x, alpha)
# plt.plot(x, pdf, linewidth=2, color='y')
# # end of Order data

# # Start of Payment data
# # read data from a file
# # assuming files are in format requested in project pdf
# # first line is names of team members
# # second line is date the data was collected
# # third line is time the data was collected (start-end)
# # forth line is the station (arrival,order,payment,pickup)
# # fifth line is arrival and departure headings
# # six line and on are the times
# arrivalTimes = []  # array of arrival time data from file (string)
# departTimes = []  # array of depart time data from file (string)
# with open('Project2 Data/Payment_Roselius.csv', 'r') as infile:
#     numIgnore = 5  # ignore the first five lines of the file
#     for value in infile.readlines():
#         if numIgnore <= 0:
#             value = value.strip("\n")  # there was an extra new line after every line in my file
#             value = value.strip(",")  # there was a bunch of commas after every time in my file
#             value = value.split(",")
#             arrivalTimes.append(value[0])
#             departTimes.append(value[1])
#         else:
#             numIgnore -= 1
#     infile.close()
#
# # calculate values
# s = []  # array of mean order time data calculated (minutes)
# length = len(arrivalTimes) - 1  # length of array -1 because index starts at 0
# i = 0
# while i < length:
#     d = datetime.strptime(departTimes[i], "%H:%M:%S") - datetime.strptime(arrivalTimes[i], "%H:%M:%S")
#     tD = d.seconds / 60
#     s.append(tD)
#     i += 1
#
# # generate a histogram
# import matplotlib.pyplot as plt
# numBins = 5
# count, bins, ignored = plt.hist(s, numBins, density=True, align='mid')
#
# # superimpose a lognormal distribution pdf
# x = np.linspace(min(bins), max(bins), numBins)
# mu, sigma = -0.05, 0.5  # mean and standard deviation
# pdf = (np.exp(-(np.log(x) - mu) ** 2 / (2 * sigma ** 2))
#        / (x * sigma * np.sqrt(2 * np.pi)))
# plt.plot(x, pdf, linewidth=2, color='r')
#
# # estimate parameters from data
# sum = 0
# n = 0
# for v in s:
#     sum = sum + np.log(v)
#     n += 1
# mu = sum / n
# sum = 0
# n = 0
# for v in s:
#     sum = sum + (np.log(v) - mu) ** 2
#     n += 1
# sigma = math.sqrt(sum / n)
# x = np.linspace(min(bins), max(bins), numBins)
# pdf = (np.exp(-(np.log(x) - mu) ** 2 / (2 * sigma ** 2))
#        / (x * sigma * np.sqrt(2 * np.pi)))
# plt.plot(x, pdf, linewidth=2, color='y')
# # end of Payment data

# Start of Pickup data
# read data from a file
# assuming files are in format requested in project pdf
# first line is names of team members
# second line is date the data was collected
# third line is time the data was collected (start-end)
# forth line is the station (arrival,order,payment,pickup)
# fifth line is arrival and departure headings
# six line and on are the times
arrivalTimes = []  # array of arrival time data from file (string)
departTimes = []  # array of depart time data from file (string)
with open('Project2 Data/Pickup_Roselius.csv', 'r') as infile:
    numIgnore = 5  # ignore the first five lines of the file
    for value in infile.readlines():
        if numIgnore <= 0:
            print("Before Strip")
            value = value.strip("\n")  # there was an extra new line after every line in my file
            value = value.strip(",")  # there was a bunch of commas after every time in my file
            value = value.split(",")
            print(value)
            print("After Strip")
            arrivalTimes.append(value[0])
            departTimes.append(value[1])
        else:
            numIgnore -= 1
    print(arrivalTimes)
    print(departTimes)
    infile.close()

# calculate values
s = []  # array of mean order time data calculated (minutes)
length = len(arrivalTimes) - 1  # length of array -1 because index starts at 0
# print("Length: %d" % (length + 1))
i = 0
while i < length:
    d = datetime.strptime(departTimes[i], "%H:%M:%S") - datetime.strptime(arrivalTimes[i], "%H:%M:%S")
    # print("difference: ", d)
    tD = d.seconds / 60
    # print("time: %d" % tD)
    s.append(tD)
    i += 1
# print(s)
# print("Length: %d" % len(s))

# generate a histogram
import matplotlib.pyplot as plt
numBins = 5
count, bins, ignored = plt.hist(s, numBins, density=True, align='mid')
print("bins: ", bins)

# superimpose a exponential distribution pdf
x = np.linspace(min(bins), max(bins), numBins)
lam = 1
pdf = (np.exp(-x / lam) / lam)
plt.plot(x, pdf, linewidth=2, color='r')

# estimate parameters from data
n = 0
sum = 0
for v in s:
    sum += v
    n += 1
lam = sum / n
x = np.linspace(min(bins), max(bins), numBins)
pdf = (np.exp(-x / lam) / lam)
plt.plot(x, pdf, linewidth=2, color='y')
# end of Pickup data

# chi squared
print("Chi squared: ", chisquare(count, pdf))

plt.axis('tight')
plt.show()