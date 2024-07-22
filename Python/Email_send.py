import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("mohammadalisk050@gmail.com","mrly xagv ngab gbdf ")
subject = "Interview"
body = 'Hi i am python'
massage = "Subject : {}\n\n{}".format(subject,body)
listadd = ['mohammadalisk01@gmail.com','mohammadalisk060@gmail.com']
ob.sendmail('mohammadalisk050@gmail.com',listadd,massage)
ob.quit()
print("Email send Succesfully.")