#! python3
import webbrowser, sys, pyperclip, requests, bs4, smtplib

from pip._internal.models import link

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

#this is the email it will send from, most likely you have to change settings on your gmail to get it to send. Check project descriptions.
conn.login('example@gmail.com','password')

sys.argv

if len(sys.argv) > 1:
  address =   ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

res = requests.get("https://enviro.epa.gov/enviro/uv_search_v2?zipcode="+address)
wholetext=bs4.BeautifulSoup(res.text,'html.parser')
res.text


#print(res.text)

images = wholetext.findAll('img')
text =""
for image in images:
    text += (image['src'])

#this is the uv indexes that an email will be sent

if text.find("/uv/images/ef/uv6") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 6...\n\n' "its hot. put sunscreen")

if text.find("/uv/images/ef/uv7") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 7...\n\n' "its hot. put sunscreen")

if text.find("/uv/images/ef/uv8") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 8...\n\n' "its hot. put sunscreen")

if text.find("/uv/images/ef/uv9") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 9...\n\n' "its hot. put sunscreen")

if text.find("/uv/images/ef/uv10") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 10...\n\n' "its hot babe. put sunscreen")

if text.find("/uv/images/ef/uv11") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 11...\n\n' "its hot. put sunscreen or stay inside")

if text.find("/uv/images/ef/uv12") > 0:
    conn.sendmail('example@gmail.com', 'example@gmail.com', 'Subject: HOT, Index 12...\n\n' "its hot. put sunscreen or honestly stay inside")

