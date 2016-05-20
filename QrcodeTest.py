import uuid

import qrcode
# from PIL import Image
# import easygui


# qrcode.run_example("xzxczxc")
# easygui.egdemo()
# img = qrcode.make("asdklcxzjlcxzlj;zcxj;klcxzjklz")
# print(img)
# img.save('ppwangsousuiimage.png')
import hashlib

m2 = hashlib.md5(bytes('123123','utf-8'))

print(m2.hexdigest())

