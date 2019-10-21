# ThirdSpace_Autobook
A Python script that utilises Seleium to automatically navigate through the ThirdSpace web pages to book a fitness class. Intended to be integrated into a task scheduler to automatically execute at a specified time.

To use, create file named 'credentails.py' at root directory. 
Contain within the file:
username = "(email address)"
password = "(password)"
 Where 'email address' and 'password' are valid Third Space credentails
  
 Within app_V2.py the following XPATH defines which exercicse class will be booked:
 html/body/main/div[5]/div/div[2]/div[1]/div/div[3]/div/div[24]
 
This can be modified in for the class of choice by getting the XPATH of the class from the timetable page.
