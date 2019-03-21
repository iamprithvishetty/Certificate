import gspread
from PIL import Image, ImageDraw, ImageFont
from oauth2client.service_account import ServiceAccountCredentials
i = 1
ch = 0
ch1 = 1
ch2 = 1
ch3 = 0
scope = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client = gspread.authorize(credentials)
sheet = client.open('question_dnb').worksheet('Sheet1')
data = sheet.row_values(i)
sheet1 = client.open('question_dnb').worksheet('Sheet2')
data1 = sheet1.row_values(i)
sheet2 = client.open('question_dnb').worksheet('Sheet3')
data2 = sheet2.row_values(i)
print(data)
print(data1)
print(data2)
while ch3 != 1 :
	if ch == 0:
		data = sheet.row_values(i)
		if data[0] == '0':
			ch = 1
			ch1 = 0
			i=1
		else :
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data[0], fill=color, font=font)
			image.save('C:\Prithvi\Certificate\Certi\\'+data[0]+'.png')
			i=i+1

	if ch1 == 0:
		data1 = sheet1.row_values(i)
		if data1[0] == '0':
			ch = 1
			ch1 = 1
			ch2 = 0
			i=1
		else :
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data1[0], fill=color, font=font)
			image.save('C:\Prithvi\Certificate\Certi\\'+data1[0]+'1.png')
			i=i+1

	if ch2 == 0:
		data2 = sheet2.row_values(i)
		if data2[0] == '0':
			ch = 1
			ch1 = 1
			ch2 = 1
			ch3 = 1
		else :
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data2[0], fill=color, font=font)
			image.save('C:\Prithvi\Certificate\Certi\\'+data2[0]+'2.png')
			i=i+1