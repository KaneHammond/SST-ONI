import Modules

from Modules import*


# Identify the csv file in the folder paths
Files = os.listdir("CSV_DATA/")

# Extract data from a given file in Files
df = pd.DataFrame(columns=['Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# Loop index
i = 0
while i < len(Files):
	with open('CSV_DATA/'+Files[i]) as f:
		# Define which index is being processed
		Split1 = Files[i].replace('_SST', '')
		Split2 = Split1.replace('.csv', '')
		RawData = []
		for aRow in f:
			RawData.append(aRow)
		# Drop first row, just the header
		RawData = RawData[1::]
		
		# Clean up the data
		allData = []
		for aRow in RawData:
			# aRow = aRow.replace('\\n', '')
			aRow = aRow.split(',')
			# Now clean up the list item
			LI = []
			for aItem in aRow:
				if aItem!=aRow[-1]:
					LI.append(aItem)
				if aItem==aRow[-1]:
					# Remove line end from final item
					aItem = aItem.replace('\n', '')
					LI.append(aItem)
			allData.append(LI)
		# allData format: [index, year, SST 1, SST 2, SST 3, SST 4, SST 5, SST 6, SST 7,
		# SST 8, SST 9, SST 10, SST 11, SST 12,]

		# Start calculating the averages
		# The first year we can start is 1965 based upon current methods
		# for calculating the ONI. The center of the analysis will be the 
		# first of a 5 year window analyzed under the average. Current
		# method of averaging uses a 5 year window for calculating the 
		# ONI, using a 30 year average for each 5 years. Source:
		# https://www.climate.gov/news-features/understanding-climate/watching-el-ni%C3%B1o-and-la-ni%C3%B1a-noaa-adapts-global-warming


		# Calculate our 30 year averages centered on a specific year as
		# defined by NOAA

		# Max limit
		MaxL = int(allData[-1][1])-15
		# Min limit
		MinL = int(allData[0][1])+14
		# Define the years for the averages to be calculated on
		YearsCalc = []
		for m in range(MinL, MaxL):
			YearsCalc.append(m)
		# 30 year average data
		TAveDat = []
		# Temporary Data
		Temp = []
		# Years for each average
		YearsAve = []
		# Index value
		c = 1
		n = 0
		# while n < len(YearsCalc):
		for aRow in allData:
			if int(aRow[1]) == int(YearsCalc[n]):
				n = n+1
				MinY = int(aRow[1])-14
				MaxY = int(aRow[1])+15
				for TY in range(MinY, MaxY+1):
					for aItem in allData:
						if int(aItem[1]) == int(TY):
							SST_Temp = aItem[2::]
							for Temperature in SST_Temp:
								Temperature = float(Temperature)
								Temp.append(Temperature)
				TT = sum(Temp)
				Ave = TT/360
				TAveDat.append(Ave)
				YearsAve.append(aRow[1])
				Temp = []
				if n == len(YearsCalc):
					break

		# Use our data to compare 5 year segments to the centered 30 year
		# averages. We will start as far back as possible. The averages
		# are automatically calculated for every year possible in the
		# dataset.

		# Define start year
		SY = int(YearsAve[0])
		# Define the window mod. We are analyzing 5 years at a time.
		# Adding 4 will push the next date up for the analysis to allow
		# for the selection of 5 years of data.
		WindowMod = 5
		# Years to center a 30 year average
		CY = []
		Y = 0

		# Define the years the 30 year averages will be "centered" on
		while Y<int(YearsAve[-1]):
			if Y==0:
				Y = int(YearsAve[0])
				CY.append(Y)
			if Y!=0:
				Y = Y+WindowMod
				if Y<int(YearsAve[-1]):
					CY.append(Y)

		# Define which years are present in the set to determine where
		# the end of the current method is no longer useable. The NOAA
		# now use a 30 year average to explain the most recent decade,
		# where data is not available to use the method above. This is 
		# similar to the old method used.

		IncompleteYears = []
		Records = []
		NegVal = 0
		for aRow in allData:
			# Select only monthly data to check if its a full set.
			# Meaning no -99.99 values, for when data is not available
			Select = aRow[2::]
			Temp = []
			for aItem in Select:
				Temp.append(float(aItem))
			for aItem in Temp:
				if aItem < 0:
					# Count if negative values present. These
					# represent no data.
					NegVal = NegVal+1 
			# This will identify the location of negative values in a given year
			# if it is the final year (it should be), they will be the last
			# ones in the MonthlyValues data set. 
			if NegVal>0:
				Records.append(NegVal)
				IncompleteYears.append(aRow[1])			
				NegVal = 0
		
		if len(IncompleteYears)>1:
			print 'Multiple Years Missing From Record.\n 		****EXIT****'
			sys.exit()


		# Write the data set with all monthly data. The first record will
		# be January of the first year in the data set.
		MonthlyValues= []
		for aRow in allData:
			Select = aRow[2::]
			for aItem in Select:
				MonthlyValues.append(aItem)
		
		# Compute the rolling average

		# Window size
		Window = 3
		# index value
		i = 0
		# Temp total 
		TT = 0
		# Rolling Window
		ThreeMonthAve = []
		# Starting index
		SI = 1
		while SI<len(MonthlyValues)-1:
			Temp = (float(MonthlyValues[SI-1])+float(MonthlyValues[SI])+float(MonthlyValues[SI+1]))/3
			ThreeMonthAve.append(Temp)
			SI = SI+1

		# Filter out the incomplete data for the final year.
		# If only one month is incorect, then the Mod value would be equal 
		# to zero. In this case, the entire available data set can be used
		# as the first and last month of the
		Mod = (Records[0]*-1)+1
		if Mod==0:
			Mod=len(ThreeMonthAve)
		TMA = ThreeMonthAve[0:Mod]

		# Define length of years
		FY = 11
		FiY = 12-(int(Records[0]))
		SY = 12 

		# Other years will have 12 records each, determine how many years
		# are in the data set.

		# Set a counting index for the loop
		i = 0
		Ri = 0
		Data = []
		Temp = []
		for anAve in TMA:
			# If the index is 0, it is within the first year
			if i==0:
				Ri = Ri+1
				Temp.append(anAve)
				# If the Ri is equal to the the FY limit, the first
				# year is over. We must then append the Temp data
				# and add a year/reset our Ri.
				if Ri==FY:
					Data.append(Temp)
					Temp = []
					i = i+1
					Ri = 0
			# Check for finaly year
			if i==allData[-1][0]:
				Ri = Ri+1
				Temp.append(anAve)
				if Ri==FiY:
					Data.append(Temp)
					Temp = []
			# Every other year
			if i>0 and i < allData[-1][0]:
				Ri = Ri+1
				Temp.append(anAve)
				if Ri==SY:
					Data.append(Temp)
					Temp = []
					Ri = 0
					i = i+1

		# Define last decades of data to use the 30 year average
		# calculations on

		# Determine the limit for the first decade to be graphed on a 
		# 30 year average.
		MinLThrt = int(round(MaxL/100)*100)+1
		
		# Count how many decades need to be analyzed using the fixed 30
		# year average. The final decade may be incomplete

		# Index
		i = 1
		c = 0
		Limit = 9

		Year = MinLThrt

		DecEnds = []

		while Year<int(allData[-1][1]):
			Year = Year+i
			c = c+i
			if c == Limit:
				DecEnds.append(Year)
		DecEnds.append(Year)
		# print DecEnds

		DecStarts = [MinLThrt]

		if len(DecEnds)>1:
			DecStarts.append(MinLThrt+10)

		# print DecStarts

		# Calculate the 30 year averages
		TYAves = []

		for aDate in DecStarts:
			MinDate = aDate-30

			sys.exit()



		# # Year index
		# Index = []

		# for z in range(int(allData[0][0]), int(allData[-1][0])):
		# 	Index.append(z)
		# print Index
		# sys.exit()

		# if len(IncompleteYears)>0:
		# 	for aItem in IncompleteYears:
		# 		for aRow in allData:
		# 			if aItem==aRow[1]:



		# Parse the 3 month averages by year, the firs and last months
		# are not able to be used. So the lenght of the set should 
		# be 2 less than the lenght of total monthly values.







		# Write an index which signifies the start of each year (in the monthly
		# data set)

		sys.exit()






		# WORK
		# the downloaded data is in, just need to start using it
		sys.exit()

		



