import requests
from datetime import datetime

while(True):
    try:
        url = input("Please give a valid url: ")
        with requests.get(url) as response:
            for header in response.headers:
                print("{} : {}".format(header, response.headers[header]))
            s_soft = response.headers.get('server')
            print("\nThe software used by the web server is : ", s_soft)
            if not response.cookies:
                print("There are no cookies being used by the website")
            else:
                print("\n{} cookies are being used by the website".format(str(len(response.cookies))))
                for cookie in response.cookies:
                    print("\nCookie name : ", cookie.name)
                    expires = cookie.expires
                    print("Cookie expires on : ", datetime.fromtimestamp(expires))
            reply = input("\nWanna try a different url (y/n)?")
            if reply == 'n':
                exit(1)
    except:
            print("This is not a valid url. Please give another one")
