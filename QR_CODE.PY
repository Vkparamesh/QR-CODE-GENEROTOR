# Import QRCode from pyqrcode
import pyqrcode 
import png
from pyqrcode import QRCode
#PIP INSTALL pyqrcode

# HERE ENTER THE URS
s = input('enter the url:')

# Generate QR code
url = pyqrcode.create(s)

# SAVE QR COD AS SVG FORMAT AS URL NAME
url.svg(s+'svg', scale = 16)

# SAVE QR COD AS PNG FORMAT AS URL NAME
url.png(s+'.png', scale = 16)
