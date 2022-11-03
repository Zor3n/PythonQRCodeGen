import pyqrcode

##automatic generation

# qr_code = pyqrcode.create('YOUR LINK')
# qr_code.png('code/QR_NAME.png', scale=5) #pip install pypng
# qr_code.show()

##manual geneartion

link = input('Please, enter your link: ')
image_name = input('Please, enter a name: ')
qr_code = pyqrcode.create(link)
qr_code.png(f'code/{image_name}.png', scale=5)
qr_code.show()