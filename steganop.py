import cv2  
import numpy as np  
import types  
  
def msg_to_bin(msg):  
    if type(msg) == str:  
        return ''.join([format(ord(i), "08b") for i in msg])  
    elif type(msg) == bytes or type(msg) == np.ndarray:  
        return [format(i, "08b") for i in msg]  
    elif type(msg) == int or type(msg) == np.uint8:  
        return format(msg, "08b")  
    else:  
        raise TypeError("Input type not supported")  
  
  
  
  

  
  
  
def encodeText():  
    img_name = input("Enter image name (with extension): ")  
    img = cv2.imread(img_name)  
    print("The shape of the image is: ", img.shape)   
    print("The original image is as shown below: ")  
    data = input("Enter data to be encoded: ")  
    file_name = input("Enter the name of the new encoded image (with extension): ")  
    nBytes = img.shape[0] * img.shape[1] * 3 // 8  
    print("Maximum Bytes for encoding:", nBytes)   
    secret_msg =data+ '#####'        
    dataIndex = 0  
    bin_secret_msg = msg_to_bin(secret_msg)
    dataLen = len(bin_secret_msg)
    for values in img:  
        for pixels in values:  
            r, g, b = msg_to_bin(pixels)  
            if dataIndex < dataLen:  
                pixels[0] = int(r[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1  
            if dataIndex < dataLen:
                pixels[1] = int(g[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1  
            if dataIndex < dataLen:
                pixels[2] = int(b[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1  
            if dataIndex >= dataLen:  
                break
    cv2.imwrite(file_name,img)
def decodeText():  
    img_name = input("Enter the name of the Steganographic image that has to be decoded (with extension): ")  
    img = cv2.imread(img_name)    
    print("The Steganographic image is as follow: ")  
    bin_data = ""
    for values in img:  
        for pixels in values:  
            r, g, b = msg_to_bin(pixels)  
            bin_data += r[-1]
            bin_data += g[-1]  
            bin_data +=b[-1]
    allBytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]  
    decodedData = ""
    for bytes in allBytes:  
        decodedData += chr(int(bytes, 2))  
        if decodedData[-5:] == "#####":
            break  
    return decodedData[:-5]
      
  

def steganography():  
    n = int(input("Image Steganography \n1. Encode the data \n2. Decode the data \n Select the option: "))  
    if (n == 1):  
        print("\nEncoding...")  
        encodeText()  
    elif (n == 2):  
        print("\nDecoding...")  
        print("Decoded message is " + decodeText())  
    else:  
        raise Exception("Inserted value is incorrect!")  
  
steganography()
