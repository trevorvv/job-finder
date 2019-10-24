## TODO - find out about how to scraped data to the sendEmail method
## TODO - 

# get_attribute('href') to get the URL of the post 
#
# div[contains(., "Desired text")]
# div[starts-with(., "Desired text")]

# imports required
import json
import smtplib
from selenium import webdriver
from email.mime.multipart import MIMEMultipart

# load the json object
with open('config.json', 'r+') as f:
    data = json.load(f)

# do not forget this variable is going to change depending on the OS/computer
# set the path variable
path = data['config']['chrome_driver']

# main function
def main():
    # array to hold the information / links for the jobs 
    tester()

# method just to test 
def tester():
    driver = webdriver.Chrome(executable_path=path)
    driver.get(data['urls']['frcc'])
    driver.find_elements_by_xpath("//div[contains(@class, 'HR')]").get_attribute('href')
    driver.find_elements_by_xpath("//div[contains(@class, 'Human Resources')]").get_attribute('href')
    

# function to send the email 
## TODO find out about how to pass info into the data
def sendEmail():
    try:
        # set up the SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(data['emails']['myEmail'], data['emails']['password'])
        # create the message
        msg = MIMEMultipart()
        msg['From'] = data['emails']['myEmail']
        msg['To'] = data['emails']['kelsEmail']
        msg['Subject'] = "Here are your job listings for the day!"
        # send the email
        s.send_message(msg)
        del msg
        s.quit()
    except: 
        pass

# driver
if __name__ == "__main__":
    # execute only if run as a script
    main()