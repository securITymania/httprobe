#!/usr/bin/python

#This script is used to detect the domain is accepting HTTP or HTTPS connection

#You can pass Sub-domaina list as input

#Bugbounty collection script



import requests

from urlparse import urlparse

from threading import Thread

import urllib2

import sys

import argparse

from Queue import Queue





parser = argparse.ArgumentParser()

parser.add_argument("-l","--list", help="Give subdomains list file as input ",action="store_true")

parser.add_argument("file")



if len(sys.argv) < 2:

    parser.print_usage()

    sys.exit(1)

    

args = parser.parse_args()



hosts = args.file











   



concurrent = 200



def doWork():

   while True:

       url = q.get()

       url = getStatus(url)

       doSomethingWithResult(url)

       q.task_done()



def getStatus(ourl):

   try:

       res = requests.get("http://"+ourl)

       return res.url

   except:

       return "error", ourl



def doSomethingWithResult(url):

   print(url)



q = Queue(concurrent * 2)

for i in range(concurrent):

   t = Thread(target=doWork)

   t.daemon = True

   t.start()

try:

    for url in open(hosts,'r'):

       q.put(url.strip())

    q.join()

except KeyboardInterrupt:

   sys.exit(1)

