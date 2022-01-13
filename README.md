# Cryptoproject

Python implementation of ECB-penguin concept
## Dependencies 

```bash
opencv-python==4.5.2.52
pycryptodome==3.12.0
numpy==1.20.3
```

## Installation

Tool can be installed using git.

```bash
git clone https://github.com/cornwebfox/ecb-cbc_implementation
cd ecb-cbc_implementation
pip3 install -r requirements.txt
```

## Usage
Run AES-ECB encryption of image
```bash
python3 crypto_project.py --input IMAGE DIRECTORY
```
Run AES-ECB encryption of image
```bash
python3 crypto_project.py --cbc --input IMAGE DIRECTORY
```
