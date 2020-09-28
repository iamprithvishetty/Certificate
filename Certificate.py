#Certificate Automation
#I had 3 sheets so three if conditions I have used you can increase the no of flags or decrease along with the for loop according to your requirements

import gspread #Google Spread Sheet Library Included
from PIL import Image, ImageDraw, ImageFont #Pillow Library Included
from oauth2client.service_account import ServiceAccountCredentials #oauth2client in order to make changes using the credentials in our Sheets
count = 1 #count variable is used here for incrementing/ navigating through all the names in the Google sheet
ch = 0 #Check 0       THE USE OF CHECK IS FOR SETTING FLAGS IN ORDER TO CHANGE THE SHEET
ch1 = 1 #Check 1
ch2 = 1 #Check 2
ch3 = 0 #Check 3
scope = ['https://www.googleapis.com/auth/drive.readonly'] #We are only reading the file  so scope is set accordingly
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope) # credentials.json is the file which was downloaded when I created credentials in Google API
client = gspread.authorize(credentials) #Authorizing our credentials and connecting

sheet = client.open('question_dnb').worksheet('Sheet1') #'question_dnb' is the Google Sheet I want to access and inside that I want to access Sheet1
sheet1 = client.open('question_dnb').worksheet('Sheet2') #'question_dnb' is the Google Sheet I want to access and inside that I want to access Sheet2
sheet2 = client.open('question_dnb').worksheet('Sheet3') #'question_dnb' is the Google Sheet I want to access and inside that I want to access Sheet3

'''data = sheet.row_values(i)  # JUST FOR CHECKING PURPOSE
data1 = sheet1.row_values(i)
data2 = sheet2.row_values(i)
print(data)
print(data1)
print(data2)'''

while ch3 != 1 : #Run through the loop until the last sheet is checked and ch3 is set to 1
	
	if ch == 0: #For Sheet1 
		data = sheet.row_values(count) #data is the count^th row stored in terms of list of the Sheet1, we are reading the row value and storing it inside the list
		if data[0] == '0': #This is to keep a check on whether we have reached the last element i.e set to "0" in the Sheet
			ch = 1 # ch is set high to indicate that Sheet1 has been completely navigated through
			ch1 = 0 # ch1 is set low to move to the Sheet2 
			count=1 #count is again resetted for the next Sheet i.e Sheet2
		else :
			image = Image.open('FINAL.png') #My Image or in this case template I want to make changes in
			draw = ImageDraw.Draw(image) #I've opened the image in Drawing mode to make the changes
			font = ImageFont.truetype('Calibri.ttf', size=150) #Set the font type and size
			(x, y) = (1300, 1000) #Co-ordinate where we want to plce the text
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data[0], fill=color, font=font) #use the text method to insert the text at the specified coordinates with the mentioned attributes
			image.save('C:\Prithvi\Certificate\Certi\\'+data[0]+'.png') #Save the image concatinated with the name at the end so hence data[0] is used
			count=count+1 # Incrementing thee count to move to the next row

	if ch1 == 0:
		data1 = sheet1.row_values(count)
		if data1[0] == '0':
			ch = 1
			ch1 = 1 # ch1 is set high to indicate that Sheet2 has been completely navigated through
			ch2 = 0 # ch2 is set low to move to the Sheet3
			count=1 #count is again resetted for the next Sheet i.e Sheet3
		else :
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data1[0], fill=color, font=font)
			image.save('C:\Prithvi\Certificate\Certi\\'+data1[0]+'1.png')
			count=count+1

	if ch2 == 0:
		data2 = sheet2.row_values(count)
		if data2[0] == '0':
			ch = 1
			ch1 = 1
			ch2 = 1 # ch2 is set high to indicate that Sheet3 has been completely navigated through
			ch3 = 1 # ch3 is set high to get out of the while Loop
		else :
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data2[0], fill=color, font=font)
			image.save('C:\Prithvi\Certificate\Certi\\'+data2[0]+'2.png')
			count=count+1
