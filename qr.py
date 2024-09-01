import qrcode

# URL of the hosted Python script
url = "https://pastebin.com/your_generated_url"  # Replace with your actual URL

# Generate the QR code
qr = qrcode.make(url)

# Save the QR code to a file
qr.save("cafeteria_management_system_qr.png")

print("QR code generated and saved as 'cafeteria_management_system_qr.png'.")
