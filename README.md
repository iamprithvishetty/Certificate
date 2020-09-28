# Certificate
Auto Generated Certificate using pillow and gspread

### 1) For setting up gspread i.e Google Developer Console and using API
Go to:-  https://console.developers.google.com/apis
#### a) Create New Project 
#### b) Select The New Project Created
#### c) Click Enable APIs and select all the APIs you will be using
#### d) For example Select Google Drive API and Google Sheets API and click Enable
#### e) Now Create credentials
   ##### 1)Select the API in use
   ##### 2)Select Web Server
   ##### 3)Select Application Data
   ##### 4)Are you planning to use this API with App Engine or Compute Engine?
       No, I’m not using them
   ##### 5)Now Create a service account
   #####    Give a service account name --> Anything
   #####    Role --> Project & Owner
       Key Type --> JSON
   ##### 6) IMP : A JSON file will be downloaded keep it safe and don't share it with anyone and you only have to create credentials once
   
### 2) Summary of the code
#### Install Google Sheets library
    pip install gspread
#### Install oauth2client library
    pip install oauth2client
#### Install Pillow library
    pip install Pillow
   PIL and Pillow currently cannot co-exist in the same environment. If you want to use Pillow, please remove PIL first.
#### All rest of the code details has been mentioned in the comments of the code
       
#### Python Code
      https://github.com/iamprithvishetty/Certificate/blob/master/Certificate.py
      
#### Sample Image File
      https://github.com/iamprithvishetty/Certificate/blob/master/FINAL.png
      
#### Sample Credentials File 
      https://github.com/iamprithvishetty/Certificate/blob/master/credentials.json
     
