import qrcode as qr                                                        # imports library that generates QR code --> qr : alias (nickname)
img = qr.make("https://www.youtube.com/channel/UC3XBkDeCVXCoCofFgfUZXGw")  #.make : creates QR code
img.save("KaranAujla_youtube.png")                                         # saves the image of the qrcode

