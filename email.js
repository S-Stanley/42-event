const nodemailer = require("nodemailer");
const fs = require("fs");
require('dotenv').config()

function get_events(){
	fs.readFile('events.json', 'utf8', function (err,data) {
        	const output = [];
		let res = "";
		data = JSON.parse(data);
		for (let i in data) {
			const mls = new Date(data[i].begin_at) - new Date();
			if (mls > 0 && new Date(1631052000000) - new Date(data[i].begin_at) > 0)
				output.push(data[i]);
		}
		for (let x in output){
			res = res + `\nName: ${output[x].name}`;
			res = res + `\nDescription: ${output[x].description}`;
			res = res + `\nDate: ${output[x].begin_at}`;
			res = res + "\n\n******************\n\n";
		}
		send_email(res);
	});
}

async function send_email(content) {
	let transporter = nodemailer.createTransport({
		host: process.env.SMTP,
		port: 465,
		auth: {
			user: process.env.EMAIL_SMTP,
			pass: process.env.PASSWORD_SMTP,
		},
	});

	let info = await transporter.sendMail({
		from: process.env.EMAIL_SMTP,
		to: process.env.MYEMAIL,
		subject: "Events 42 of the week",
		text: content,
	});
	console.log("Message sent: %s", info.messageId);
	console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));
}

get_events();
