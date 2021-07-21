#Import
import ftplib

HOST = '127.0.0.1'
USERNAME = 'ftpuser'
PASSWD = 'owl'

ftp_server = ftplib.FTP(HOST, USERNAME, PASSWD)

ftp_server.encoding = "utf-8"

filename = "csvTest.csv"

textFile = open(filename, 'rb')

ftp_server.storbinary("STOR %s" %filename, textFile)
#ftp_server.storbinary(f'STOR{filename}', textFile)

textFile.close()

ftp_server.quit()
