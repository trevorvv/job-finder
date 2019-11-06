# TODO - find out about how to scraped data to the sendEmail method

# imports required
import json
import smtplib
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart


# load the json object
with open('config.json', 'r+') as f:
    data = json.load(f)

# do not forget this variable is going to change depending on the OS/computer
# set the path variable
path = data['config']['chrome_driver']


# method just to test
def scanning():
    driver = webdriver.Chrome(executable_path=path)
    for names, urls in data['urls'].items():
        driver.get(urls)
        try:
            hr = driver.find_element(By.XPATH, "//*[contains(text(), 'HR')]").get_attribute('href')
            if hr:
                sendEmail(urls)
            else:
                continue
        except:
            continue


# function to send the email
# TODO - set up the smtp to send emails
def sendEmail(x):
    date = datetime.date.today().strftime("%B" + " " + "%d" + " " + "%Y")
    try:
        # set up the SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(data['emails']['senderEmail'], data['emails']['password'])
        # create the message
        msg = MIMEMultipart()
        msg['From'] = data['emails']['senderEmail']
        msg['To'] = data['emails']['kelsEmail']
        msg['Subject'] = "Here are your job listings for " + date + "!"
        msg.attach(x)
        # send the email
        s.send_message(msg)
        del msg
        s.quit()
    except:
        pass


# main function
def main():
    # array to hold the information / links for the jobs
    scanning()


# driver
if __name__ == "__main__":
    # execute only if run as a script
    main()
