#Code that takes an emoji name and converts it to the actual emoji, using a library of emojis and their associated name

import emoji #Import emoji module which we use to convert

emoji_name = input("Enter emoji text: ") #Prompt user for input

print(emoji.emojize(emoji_name, language='alias')) #Convert either ':emoji_name:' or ':emojiname:' into the actual emoji

