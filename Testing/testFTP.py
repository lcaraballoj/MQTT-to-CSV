#Import
import ftplib

HOST = '127.0.0.1'
USERNAME = 'ftpuser'
PASSWD = 'owl'

ftp_server = ftplib.FTP(HOST, USERNAME, PASSWD)

ftp_server.encoding = "utf-8"

filename = "test.txt"

textFile = open(filename, 'rb')

ftp.storbinary(f"STOR {filename}", textFile)
#ftp_server.storbinary(f'STOR{filename}', textFile)

textFile.close()

ftp_server.quit()
