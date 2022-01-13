
from pygame import mixer
import time
from selenium import webdriver
def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

#x = input("Learn username: ")
#y = input("Learn password: ")
#link = input("Link of the page: ")
#z = input("Keyword to search: ")

x='school number'
y='password.'
z='fghdsfthgfshgfshgf'
link="https://learn.khas.edu.tr/my/" #wanted website link

browser = webdriver.Chrome()

browser.get(link)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(x)
password.send_keys(y)

button = browser.find_element_by_id("loginbtn")
button.click()

body = browser.find_element_by_tag_name("body")
original = body.text
original_list = original.split(" ")

while True:
    browser.get(link)
    html_source = browser.page_source
    body = browser.find_element_by_tag_name("body")
    newer = body.text
    newer_list = newer.split(" ")
    
    if z in html_source or original != newer:
        print("Uyan")
        print(Diff(newer_list, original_list))
        
        mixer.init()
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        time.sleep(20)
    else:
        print("Uyu")

    time.sleep(15)
