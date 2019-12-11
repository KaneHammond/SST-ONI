import Modules

from Modules import*

# Disable warning for insecure download.
# Message given without disabling:
# C:\Python27\lib\site-packages\urllib3\connectionpool.py:847: 
# InsecureRequestWarning: Unverified HTTPS request is being made. 
# Adding certificate verification is strongly advised. 
# See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# InsecureRequestWarning)

# Write output location for raw data 
dir = 'RAW_TXT_DATA'
if not os.path.exists(dir):
    os.makedirs(dir)
RawOut = 'RAW_TXT_DATA/'

dir = 'CSV_DATA'
if not os.path.exists(dir):
    os.makedirs(dir)
CSVOut = 'CSV_DATA/'

# DOWNLOAD
#####################################################################################

print 'Downloading Files...'
# Download the Nino 4 Index data
urllib3.disable_warnings()
url = "http://www.esrl.noaa.gov/psd/data/correlation/nina4.data"
fileName = "nina4.txt"
with urllib3.PoolManager() as http:
    r = http.request('GET', url)
    with open(RawOut+fileName, 'wb') as fout:
        fout.write(r.data)

# Download the Nino 3.4 Index data (Most common one used)
url = "http://www.esrl.noaa.gov/psd/data/correlation/nina34.data"
fileName = "nina34.txt"
with urllib3.PoolManager() as http:
    r = http.request('GET', url)
    with open(RawOut+fileName, 'wb') as fout:
        fout.write(r.data)

# Download the Nino 1+2 Index data
url = "http://www.esrl.noaa.gov/psd/data/correlation/nina1.data"
fileName = "nina12.txt"
with urllib3.PoolManager() as http:
    r = http.request('GET', url)
    with open(RawOut+fileName, 'wb') as fout:
        fout.write(r.data)
#####################################################################################
print '\nConverting .txt files to .csv...'
# Process files
Files = os.listdir("RAW_TXT_DATA/")

df = pd.DataFrame(columns=['Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# Loop index
i = 0
while i < len(Files):
	with open(RawOut+Files[i]) as f:
		# Define which index is being processed
		Split1 = Files[i].replace('nina', '')
		Split2 = Split1.replace('.txt', '')
		# Check its length, if greater than 1, a decimal must be placed
		if len(Split2) > 1:
			ID = Split2[0]+'.'+Split2[-1]
		# If one number is identified then no decimal and ampersand are needed
		if len(Split2) == 1:
			ID = Split2

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

