def first_name():
    print("this is a first name !")

import emoji

# Sample text with emojis
text_with_emojis = 'I love Python! '

# Convert emojis to text
text_with_text = emoji.demojize(text_with_emojis)

print('Original Text:', text_with_emojis)
print('Text with Emojis Converted to Text:', text_with_text)