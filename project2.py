import qrcode as qr

def generate_qr_code(data, filename="qrcode.png"):
    try:
        # Create a QRCode object with some custom settings
        qr_code = qr.QRCode(
            version=1,  # The size of the QR code (1 is the smallest)
            error_correction=qr.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # The size of each box in the QR code
            border=4,  # The width of the border (minimum is 4)
        )

        # Add data to the QR code
        qr_code.add_data(data)
        qr_code.make(fit=True)  # Fit the data into the QR code

        # Create an image from the QR codes
        img = qr_code.make_image(fill='black', back_color='white')

        # Save the image to a file
        img.save(filename)
        print(f"QR code saved as {filename}")

    except Exception as e:
        print(f"Error generating QR code: {e}")

# Take user input for the data to encode
user_data = input("Enter the data (URL or text) to encode in the QR code: ")

# Optional: Ask for a custom filename or use default "qrcode.png"
filename = input("Enter a filename for the saved QR code image (default is tmkoc.png): ")
if not filename:
    filename = "tmkoc.png"  # If no filename is provided, use default

# Call the function with the user input
generate_qr_code(user_data, filename)
