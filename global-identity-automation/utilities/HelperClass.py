import random
import string
import time
import os
import sys
import os.path
import datetime
import shutil
from configparser import ConfigParser
from pathlib import Path


from configparser import ConfigParser
from pathlib import Path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
from PIL import Image, ImageChops
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



class Helper(BaseClass):
    def getHighlightElement(element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("background: green; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)

    def getRandomString(self, length):
        key = ''
        for i in range(length):
            key += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        return key

    def getRandomEmail(self, randomString):
        email = randomString + "_automation@emailers.com"
        return email

    def getDataFromAppConfigIni(self, section, key):
        return self.getDataFromConfig(section, key, "app-config.ini")

    def getDataFromAuthIni(self, section, key):
        return self.getDataFromConfig(section, key, "auth0-api-config.ini")

    def getDataFromConfig(self, section, key, file):
        dirpath = Path(__file__).parent.parent
        configur = ConfigParser()

        path = Path.joinpath(dirpath, file)

        configur.read(path)
        # print("Section===========", section)
        # print("key===========", key)
        return configur.get(section, key)

    # def performImageComparision(self, referneceimage, actualimage):
    #     logger = self.getLogging()
    #     image1 = cv2.imread(self.getDataFromConf("STAGING", "referneceImagePath")+referneceimage)
    #     image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    #     histogram = cv2.calcHist([image], [0],
    #                              None, [256], [0, 256])
    #     image2 = cv2.imread(self.getDataFromConf("STAGING", "actualImagePath")+actualimage)
    #     image = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    #
    #     histogram1 = cv2.calcHist([image], [0],
    #                               None, [256], [0, 256])
    #     c1 = 0
    #     i = 0
    #     while i < len(histogram) and i < len(histogram1):
    #         c1 += (histogram[i] - histogram1[i]) ** 2
    #         i += 1
    #     logger.info(c1)
    #     print(c1)
    #     c1 = c1 ** (1 / 2)
    #     c1=int(c1)
    #     logger.info(c1)

        #self.assertForValidatingNumber( 0, c1, "Image Comparision is done successfully",
                                                 #"Couldn't match two images while comparision")

    def compareImage(self, referneceimage, actualimage):
        img1 = Image.open(self.getDataFromConf("STAGING", "actualImagePath") + actualimage).convert('RGB')
        img2 = Image.open(self.getDataFromConf("STAGING", "referneceImagePath") + referneceimage).convert('RGB')
        diff = ImageChops.difference(img2, img1)
        print(diff.getbbox())
        self.getLogging().critical(diff.getbbox())
        if diff.getbbox():
            self.getLogging().critical("images are different")
        else:
            self.getLogging().critical("images are same")



    def actionOnPopUp(self):
        try:
            obj = self.driver.switch_to.alert
            action = ActionChains(self.driver)
            action.send_keys(Keys.ESCAPE).perform()
        except:
            logger = self.getLogging()
            logger.info("Alert not found.")

        # try :
        #     if len(element) > 0:
        #         if action == "click":
        #             element.click()
        #         elif action == "esc":
        #             action = ActionChains(self.driver)
        #             action.send_keys(Keys.ESCAPE).perform()
        # except:
        #     logger = self.getLogging()
        #     logger.info("Exception is Element not found.")

    def send_email(email_recipient,
                   email_subject,
                   email_message,
                   attachment_location,
                   email_sender,login,password):



        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_recipient
        msg['Subject'] = email_subject

        msg.attach(MIMEText(email_message, 'plain'))

        if attachment_location != '':
            filename = os.path.basename(attachment_location)
            attachment = open(attachment_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= %s" % filename)
            msg.attach(part)

        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.login(login, password)
            text = msg.as_string()
            server.sendmail(email_sender, email_recipient, text)
            print('email sent')
            server.quit()
        except:
            print("SMPT server connection error")
        return True

    def getTimeStampStr(self):
        ct = datetime.datetime.now()

        return ct.__str__()

    def copyBtwDir(self,src,dest):
        shutil.copy(src, dest)

    def getfileNameWOExt(self,filepath):
        base = os.path.basename(filepath)
        return os.path.splitext(base)[0]

    def getfileNameWExt(self,filepath):
        return os.path.basename(filepath)

