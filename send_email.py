import smtplib

def send_email_gmail(to: list, msg: str):
	gmail_user = 'stanleyserbin@gmail.com'
	gmail_password = 'cazjeH-wonpyd-1myqtu'

	sent_from = gmail_user
	subject = 'New subscriber!'
	body = msg

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print ('Email sent!')
	except Exception as e:
		print(e)
		print ('Something went wrong...')
