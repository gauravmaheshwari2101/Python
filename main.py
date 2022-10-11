#Importing the Package
import random
import string

print('Hello, Your new Captcha is ..!!')
#Length of Captcha
length = 6

#string module is used for defining the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combining the data and store the data
combination = lower + upper + num + symbols

#random module to finally generate the captcha.
temp = random.sample(combination,length)
captcha = "".join(temp)

#printing the captcha
print(captcha)
