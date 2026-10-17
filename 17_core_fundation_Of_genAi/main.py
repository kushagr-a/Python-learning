import tiktoken # type: ignore[reportMissingImports]

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, how are you doing today? I hope you're having a great day!"
token = enc.encode(text)  # This will return a list of token IDs

print("Token IDs:", token)

tokenG = [13225, 11, 1495, 553, 481, 5306, 4044, 30, 357, 5498, 7163, 4566, 261, 2212, 2163, 0]
decoded_text = enc.decode(tokenG)  # This will convert the token IDs back to the original text

print("Decoded Text:", decoded_text)