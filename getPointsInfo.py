# This file attempts to scrape a username and their points value from Streamlabs
import requests, bs4, html.parser
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#Go to Streamlabs Website
driver.get("https://streamlabs.com/login")
#Go to Twitch Login
buttonLogIn = driver.find_element_by_id('connect-with-twitch')
buttonLogIn.click()
#Fill out Username and Password
buttonUsername = driver.find_element_by_id('username')
buttonUsername.click()
myUsername = input("Please enter your Twitch Username: ")
buttonUsername.send_keys(myUsername)
buttonPassword = driver.find_element_by_name('password')
buttonPassword.click()
myPassword = input("Please enter your Twitch Password: ")
buttonPassword.send_keys(myPassword)
buttonPassword.send_keys(Keys.ENTER)
#Ask for 2-factor auth Token and input it
tokenCode = input("What is the Two-Factor authorization code?: ")
twoFactAuth = driver.find_element_by_id('user-token')
twoFactAuth.send_keys(tokenCode)
twoFactAuth.send_keys(Keys.ENTER)
#Navigate to the SLOBS Extension
input("I need some help. Could you click the x on the screen, then navigate to extensions? Once you do, say anything here :).")
#Make a table to store user info in
acctTable = PrettyTable()
acctTable.field_names = ["Username", "Points"]
buttonNextList = driver.find_element_by_xpath("//div[@id='donation-pagination']/button[2]")
#while(buttonNextList.get_attribute("disabled") == None):
accountTable = driver.find_element_by_class_name('account-table')
accountTbody = accountTable.find_element_by_tag_name('tbody')
for i in range(100):
    userName = accountTbody.find_element_by_class_name('table__name')
    userPoints = accountTbody.find_element_by_class_name('table__message')
    acctTable.add_row([userName, userPoints])
print(acctTable)
#buttonNextList.click()
    #There is an option with PrettyTable to pull from an HTML file. When I pick this back up, that sounds like a good place to go.

#Useful links: http://zetcode.com/python/prettytable/ | https://selenium-python.readthedocs.io/api.html | https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
# https://selenium-python.readthedocs.io/navigating.html | https://selenium-python.readthedocs.io/getting-started.html | https://pybit.es/requests-session.html  |


#Find path for extensions, store it, then get current url, get first x chars until you would navigate it (streamlabs.com/dashboard#/*), then navigate to stored url bit


#res = requests.get('https://streamlabs.com/dashboard#/loyalty')
#res.raise_for_status()
#slobsSoup = bs4.BeautifulSoup(res.text, features = "html.parser")
#type(slobsSoup)
#This now searches the BeautifulSoup object for the info I need via tags
#The smart move here would probably to be generate a dictionary for each name
#We need to bypass the login page
#slUsers = slobsSoup.select('div')
#type(slUsers)
#len(slUsers)
