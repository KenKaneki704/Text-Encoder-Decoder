import string


# Text Encoder 
text = input("Text: ")
text_encoded = text.encode("utf_16")

print(f"Encoded Text: {text_encoded}")

# Text Decoder
text = input("Text: ")
text_decoded = text_encoded.decode("utf_16")

print(f"Encoded Text: {text_decoded}")
