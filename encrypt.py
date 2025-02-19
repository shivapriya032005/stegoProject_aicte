import cv2
import numpy as np

def encrypt_message(image_path, message, password, output_image="encryptedImage.png"):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_image, img)
    print(f"Message encrypted and saved as {output_image}")

if __name__ == "__main__":
    img_path = input("Enter the image path: ")
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypt_message(img_path, msg, password)
