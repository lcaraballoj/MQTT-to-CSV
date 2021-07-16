#Import
import ftplib
import csv

HOST = '127.0.0.1'
USERNAME = 'ftpuser'
PASSWD = 'owl'

ftp_server = ftplib.FTP(HOST, USERNAME, PASSWD)

ftp_server.encoding = "utf-8"

filename = "csvTest.csv"

textFile = open(filename, 'rb')

with open(filename, 'wb') as file:
    ftp.write(filename, ftp_server)
