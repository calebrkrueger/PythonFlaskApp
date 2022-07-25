# Importing library
import qrcode

# Data to encode
data = input("What would you like to encode?")

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

# Adding data to the instance 'qr'
qr.add_data(data)

# Add data to QR code and style it accordingly


qr.make(fit=True)
img = qr.make_image(fill_color='black',
                    back_color='white')

img.save('MyQRCode2.png')