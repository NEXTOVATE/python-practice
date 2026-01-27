#write a program to creat a qrcode generator.

#flow ==>  import module   input url ---->     qrcode.png  ---->         save qrcode ---->   qrcode created successfully   



import qrcode

url = input("Enter th url :")

img = qrcode.make(url)

img.save("qrcode.png")
print("qrcode created successfully")

































