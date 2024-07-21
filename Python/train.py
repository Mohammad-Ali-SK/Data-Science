import qrcode as q

img = q.make("https://www.facebook.com/")
img.save("img.png")