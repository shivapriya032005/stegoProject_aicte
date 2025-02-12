import cv2
import numpy as np

def decrypt_message(image_path, original_message_length, password):
    img = cv2.imread("encryptedImage.png")

    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    message = ""

    pas = input("Enter passcode for decryption: ")
    
    if password == pas:
        for _ in range(original_message_length):
            pixel_value = int(img[n, m, z])  # Convert uint8 to int

            if pixel_value in c:
                message += c[pixel_value]
            else:
                print(f"Error: Unexpected pixel value {pixel_value} detected.")
                return
            
            n += 1
            m += 1
            z = (z + 1) % 3

        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED!")

if __name__ == "__main__":
    img_path = input("Enter the encrypted image path: ")
    msg_length = int(input("Enter the length of the original message: "))
    password = input("Enter the original passcode: ")

    decrypt_message(img_path, msg_length, password)
