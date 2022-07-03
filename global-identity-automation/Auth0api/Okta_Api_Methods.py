import time
import urllib

import requests

from PageObject.SSOSignin import SSOSignin
from utilities.BaseClass import BaseClass
from utilities.ExcelUtilClass import ExcelUtil
from utilities.HelperClass import Helper


class OKTALib(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    def createUserOkta(self, Fname, Lname, email, login, password, securityQuestion, Answer):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'api/v1/users?activate=true'
        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }
        body={
                  "profile": {
                    "firstName": "'"+Fname+"'",
                    "lastName": "'"+Lname+"'",
                    "email": "'"+email+"'",
                    "login": "'"+login+"'"
                  },
                  "credentials": {
                    "password" : { "value": "'"+password+"'" },
                    "recovery_question": {
                      "question": "'"+securityQuestion+"'",
                      "answer": "'"+Answer+"'"
                    }
                  }
                }


        responseAuth0 = requests.post(baseUrl, headers=headersAuth, json=body)
        response = responseAuth0.json()
        return response


    def changePasswordOkta(self, oldpassword, newPassword, userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/credentials/change_password'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }
        body={
              "oldPassword": { "value": "{{"+oldpassword+"}}" },
              # "newPassword": { "value": "uTVM,TPw55" }
            "newPassword": {"value": ""+newPassword+""}
            }


        responseAuth0 = requests.post(baseUrl, headers=headersAuth, json=body)
        response = responseAuth0.json()
        return response



    def activateUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/activate?sendEmail=false'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response


    def deactivateUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/deactivate'
        #https://dev-491287.oktapreview.com/api/v1/users/00u11t2nj4gWPivkL0h8/lifecycle/deactivate

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def unlockUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/unlock'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        # log.info(responseAuth0.status_code)
        # response = responseAuth0.json()
        return responseAuth0

    def expirePasswordOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/expire_password'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response


    def resetPasswordOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/reset_password?sendEmail=false'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response


    def setTempPasswordOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/expire_password?tempPassword=true'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def suspendUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/suspend'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def suspendUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/suspend'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def unsuspendUserOkta(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'/api/v1/users/'+userID+'/lifecycle/unsuspend'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def clearUserSessions(self,  userID):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL+'api/v1/users/'+userID+''

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
        }

        responseAuth0 = requests.delete(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response

    def getCurentUser(self):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL", "okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL + 'api/v1/users/me'


        log.info(baseUrl)


        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
            'Accept':'application/json',
            'Content-Type':'application/json'
        }

        responseAuth0 = requests.get(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response


    def verifyOKTALoggedinSessions(self):
        helper = Helper()
        log = self.getLogging()

        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        oktaHomePageURL = str(helper.getDataFromConfig("OKTA", "oktaHomePageURL","okta-api-config.ini"))
        try:
            mainWindow = self.driver.current_window_handle
            log.info(mainWindow)
            self.openNewTab(self.driver, oktaURL)
            childwindow = self.driver.window_handles[1]
            log.info(self.driver.window_handles[0])
            log.info(self.driver.window_handles[1])
            if mainWindow not in childwindow:
                self.driver.switch_to.window(self.driver.window_handles[1])

                log.info(str(self.driver.current_url) + "Link is opening in new tab")
                currentURL = str(self.driver.current_url)

                # self.assertForValidation(str(self.driver.current_url),oktaHomePageURL, "Okta session is not active" )
                # result = currentURL.find(oktaHomePageURL)

                if (currentURL.find(oktaHomePageURL) != -1):
                    print("Okta session is not active active")
                    self.assertForValidation(str(self.driver.current_url), oktaHomePageURL,
                                             "Okta session is not active")
                else:
                    print("Okta session is active active")


                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
            log.info(self.driver.current_url)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            log.info(errc)


    def LogoutOktaSession(self):
        helper = Helper()
        log = self.getLogging()
        ssoSignin=SSOSignin(self.driver)

        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL","okta-api-config.ini"))
        oktaHomePageURL = str(helper.getDataFromConfig("OKTA", "oktaHomePageURL","okta-api-config.ini"))
        try:
            mainWindow = self.driver.current_window_handle
            log.info(mainWindow)
            self.openNewTab(self.driver, oktaURL)
            childwindow = self.driver.window_handles[1]
            # log.info(self.driver.window_handles[0])
            # log.info(self.driver.window_handles[1])
            if mainWindow not in childwindow:
                self.driver.switch_to.window(self.driver.window_handles[1])

                log.info(str(self.driver.current_url) + "Link is opening in new tab")
                currentURL = str(self.driver.current_url)
                # self.assertForValidation(str(self.driver.current_url),oktaHomePageURL, "Okta session is not active" )
                if (currentURL.find(oktaHomePageURL) != -1):
                    print("Okta session is not  active")
                    self.assertForValidation(str(self.driver.current_url), oktaHomePageURL,
                                             "Okta session is not active")
                else:
                    print("Okta session is  active")
                time.sleep(2)
                ssoSignin.clickuserMenuHomePage()
                time.sleep(1)
                ssoSignin.clicksignutButtonHomePage()
                time.sleep(1)
                self.driver.close()

                self.driver.switch_to.window(self.driver.window_handles[0])
            log.info(self.driver.current_url)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            log.info(errc)

    def getUserByEmail(self, Email):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL", "okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))
        baseUrl = oktaURL + 'api/v1/users/'+Email+''

        # log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        responseAuth0 = requests.get(baseUrl, headers=headersAuth)
        response = responseAuth0.json()
        return response


    def updateUserProfile(self, userID, Fname,Lname, Email, MobileNumber):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL", "okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))

        baseUrl = oktaURL + 'api/v1/users/'+userID+''

        log.info(baseUrl)
        log.info(MobileNumber)


        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        body ={
                "profile": {
                    "firstName": Fname,
                    "email": Email,
                    "mobilePhone": MobileNumber,
                    "lastName": Lname,
                    "secondEmail": None,
                    "login": Email
                }
        }

        responseAuth0 = requests.post(baseUrl, headers=headersAuth, json=body)
        response = responseAuth0.json()
        return response


    def updatecurrentUserProfile(self,  Fname,Lname, Email, MobileNumber):
        helper = Helper()
        log = self.getLogging()
        oktaURL = str(helper.getDataFromConfig("OKTA", "oktaURL", "okta-api-config.ini"))
        apiKey = str(helper.getDataFromConfig("OKTA", "ApiToken", "okta-api-config.ini"))

        baseUrl = oktaURL + '/api/v1/users/me'

        log.info(baseUrl)

        headersAuth = {
            'Authorization': 'SSWS ' + str(apiKey),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        body ={
                "profile": {
                    "firstName": "'"+Fname+"'",
                    "email": "'"+Email+"'",
                    "mobilePhone": "'"+MobileNumber+"'",
                    "lastName": "'"+Lname+"'",
                    "secondEmail": 'null',
                    "login": "'"+Email+"'"
                }
        }


        responseAuth0 = requests.post(baseUrl, headers=headersAuth, json=body)
        response = responseAuth0.json()
        return response


