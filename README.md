# Python-Project

1. The task is to create a small python application ,  so i have created a Captcha Application which we are using in our day to day life. I have used random and String Package .
    Random is to generate the Random captcha using the inputs . String is used for Defining the Data. 
    Example - 1. IRCTC e-ticketing platform shows us the Random Captcha(includes digits, alphabets and Symbols) which should be match with our input while logging in the irctc account.
              2. Google Authenticator application which we are using Professionally as a Multifactor Authentication , which consists of 6 random digits. 

2. I have added Jenkinsfile with different stages to trigger the specified jobs at a particular time. We can Checkout,Build and Cleanup the checkout using this Jenkinsfile.

3. Next , I have added Crontab.sh file , to Complete the Cronjobs which is Clone , create a log file with a naming convention which consists of print last 5 git logs with Author and Modified Files only .
   To trigger the cronjob at 3 PM every day , we need to create a crontab with " 0 15 * * * /crontab.sh " , which will automate the Cronjobs at 3 PM everyday .
