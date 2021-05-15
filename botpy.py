import tweepy
import time
import pandas as pd
from datetime import datetime
import ntplib
import datetime, time


def getdatframe():
    return pd.read_csv("/home/rohit/twetdata1.csv") 

def Authentication():
    consumer_key ="Rmj8rj39BPhSCcrxMwgCsWbOM"
    consumer_secret ="RxkWMWRu1scomTE5bkXHrq62sDnQeqfgVhS796l8byR1gxP4Ip"
    access_token ="1357107488886198272-MzCO3owoEKmwlBnhB6PTL6T5F24O8N"
    access_token_secret ="5EGaRDjFE1aJ99sNJdAUYgcGp5nshMmzuTkUbcZgS88e3"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def driver(api,df):
     for tweet in df["tweet"]:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        Time = str(datetime.datetime.fromtimestamp(response.tx_time).strftime("%H:%M") )
        time.sleep(5)
        api.update_status(status =tweet)
        print("Done")
        if (Time=="02:26"):
            print("Good bye times up")
            break

if __name__=="__main__":
    while(True):
        df=getdatframe()
        api=Authentication()
        driver(api,df)
        break

