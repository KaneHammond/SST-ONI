import csv
import sys
import os
import copy
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from datetime import datetime
from scipy import stats
from datetime import date, timedelta
import scipy as sp
import pandas as pd
try:
    import matplotlib.pyplot as plt
except:
    import pip
    pip.main(['install','matplotlib.pyplot'])
    import matplotlib.pyplot as plt
try:
    import numpy as np
except:
    import pip
    pip.main(['install','numpy'])
    import numpy as np
import datetime
#*******************IMPORT DATA********************
#*******************IMPORT DATA********************
#*******************IMPORT DATA********************
sstData = []
inFile = open('SST.csv', 'r') #this just opens the file
theCsvData = csv.reader(inFile)
for aRow in theCsvData:   #This takes the information read from the cvs and creates an index from it
  sstData.append(aRow[:])

#FORMAT
x = []
#Call file: sstData
# Prep data
for aRow in sstData:
	aRow[0]=str(aRow[0])
	aRow[1]=str(aRow[1])
	x = aRow[1]=str(aRow[1])
	x = aRow[1]=str(aRow[1]).zfill(2)
	aRow[1] = x
	aRow[2]=float(aRow[2])
	aRow[3]=float(aRow[3])
	aRow[4]=float(aRow[4])
	aRow[5]=float(aRow[5])
	aRow[6]=float(aRow[6])
	aRow[7]=float(aRow[7])
	aRow[8]=float(aRow[8])
	aRow[9]=float(aRow[9])

# Write Index of dates in order
MainIndex = []
for aRow in sstData:
	MainIndex.append(aRow[0:2])
x = 0

# Copy index dates for each SST zone
N1_N2 = copy.deepcopy(MainIndex) # 2-3
N3 = copy.deepcopy(MainIndex) # 4-5
N4 = copy.deepcopy(MainIndex) # 6-7
N3p4 = copy.deepcopy(MainIndex) # 8-9

# Append dated SST index with specific SST values
for aRow in sstData:
	N1_N2[x].insert(3, aRow[2])
	N1_N2[x].insert(4, aRow[3])
	N3[x].insert(3, aRow[4])
	N3[x].insert(4, aRow[5])
	N4[x].insert(3, aRow[6])
	N4[x].insert(4, aRow[7])
	N3p4[x].insert(3, aRow[8])
	N3p4[x].insert(4, aRow[9])
	x = x+1

# Format for each SST and ONI set: [Year, Month, SST, ONI]
# print N1_N2[1]
# print N3[1]
# print N4[1]
# print N3p4[1]
# print sstData[1]

# Format for Anom Records is as follows:
#****[Year, Month, Temperature C, Anomaly Value in C]****
#****[Year, Month, Temperature C, Anomaly Value in C]****
# Anomaly values +0.5 C are considered significant after 5
# 3 month mean consecutive periods (15 months) for El Nino // USE N3p4
# Anomaly values -0.5 C are considered significant after 5
# 3 month mean consecutive periods (15 months) for La Nina // USE N4
# *************N3p4 GRAPHING******************
# *************N3p4 GRAPHING******************
# *************N3p4 GRAPHING******************

x = []
y = []
from datetime import datetime
for aRow in N3p4:
	y.append(aRow[-1])
	x.append(aRow[0:2])
# print x
x1 = []
temp = []
for aRow in x:
	aRow = str(aRow)
	aRow = aRow.replace(", ", "-")
	aRow = aRow.replace("[", "")
	aRow = aRow.replace("]", "")
	aRow = aRow.replace("'", "")
	temp = datetime.strptime(aRow, '%Y-%m')
	x1.append(temp)
	temp = []
y = np.array(y, dtype=float)

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

date = []
for aItem in x1:
	# print aItem
	np.datetime64(aItem)
	date.append(aItem)
date = np.array(date, dtype='datetime64[D]')
date = date.astype('O')
N3p4Dates = copy.deepcopy(date)
y = np.array(y, dtype='float')
# print date

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(date, y, label = 'ONI')


# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)
# myFmt = mdates.DateFormatter('%m')
# ax.xaxis.set_minor_formatter(myFmt)

import datetime
datemin = datetime.date(date.min().year, 1, 1)
datemax = datetime.date(date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

#LABEL
ax.legend(loc='right')
ax.set_title('1982-2018 Oceanic Nino Index 3.4')
ax.set_xlabel('Year')
ax.set_ylabel('Oceanic Nino Index')

# ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = y
ax.grid(True)

fig.autofmt_xdate()

plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.savefig('3.4ONI.pdf')
plt.close()
# *************N4 GRAPHING******************
# *************N4 GRAPHING******************
# *************N4 GRAPHING******************
x2 = []
y2 = []

for aRow in N4:
	y2.append(aRow[-1])
	x2.append(aRow[0:2])
# print x
x12 = []
temp = []
for aRow in x2:
	aRow = str(aRow)
	aRow = aRow.replace(", ", "-")
	aRow = aRow.replace("[", "")
	aRow = aRow.replace("]", "")
	aRow = aRow.replace("'", "")
	# aRow = str.zfill(2) 
	# temp = datetime.strptime(aRow, '%Y-%m')
	x12.append(aRow)

# print x1

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

date2 = []
for aItem in x12:
	# print aItem
	np.datetime64(aItem)
	date2.append(aItem)
date2 = np.array(date2, dtype='datetime64[D]')
date2 = date2.astype('O')
y2 = np.array(y2, dtype='float')
# print date

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(date2, y2, label = 'ONI')


# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)
# myFmt = mdates.DateFormatter('%m')
# ax.xaxis.set_minor_formatter(myFmt)

datemin = datetime.date(date.min().year, 1, 1)
datemax = datetime.date(date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

#LABEL
ax.legend(loc='right')
ax.set_title('1982-2018 Oceanic Nino Index 4')
ax.set_xlabel('Year')
ax.set_ylabel('Oceanic Nino Index')

# ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = y
ax.grid(True)

fig.autofmt_xdate()

plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.savefig('4ONI.pdf')
plt.close()
#***************************Overlay N4 N3.4 N3 N1_N2
#***************************Overlay N4 N3.4 N3 N1_N2
#***************************Overlay N4 N3.4 N3 N1_N2
# Points for N3
x3 = []
y3 = []

for aRow in N3:
	y3.append(aRow[-1])
	x3.append(aRow[0:2])
# print x
x13 = []
temp = []
for aRow in x3:
	aRow = str(aRow)
	aRow = aRow.replace(", ", "-")
	aRow = aRow.replace("[", "")
	aRow = aRow.replace("]", "")
	aRow = aRow.replace("'", "")
	x13.append(aRow)
date3 = []
for aItem in x13:
	# print aItem
	np.datetime64(aItem)
	date3.append(aItem)
date3 = np.array(date3, dtype='datetime64[D]')
date3 = date3.astype('O')
y3 = np.array(y3, dtype='float')
# Points for N 1 & 2
x4 = []
y4 = []

for aRow in N1_N2:
	y4.append(aRow[-1])
	x4.append(aRow[0:2])
# print x
x14 = []
temp = []
for aRow in x4:
	aRow = str(aRow)
	aRow = aRow.replace(", ", "-")
	aRow = aRow.replace("[", "")
	aRow = aRow.replace("]", "")
	aRow = aRow.replace("'", "")
	x14.append(aRow)
date4 = []
for aItem in x14:
	# print aItem
	np.datetime64(aItem)
	date4.append(aItem)
date4 = np.array(date4, dtype='datetime64[D]')
date4 = date4.astype('O')
y4 = np.array(y4, dtype='float')

fig, ax = plt.subplots(figsize=(13, 8))
plt.plot(date2, y2, label = 'N4')
plt.plot(date, y, label = 'N3.4')
plt.plot(date3, y3, label = 'N3')
plt.plot(date4, y4, label = 'N1_N2')


# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)
# myFmt = mdates.DateFormatter('%m')
# ax.xaxis.set_minor_formatter(myFmt)

datemin = datetime.date(date.min().year, 1, 1)
datemax = datetime.date(date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

#LABEL
ax.legend(loc='right')
ax.set_title('1982-2018 Oceanic Nino Index')
ax.set_xlabel('Year')
ax.set_ylabel('Oceanic Nino Index')

# ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = y
ax.grid(True)

fig.autofmt_xdate()

plt.legend(loc='upper left')
plt.xticks(rotation=90)
# plt.show()
plt.savefig('All_SST_Values.pdf')
plt.close()

#************************CHOOSE SIMILAR YEARS********************
#************************CHOOSE SIMILAR YEARS********************
#************************CHOOSE SIMILAR YEARS********************

i = 0
for aRow in N3p4:
	aRow.append(N3p4Dates[i])
	i = i+1
	
dfN = pd.DataFrame(N3p4, columns=['Year', 'Month', 'SST', 'ONI', 'Date'])
dfN['Date'] = pd.to_datetime(dfN['Date'])

dfN['Date'] = dfN.Date.dt.strftime('%m %Y')


Totaldf = dfN

Totaldf['Date'] = pd.to_datetime(Totaldf['Date'])
Totaldf = Totaldf.sort_values(by='Date')
Totaldf = Totaldf.reset_index()
Totaldf = Totaldf.drop(columns='index')
# print Totaldf.head()
Totaldf = Totaldf.values.tolist()
#FORMAT [Year, Month, SST, ONI, Date}


#**********************PREP SST DATA***************
#**********************PREP SST DATA***************
#**********************PREP SST DATA***************

for aRow in Totaldf:
	aRow[0] = np.datetime64(aRow[0])
	x = aRow[0]
	del aRow[0]
	aRow.insert(0, x)

SelectedData = []
startdate = np.datetime64('1982-01-01')
enddate = Totaldf[-1][0]

for aRow in Totaldf:
	if aRow[0]>=startdate and aRow[0]<=enddate:
		SelectedData.append(aRow)

WindowAve = []
x = []
AveSST = []
AveElevation = []
i = 0
for aRow in SelectedData:
    aRow.insert(0, i)
    del aRow[-1]
    i=i+1

# print SelectedData
windowIndexMin=0
windowIndexMax = 5 #Months for Average
ONI_InWindow = []
numbEventsAboveWindowMean = 0
ONI_STD = []
AveONI = []
Date = []

for aRow in SelectedData:
    if aRow[0]>= windowIndexMax:
        for j in range(windowIndexMin,windowIndexMax,1):
            ONI_InWindow.append(SelectedData[j][-1])

	ONI_InWindowArray = np.array(ONI_InWindow, dtype=np.float)
	ONI_MeanInWindow = np.mean(ONI_InWindowArray)
	ONI_STDInWindow = np.std(ONI_InWindowArray)

	if (j+1)>=len(SelectedData):
	    break
	AveE = SelectedData[j+1][2]
	d = SelectedData[j+1][1]
	AveElevation.append(AveE)
	Date.append(d)
	# SSTMeanInWindow = np.ndarray.astype(SSTMeanInWindow, str)
	AveONI.append(ONI_MeanInWindow)
	ONI_STD.append(ONI_STDInWindow)
	ONI_InWindow = []
	windowIndexMin=windowIndexMin+1
	windowIndexMax=windowIndexMax+1
# print AveONI[0]
# print AveElevation[0]
# **************************GRAPH*********************

Date = np.array(Date, dtype='datetime64[D]')
Date = Date.astype('O')


fig, ax1 = plt.subplots(figsize=(13, 8))
ax1.plot(Date, AveONI, label = '4 Month Average ONI')

ax2 = ax1.twinx()
ax2.plot(Date, AveElevation, label = 'Ave Water Level', color='black')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)
# myFmt = mdates.DateFormatter('%m')
# ax.xaxis.set_minor_formatter(myFmt)

datemin = datetime.date(Date.min().year, 1, 1)
datemax = datetime.date(Date.max().year + 1, 1, 1)
ax1.set_xlim(datemin, datemax)

#LABEL
# ax2.legend(loc='upper right')
# ax1.legend(loc='upper left')
# ax1.set_title('%i-%i ONI and Water Level' % (YearStart, CurrentYear))
ax1.set_xlabel('Year')
ax1.set_ylabel('Degrees Celsius')
ax2.set_ylabel('Water Level (ft)')

ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = y
ax1.grid(True)

fig.autofmt_xdate()

# plt.legend(loc='upper left')
plt.xticks(rotation=90)
# plt.show()
plt.savefig('5MonthAveOIN_MaxRE.pdf')
plt.show()
plt.close()

#**********************GRAPH****************************
from matplotlib.ticker import NullFormatter

# the random data
Ignore = ~np.logical_or(np.isnan(AveONI), np.isnan(AveElevation))
# print Ignore
# print AveElevation
AveONI = np.compress(Ignore, AveONI)
AveElevation = np.compress(Ignore, AveElevation)
# print AveElevation
x = AveONI
y = AveElevation

nullfmt = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(10, 10))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y)

# now determine nice limits by hand:
# binwidth = 0.25
binwidthx = 0.05
binwidthy = 0.2
# xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
xmax = np.max(np.fabs(x))
ymax = np.max(np.fabs(y))
# lim = (int(xymax/binwidth) + 1) * binwidth
limx = (int(xmax/binwidthx) + 1) * binwidthx
limy = (int(ymax/binwidthy) + 1) * binwidthy
# axScatter.set_xlim((-lim, lim))
# axScatter.set_ylim((-lim, lim))
axScatter.set_xlim((-limx, limx))
axScatter.set_ylim((10, limy))

# bins = np.arange(-lim, lim + binwidth, binwidth)
binsx = np.arange(-limx, limx + binwidthx, binwidthx)
binsy = np.arange(-limy, limy + binwidthy, binwidthy)
axHistx.hist(x, bins=binsx)
axHisty.hist(y, bins=binsy, orientation='horizontal')
axHisty.set_xlabel('Number of Records', fontsize=12)
axHistx.set_ylabel('Number of Records', fontsize=12)
axHistx.set_xlim(axScatter.get_xlim())
axHisty.set_ylim(axScatter.get_ylim())
axScatter.set_xlabel('ONI', fontsize=12)
axScatter.set_ylabel('River Depth (ft)', fontsize=12)
axScatter.set_title('%i-%i Oceanic Nino Index(3.4) and Monthly High Water Level' % (1982, CurrentYear), y = 1.3255)
fig.tight_layout()
plt.savefig('5MonthOIN_MaxRE_Hist.pdf')

# plt.show()
#**************************5 3 month av N3.4***************
#**************************5 3 month av N3.4***************
#**************************5 3 month av N3.4***************
#*********************AVE 1
AveElevation = []
windowIndexMin=0
windowIndexMax = 3 #Months for Average
ONI_InWindow = []
ONI_STD = []
ONI_STDInWindow = []
AveONI = []
Date = []
for aRow in SelectedData:
    if aRow[0]>= windowIndexMax:
        for j in range(windowIndexMin,windowIndexMax,1):
            ONI_InWindow.append(SelectedData[j][-1])


	ONI_InWindowArray = np.array(ONI_InWindow, dtype=np.float)
	ONI_MeanInWindow = np.mean(ONI_InWindowArray)
	ONI_STDInWindow = np.std(ONI_InWindowArray)

	if (j+1)>=len(SelectedData):
	    break
	AveE = SelectedData[j+1][2]
	d = SelectedData[j+1][1]
	AveElevation.append(AveE)
	Date.append(d)
	# SSTMeanInWindow = np.ndarray.astype(SSTMeanInWindow, str)

	AveONI.append(ONI_MeanInWindow)
	ONI_STD.append(ONI_STDInWindow)
	ONI_InWindow = []
	windowIndexMin=windowIndexMin+1
	windowIndexMax=windowIndexMax+1
# AveONI = np.array.tolist(AveONI)

#*********************AVE 2
i = 0
DataList = copy.deepcopy(SelectedData[3::])
for aRow in DataList:
	del aRow[0]
	aRow.insert(0, i)
	aRow.insert(1, AveONI[i])
	i = i+1
# print DataList

windowIndexMin=0
windowIndexMax = 5 #Months for Average
ONI_InWindow = []
ONI_STD = []
AveONI = []
Date = []
AveElevation = []
for aRow in DataList:
    if aRow[0]>= windowIndexMax:
        for j in range(windowIndexMin,windowIndexMax,1):
            ONI_InWindow.append(DataList[j][1])

	ONI_InWindowArray = np.array(ONI_InWindow, dtype=np.float)
	ONI_MeanInWindow = np.mean(ONI_InWindowArray)
	ONI_STDInWindow = np.std(ONI_InWindowArray)

	if (j+1)>=len(DataList):
	    break
	AveE = DataList[j+1][3]
	d = DataList[j+1][2]
	AveElevation.append(AveE)
	Date.append(d)
	# SSTMeanInWindow = np.ndarray.astype(SSTMeanInWindow, str)

	AveONI.append(ONI_MeanInWindow)
	ONI_STD.append(ONI_STDInWindow)
	ONI_InWindow = []
	windowIndexMin=windowIndexMin+1
	windowIndexMax=windowIndexMax+1

# print len(AveONI)
# print len(AveElevation)
#****************************GRAPH 3 consec 3 month ave***********

Date = np.array(Date, dtype='datetime64[D]')
Date = Date.astype('O')


fig, ax1 = plt.subplots(figsize=(13, 8))
ax1.plot(Date, AveONI, label = '3 Segments of 3 Month Average ONI')

ax2 = ax1.twinx()
ax2.plot(Date, AveElevation, label = 'Ave Water Level', color='black')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
# ax.xaxis.set_minor_locator(months)
# myFmt = mdates.DateFormatter('%m')
# ax.xaxis.set_minor_formatter(myFmt)

datemin = datetime.date(Date.min().year, 1, 1)
datemax = datetime.date(Date.max().year + 1, 1, 1)
ax1.set_xlim(datemin, datemax)

#LABEL
# ax2.legend(loc='upper right')
# ax1.legend(loc='upper left')
ax1.set_title('%i-%i ONI and Water Level' % (YearStart, CurrentYear))
ax1.set_xlabel('Year')
ax1.set_ylabel('Degrees Celsius')
ax2.set_ylabel('Water Level (ft)')

ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = y
ax1.grid(True)

fig.autofmt_xdate()

# plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.show()
# plt.savefig('5MonthAveOIN_MaxRE.pdf')
plt.close()

#**********************GRAPH****************************
from matplotlib.ticker import NullFormatter

# the random data
Ignore = ~np.logical_or(np.isnan(AveONI), np.isnan(AveElevation))
# print Ignore
# print AveElevation
AveONI = np.compress(Ignore, AveONI)
AveElevation = np.compress(Ignore, AveElevation)
# print AveElevation
x = AveONI
y = AveElevation

nullfmt = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(10, 10))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y)

# now determine nice limits by hand:
# binwidth = 0.25
binwidthx = 0.05
binwidthy = 0.2
# xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
xmax = np.max(np.fabs(x))
ymax = np.max(np.fabs(y))
# lim = (int(xymax/binwidth) + 1) * binwidth
limx = (int(xmax/binwidthx) + 1) * binwidthx
limy = (int(ymax/binwidthy) + 1) * binwidthy
# axScatter.set_xlim((-lim, lim))
# axScatter.set_ylim((-lim, lim))
axScatter.set_xlim((-limx, limx))
axScatter.set_ylim((10, limy))

# bins = np.arange(-lim, lim + binwidth, binwidth)
binsx = np.arange(-limx, limx + binwidthx, binwidthx)
binsy = np.arange(-limy, limy + binwidthy, binwidthy)
axHistx.hist(x, bins=binsx)
axHisty.hist(y, bins=binsy, orientation='horizontal')
axHisty.set_xlabel('Number of Records', fontsize=12)
axHistx.set_ylabel('Number of Records', fontsize=12)
axHistx.set_xlim(axScatter.get_xlim())
axHisty.set_ylim(axScatter.get_ylim())
axScatter.set_xlabel('ONI', fontsize=12)
axScatter.set_ylabel('River Depth (ft)', fontsize=12)
axScatter.set_title('%i-%i Oceanic Nino Index(3.4) and Monthly High Water Level' % (1982, CurrentYear), y = 1.3255)
fig.tight_layout()
plt.savefig('5MonthOIN_MaxRE_Hist.pdf')

#*******************Graph of Month direct Month Pearson*****************
#*******************Graph of Month direct Month Pearson*****************
#*******************Graph of Month direct Month Pearson*****************

