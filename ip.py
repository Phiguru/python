#!/bin/env python

# simple public IP extractor

from urllib2 import urlopen
import smtplib, os, getpass
my_ip = urlopen('http://ip.42.pl/raw').read()
print my_ip

# write to file for comparison
testIP = open('/home/happy/ipComp.txt', 'w')
testIP.write(my_ip)
testIP.write("\n")
testIP.close

# set to from and other shiznit

# def sendMe(sendMe):

# fromaddr = "From: happy"
# fromaddr = print getpass.user()
# toaddr = "To: clay@phiguru.net"
# msg = "Subject: Ext IP for Lawrence House \n\n%s" % (my_ip)
# server = smtplib.SMTP('localhost')
# server.set_debuglevel(1)
# server.sendmail(fromaddr, toaddr, msg)
#server.quit()
# return sendMe

# sendMe
