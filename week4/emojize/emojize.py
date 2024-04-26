import emoji

# Using emoji library to convert emojis from words to the actual emoji eg :thumbsup: - 👍
in_put = input("Input: ")
output = emoji.emojize(in_put, language = 'alias')

print("Output:", output)

