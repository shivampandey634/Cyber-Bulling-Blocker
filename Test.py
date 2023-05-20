from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import time
from plyer import notification
import pyscreenshot
from PIL import Image
import pytesseract
from mailer import Mailer
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\shiva\AppData\Local\Tesseract-OCR\tesseract.exe'# Pytesseract should be installed in order to run this program


window = Tk()

background=PhotoImage(file="C:\pic.png")#    We can remove these three lines as the image loads from documents the local storage 
shiv=Label(window,image=background)
shiv.pack()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var5 = StringVar()
var6 = StringVar()
def unblocker(unblock):
	hosts_path="C:/Windows/System32/drivers/etc/hosts"
	with open(hosts_path,'r+') as file:
		content = file.readlines()
		file.seek(0)
		for line in content:
			if not any(website in line for website in unblock):
        		    file.write(line)
		
		file.truncate()


def blocker(website_list):
	hosts_path="C:/Windows/System32/drivers/etc/hosts"
	redirect = "127.0.0.1"
	print("printing check\n")
	with open(hosts_path, 'r+') as file:
		content = file.read()
		for website in website_list:
			if website in content:
				pass
			else:
                # mapping hostnames to your localhost IP address
			    file.write(redirect + " " + website + "\n")
	#print("function done")
	#time.sleep(2)
	#with open(hosts_path,'r+') as file:
	#	content = file.readlines()
	#	file.seek(0)
	#	for line in content:
	#		if not any(website in line for website in website_list):
    #    		    file.write(line)
	#	
	#	file.truncate()
# 1 1 1 1 1 1 1 1   

def ss_to_text(li,file_name,emal):
	image = "C:/Users/shiva/Pictures/Screenshots/"+file_name
	text = pytesseract.image_to_string(Image.open(image), lang="eng")
	print(text)
	for item in li:
		if(text.find(item)!=-1):
			print("found")
			mail = Mailer(email="cybereedu634@gmail.com", password="mwezyvkgnvpxwprs")
			mail.send(receiver=emal, subject='Your Cyber Bullying Blocker', message='Unwanted Contents found on the screen')
			break
		else:
			print("not found")

def working(li,t,email):
	localtime = time.localtime(time.time())
	prev=localtime.tm_sec
	i=1
	while(True):
		notification.notify(
        title = "ALERT!",
        message=" you are using ur pc for more than the limit time" ,           
        # displaying time
        timeout=2
		)
		#print(t)
		image = pyscreenshot.grab()

		# To display the captured screenshot
		#image.show()
		img_path="C:/Users/shiva/Pictures/Screenshots"
		file_name="screenshot_"+str(i)+".png"
		# To save the screenshot
		image.save(f"{img_path}/{file_name}")
		time.sleep(t)
		ss_to_text(li,file_name,email)
		i+=1
def message():
	if len(var1.get()) !=0 and len(var2.get())!=0:
		showinfo("Message", "Successfully saved!") 
	else:
		showinfo("Message", "Please Enter all the fields")

def convert_string_to_list(stri):
	li = list(stri.split(","))
	return li

def start():
	#print('bcd\n')

	#Setting the size of the window
	window.geometry('600x600')
	window.title("Proctor")

	
	#email of user
	lb1 = Label(window, text="Recipient E-mail", font=("Arial Bold", 15))
	lb1.place(x=50,y=100)

	txt1 = Entry(window,width=20, textvariable=var1)
	txt1.place(x=220,y=100)
	
	
	#words
	lb3 = Label(window, text="Enter cuss words", font=("Arial Bold", 15))
	lb3.place(x=50,y=150)
	 
	txt3 = Entry(window,width=20, textvariable=var2)
	txt3.place(x=250,y=150)

	#time of screenshot
	lb4 = Label(window, text="Time limit", font=("Arial Bold", 15))
	lb4.place(x=50,y=200)

	txt4 = Entry(window,width=20, textvariable=var3)
	txt4.place(x=170,y=200)

	#website name
	lb5 = Label(window, text="Website", font=("Arial Bold", 15))
	lb5.place(x=50,y=250)

	txt5 = Entry(window,width=20, textvariable=var5)
	txt5.place(x=170,y=250)

	#unblock_website_name
	lb6 = Label(window, text="Unblock-Website", font=("Arial Bold", 15))
	lb6.place(x=50,y=300)

	txt6 = Entry(window,width=20, textvariable=var6)
	txt6.place(x=230,y=300)


	btn = ttk.Button(window, text="Save", width=20,command=message)
	btn.place(x=100,y=450)
	
	window.mainloop()	

	stri=str(var2.get())
	li=convert_string_to_list(stri)
	t_str=str(var3.get())
	lis = list(t_str.split(":"))
	print(lis)
	t=(int(lis[0])*60*60)+(int(lis[1])*60)+int(lis[2])
	web_str=str(var5.get())
	website_list = list(web_str.split(","))
	print("gone\n")	
	blocker(website_list)
	print("back\n")
	unweb_str=str(var6.get())
	website_lis = list(unweb_str.split(","))
	unblocker(website_lis)
#	print(t)
#	for _ in li:
#		print(_)
	for _ in website_list:
		print(_)
	email=str(var1.get())
	working(li,t,email)
		
if __name__=='__main__':
	#print('abc\n')
	start()
	
	
