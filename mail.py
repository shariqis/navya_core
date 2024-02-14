# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib   
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)   
# start TLS for security  Transport Layer Security  from emaiol id---> dummy mail id
s.starttls()   
# Authentication 
s.login("from@gmail.com", "ppoy evys fdec lujm")   
# message to be sent 
message = "Message_you_need_to_send"  
# sending the mail 
s.sendmail("from@gmail.com", "to@gmail.com", message)   
# terminating the session 
s.quit() 