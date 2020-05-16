#Python version = 2.*
import base64

# input Filename
# Ex. 'filename.jpg'
f = open('FILENAME','rb')		# open Pic. in binary
f2 = open('base64.txt','w')		# output base64 TXT file

ls_f=base64.b64encode(f.read())		# convert binary code to base64 code

f.close()

f2.write(ls_f)
