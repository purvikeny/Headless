import time
import urllib

import requests

from utilities.BaseClass import BaseClass
from utilities.ExcelUtilClass import ExcelUtil
from utilities.HelperClass import Helper


class Auth0Lib(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    def get_AccessToken(self, tenet):
        baseUrl = 'https://monotypeidp-'+tenet+'.us.auth0.com/oauth/token'
        log = self.getLogging()
        helper = Helper()

        body={
            "grant_type":"client_credentials",
            "client_id":helper.getDataFromAuthIni("AUTH0", "ClientId_test"),
            "client_secret":helper.getDataFromAuthIni("AUTH0", "Client_Secret_key_Test"),
            "audience":'https://monotypeidp-'+tenet+'.us.auth0.com/api/v2/'
        }

        responseAuth0 = requests.post(baseUrl, json=body)
        accessToken = responseAuth0.json()['access_token']
        # log.info(accessToken)
        return accessToken

    def getClientID(self, token, tenet, applicationName):
        log = self.getLogging()
        clientURL = 'https://monotypeidp-'+tenet+'.us.auth0.com/api/v2/clients'

        headers={
            'Authorization':'Bearer '+''+token+''
        }

        responseAuth0 = requests.get(clientURL, headers=headers)
        jsonResponseAuth0 = responseAuth0.json()
        # log.info(jsonResponseAuth0)

        for emailKey in jsonResponseAuth0:
            tenant = emailKey['tenant']
            clientId = emailKey['client_id']
            name = emailKey['name']

            dictAuth0name = name
            dictAuth0clientID= clientId

            try:
                if dictAuth0name == applicationName:
                    return dictAuth0clientID
            except:
                print('Data not found')


    def logoutUser(self, tenet, applicationName):

        log = self.getLogging()
        ap = Auth0Lib(self.driver)
        token = ap.get_AccessToken(tenet)
        clientId = ap.getClientID(token, tenet, applicationName)

        URL = "https://secure-"+tenet+".monotype.com/v2/logout?client_id=" + clientId + ""

        log.info(URL)

        try:
            self.openNewTab(self.driver, URL)

            mainWindow = self.driver.current_window_handle
            log.info(mainWindow)
            childwindow = self.driver.window_handles[1]
            log.info(self.driver.window_handles[0])
            log.info(self.driver.window_handles[1])
            if mainWindow not in childwindow:
                self.driver.switch_to.window(self.driver.window_handles[1])

                log.info(self.driver.current_url)
                log.info(str(self.driver.current_url) + "Link is opening in new tab")

                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])

            log.info(self.driver.current_url)


            # x = requests.get(URL)
            # log.info(x.text)

            # self.driver.get(URL)
        except requests.exceptions.ConnectionError as errc:

            print(errc)
            log.info(errc)

    def logoutApp(self, env):
        helper = Helper()
        log = self.getLogging()
        clientid = helper.getDataFromAuthIni(env, 'ClientId')
        logoutURL = helper.getDataFromAuthIni(env, 'logoutURL').replace('clientid', clientid)
        try:

            mainWindow = self.driver.current_window_handle
            log.info(mainWindow)
            self.openNewTab(self.driver, logoutURL)
            childwindow = self.driver.window_handles[1]
            # log.info(self.driver.window_handles[0])
            # log.info(self.driver.window_handles[1])
            if mainWindow not in childwindow:
                self.driver.switch_to.window(self.driver.window_handles[1])
                log.info(self.driver.current_url)
                log.info(str(self.driver.current_url) + "Link is opening in new tab")
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
            log.info(self.driver.current_url)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            log.info(errc)

    def get_User_APi(self, tenet, token, email):

        encodedEmail = urllib.parse.quote(email, safe='')
        baseUrl = 'https://secure-'+tenet+'.monotype.com/api/v2/users?q=email:'+encodedEmail+'&search_engine=v3'

        log = self.getLogging()

        headers = {
            'Authorization':'Bearer '+''+token+''
        }

        responseAuth0 = requests.get(baseUrl, headers=headers)

        return responseAuth0

    def getdatafromResponse(self, json, object):
        for emailKey in json:
            value = emailKey[''+object+'']
        return value


    def get_delete_user(self, tenet, token, userID):
        baseUrl = 'https://secure-'+tenet+'.monotype.com/api/v2/users/'+userID+''

        log = self.getLogging()

        headers = {
            'Authorization': 'Bearer ' + '' + token + ''
        }
        responseAuth0 = requests.delete(baseUrl, headers=headers )
        return responseAuth0


    def get_User_By_Id(self, tenet, token, userID):

        # encodedEmail = urllib.parse.quote(email, safe='')
        baseUrl = 'https://secure-'+tenet+'.monotype.com/api/v2/users/'+userID+''

        log = self.getLogging()

        headers = {
            'Authorization':'Bearer '+''+token+''
        }

        responseAuth0 = requests.get(baseUrl, headers=headers)

        return responseAuth0

