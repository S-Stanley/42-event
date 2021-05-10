import smtplib

def send_email_gmail(to: list, msg: str):
	gmail_user = 'stanleyserbin@gmail.com'
	gmail_password = 'cazjeH-wonpyd-1myqtu'
	subject = '42 events'
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(gmail_user, to, msg)
		server.close()

		print ('Email sent!')
	except Exception as e:
		print(e)
		print ('Something went wrong...')