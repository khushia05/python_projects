import pywhatkit as k
text="""You can install the qrcode library in Python using the pip package manager by typing the command “pip install qrcode” in the command prompt or terminal.
You can import the library into your Python script and use its functions to create QR codes."""
k.text_to_handwriting(text,"text_to_handwriting.PNG",[0,0,138])
print("------end-----")
