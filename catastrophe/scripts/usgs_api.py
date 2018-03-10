#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:39:42 2018

@author: satyam


"""
import os
import sys
"""
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'catastrophe.settings'
"""
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.distance import vincenty

from django.contrib.auth.models import User
from disasterApp.models import Profile

import time
import datetime
import urllib.request, json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

period=500#the minutes of period for checking 
users = Profile.objects.all()

def send_email(email,mag,time,source,depth,distance):
    print(email)
    from_id="rizeni.katastrof@gmail.com"
    to_id=email
    password="asdf@1234"
    subject="Earthquake Warning Notification"
    body="There was earthquake of "+"magnitude "+str(mag)+" at "+str(time)+" at distance of "+str(distance)+"km from your location."
    msg = MIMEMultipart()
    msg['From']=from_id
    msg['To']=to_id
    msg['Subject']=subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)	# This is if the sender's email is gmail
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_id, password)
    text = msg.as_string()
    server.sendmail(from_id, to_id, text)
    server.quit()
    #write email writing code    
while(True):
    a=datetime.datetime.utcnow() - datetime.timedelta(minutes=period)
    a=a.isoformat()
    usgs_url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+a+"&minmagnitude=4"
    print(usgs_url)
    """
    for i in users:
        location = geolocator.geocode(i.location)
        print(location)
    """
    with urllib.request.urlopen(usgs_url) as url:
        data = json.loads(url.read().decode())
        #print(data)
    earthquake_data = []
    earthquake_list = data["features"]
    print(earthquake_list[0])
    earthquake_list.append({'properties': {'updated': 1520702073040, 'mmi': None, 'type': 'earthquake', 'net': 'us', 'tsunami': 0, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us1000d2sx', 'ids': ',us1000d2sx,', 'gap': 121, 'time': 1520698713230, 'place': '81km SSW of Pagan, Northern Mariana Islands', 'mag': 4, 'types': ',geoserve,origin,phase-data,', 'title': 'M 4.0 - 81km SSW of Pagan, Northern Mariana Islands', 'detail': 'https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us1000d2sx&format=geojson', 'nst': None, 'sig': 246, 'alert': None, 'rms': 0.63, 'dmin': 2.214, 'magType': 'mb', 'status': 'reviewed', 'felt': None, 'code': '1000d2sx', 'sources': ',us,', 'tz': 600}, 'geometry': {'coordinates': [77.8880002, 29.8542626, 362.32], 'type': 'Point'}, 'type': 'Feature', 'id': 'us1000d2sx'})
    for each_quake in earthquake_list:
        temp_tuple = (each_quake["properties"]["mag"], each_quake["properties"]["time"], each_quake["geometry"]["coordinates"])
        quake_time=datetime.datetime.fromtimestamp(each_quake["properties"]["time"]/1000).strftime('%Y-%m-%dT%H:%M:%SZ')
        print(quake_time)
        source=(each_quake["geometry"]["coordinates"][1],each_quake["geometry"]["coordinates"][0])
        for u in users:
            location = geolocator.geocode(u.location)
            dest=(location.latitude, location.longitude)
            distance=vincenty(source,dest).km
            if(distance<100 and u.email!=None):
                send_email(u.email,each_quake["properties"]["mag"],quake_time,source,each_quake["geometry"]["coordinates"][2],distance)
        earthquake_data.append(temp_tuple)
    time.sleep(120)
#tmp=User.objects.all()