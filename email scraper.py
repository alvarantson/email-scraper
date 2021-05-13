from re import findall
from selenium import webdriver
import tkinter as tk
import time

from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Emaili kaabits")

        self.label = Label(master, text="\nSammud et programm jookseks normaalselt:\n\n"+
        	"1) käivitatud failiga samas kaustas chromedriver.exe\n"+
        	"2) käivitatud failiga samas kaustas sites.txt\n\n"+
        	"sites.txt kaabitavad saidid üksteise alla\n\n"+
        	"chromedriver.exe sõltub sinu google chromei versioonist\n\n"+
        	"siit saad chromei versiooni vaadata:\nchrome://settings/help\n\n"+
        	"siit saad õige ver tõmmata:\nhttps://chromedriver.chromium.org/downloads\n\n"+
        	"tulemused salvestavad käivitatud failiga samasse kausta result.txt faili!\n\n\n"+
        	"Kui selle akna kinni paned, programm käivitub!\n\n")
        self.label.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

with open("sites.txt","r") as fm:
	urls = [i.strip() for i in fm.read().split("\n")]

emails = []
for url in urls:
	driver.get(url)
	time.sleep(1)

	text = driver.find_element_by_tag_name('body').text
	variants = [
		["@","+@"],
		["[at]","\[at\]"],
		["[ät]","\[ät\]"],
		["[ at ]","\[ at \]"],
		["[ ät ]","\[ ät \]"],
		[" [at] "," \[at\] "],
		[" [ät] "," \[ät\] "],
		[" [ at ] "," \[ at \] "],
		[" [ ät ] "," \[ ät \] "]
	]
	for var in variants:
		emails += [i.replace(var[0],"@") for i in findall('[\w\.-]'+var[1]+'[\w\.-]+',text)]

#for email in emails:
#	print(email)

with open("result.txt", "w") as fm:
	fm.write("\n".join(emails))

driver.quit()