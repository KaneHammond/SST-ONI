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

		print allData
		# WORK
		# the downloaded data is in, just need to start using it
		sys.exit()

		lineList = f.readlines()
		#First 3 items are the header, 1948, and 1949. Years not useable
		# Final 3 records are not useful, they are link info.
		RawData = lineList[3:-3]
		for aItem in RawData:
			# print aItem
			# Split our data by double spaces
			aItemI = aItem.split('  ')
			# If there is missing data for some months,
			# it will need to be split by single space first.
			if len(aItemI)<13:
				# Write a temporary list for data filtering for when data is missing
				Temp = []
				aItemI = aItem.split(' ')
				aItemI[-1] = aItemI[-1].replace('\n', '')
				# For loop to drop blank elements in list
				for Var in aItemI:
					if Var!='':
						Temp.append(Var)
				aItemI = Temp
			# Replace the new line indicator
			aItemI[-1] = aItemI[-1].replace('\n', '')

			# Write a temporary dataframe of the object
			Tempdf = pd.DataFrame(aItemI)
			# Transpose our data
			Tempdf = Tempdf.transpose()
			# Insert the header info so it matches
			Tempdf.columns = columns=['Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
			# Append the data
			df = df.append(Tempdf, ignore_index = True)
		# Write a csv file with the data, use the ID to illustrate
		# which index the file belongs to. All values recorded as -99.99
		# are those provided to signify no data.
		pd.DataFrame.to_csv(df, CSVOut+ID+'_SST.csv')
		# Clear data from the df to allow for new data in next loop
		df = df.iloc[0:0]
		f.close()
		# Add 1 to the index for the loop
		i = i+1



