import qrcode

# Shortened version of the Python code for demonstration purposes
python_code = """
class Menu:
    def __init__(self):
        self.menu_items = {
            "TEA": 10,
            "COFFEE": 10,
            "BISCUIT": [10, 30, 35]
        }

    def display_menu(self):
        print("Menu Items:")
        for item, price in self.menu_items.items():
            if isinstance(price, list):
                print(f"{item}: {', '.join(str(p) for p in price)}")
            else:
                print(f"{item}: {price}")

def main():
    menu = Menu()
    menu.display_menu()

if __name__ == "__main__":
    main()
"""

# Generate the QR code
qr = qrcode.make(python_code)

# Save the QR code to a file
qr.save("cafeteria_management_system_qr.png")

print("QR code generated and saved as 'cafeteria_management_system_qr.png'.")
