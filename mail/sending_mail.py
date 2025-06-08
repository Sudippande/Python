import smtplib
content="hello This mail is send from Python"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender='sudippande10@gmail.com'
rec='sudippande81@gmail.com'
mail.login('sudippande10@gmail.com','Enter password here')
header='To:'+rec+'\n'+'From:'+sender+'\n'+'subject:testmail\n'
contetnt=header+content
mail.sendmail(sender,rec,content)
mail.close()