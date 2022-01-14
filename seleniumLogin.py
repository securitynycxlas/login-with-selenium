# Automating any login panel using selenium and python
# by: scr1pt (nycxlas)

# Import webdriver for selenium
from selenium import webdriver

# Import the ENTER key
from selenium.webdriver.common.keys import Keys

# Import the password input in command prompt
from getpass import getpass


# Your username and password input
logUser = input("Type your username: ") #Example: "scr1ptxzy"
logPass = getpass("Type your password: ") #Example "123"


# Setting browser variable name
driver = webdriver.Chrome();
driver.get("<Website for login>"); #Example: https://twitter.com/


# Login input
driver.find_element_by_name("Username input element name").send_keys(logUser) #Example: txtUsr
driver.find_element_by_name("Password input element name").send_keys(logPass) #Example: txtPass


# Send enter for login
driver.find_element_by_name("Password input element name").send_keys(Keys.RETURN)
