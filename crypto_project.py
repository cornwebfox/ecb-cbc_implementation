from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import cv2
import numpy
from PIL import Image
import os
import argparse
from pathlib import Path
enc_mode = AES.MODE_ECB #encrypt using ECB
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

required_arg = optional.add_argument('--cbc',action='store_true', help="use CBC mode of encryption instead of default ECB")

required.add_argument(
    "--input",
    type=Path,
    default=Path(__file__).absolute().parent / "data",
    help="Path to the data directory",
)
#parser.add_argument('--ecb' , action='store_true')
#parser.add_argument('--cbc', action='store_true', help="use CBC mode of encryption instead of default ECB")

p = parser.parse_args()

parser._action_groups.pop()
if enc_mode == AES.MODE_ECB:
    iv_size = AES.block_size
else:
    iv_size = 0

# Loading image for encryption
img_source  = cv2.imread(str(p.input)) #image path here
rawig, pillar, depof = img_source.shape

# Convert original image data to bytes
img_sourceBytes = img_source.tobytes()

# Encryption procecss
key = get_random_bytes(32)
iv = get_random_bytes(iv_size)
if p.cbc: #true if encryption mode is CBC
    cipher = AES.new(key, AES.MODE_CBC, iv) 
else: #case for ECB
    cipher = AES.new(key, AES.MODE_ECB)

img_sourcepadded = pad(img_sourceBytes, AES.block_size) #padding 
ciphertext = cipher.encrypt(img_sourcepadded) #encrypting image using padded source now

size_padded = len(img_sourcepadded) - len(img_sourceBytes)
void = pillar * depof - iv_size - size_padded
iv_ciphervoid = iv + ciphertext + bytes(void)
final_image = numpy.frombuffer(iv_ciphervoid, dtype = img_source.dtype).reshape(rawig + 1, pillar, depof)

# save the encrypted image
if p.cbc:
    cv2.imwrite("final_result_cbc.bmp", final_image)
    print("Encryption process has been finished, end image path: " + os.path.abspath(os.getcwd()) + "/final_result_cbc.bmp" )

elif enc_mode == AES.MODE_ECB:
    cv2.imwrite("final_result_ecb.bmp", final_image)
    print("Encryption process has been finished, end image path: " + os.path.abspath(os.getcwd()) + "/final_result_ecb.bmp" )
