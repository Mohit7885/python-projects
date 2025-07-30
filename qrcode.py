import qrcode

# Data to encode
data = "https://example.com"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (default is 4)
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")

print("QR code generated and saved as 'my_qr_code.png'.")
