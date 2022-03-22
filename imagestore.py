#!/usr/bin/python3
import base64
import mg_python
import sys
import os.path
import wget
import requests
import os
def bintoimg():
   if len(sys.argv) < 3:
      print("Please pass the name of the binary to convert as the second parameter")
      sys.exit(1)
   mg_python.m_set_host(0, yottaadd, int(yottaport), "", "")
   dat=mg_python.m_get(0, "^IMAGES", sys.argv[2], 0)
   if dat == "":
      print("The name of the binary " + sys.argv[2] + " does not exist")
      sys.exit(1)

   key = mg_python.m_order(0, "^IMAGES", sys.argv[2], "")
   byte=""
   while (key != ""):
         byte=byte+ mg_python.m_get(0, "^IMAGES", sys.argv[2],  key)
         key  = mg_python.m_order(0, "^IMAGES", sys.argv[2],  key)
   byte=byte.encode()
   print(byte)
   decodeit = open(sys.argv[2] + '.jpeg', 'wb')
   decodeit.write(base64.b64decode((byte)))

def imgtobin():
   if len(sys.argv) < 3:
      print("Please pass the name of binary to save as the second parameter")
      sys.exit(1)
   if len(sys.argv) < 4:
      print("Please pass the name of image to convert to binary as the third parameter") 
      sys.exit(1)
   mg_python.m_set_host(0, yottaadd, int(yottaport), "", "")
   dat=mg_python.m_get(0, "^IMAGES", sys.argv[2], 0)
   if dat != "":
      print("The name of the binary " + sys.argv[2] + " is already taken")
      sys.exit(1)
   nofile=0
   nolink=0
   file_download=0
   file_exists = os.path.exists(sys.argv[3])
   if file_exists != True:
      nofile=1
      try:
         r = requests.head(sys.argv[3])
         image_formats = ("image/png", "image/jpeg", "image/jpg")
         if r.headers["content-type"] in image_formats: 
            loc = wget.download(sys.argv[3])
            file_download=1
         else:
            print("That link doesn't reference an image file")
            nolink=1
      except:
         nolink=1   
   else:
      loc=sys.argv[3]
   if nolink==1 and nofile==1:
      print("The link/file location doesn't exist")
      sys.exit(1)
   else:
      with open(loc, "rb") as image2string:
         converted_string = base64.b64encode(image2string.read())
   cnt=0
   for x in range(0, len(converted_string), 100):
      print(converted_string[x:x+100])
      mg_python.m_set(0, "^IMAGES", sys.argv[2], cnt, str(converted_string[x:x+100].decode()))
      cnt=cnt+1
   if file_download==1:
      os.remove(loc)
def deletebin():
   if len(sys.argv) < 3:
      print("Please pass the name of the binary to delete from the database as the second parameter")
      sys.exit(1)
   mg_python.m_set_host(0, yottaadd, int(yottaport), "", "")
   result = mg_python.m_delete(0, "^IMAGES", sys.argv[2])
    
if len(sys.argv) < 2:
   print("Please enter either imgtobin, bintoimg or delete as a first paramter")
   sys.exit(1)
yottaadd=os.environ.get('yottaadd','localhost')
yottaport=os.environ.get('yottaport','7041')

if sys.argv[1] == "imgtobin":
   imgtobin()
elif sys.argv[1] == "bintoimg":
   bintoimg()
elif sys.argv[1] == "delete":
   deletebin()
else:
   print("Please enter either imgtobin, bintoimg or delete as a first paramter")
   
