None
meme_dict = {
            "OVERRATED": "Something that needs to be worse",
            "UNDERRATED": "Something that needs to be better",
            "CRINGE": "Something that is embarassing and not funny",
            "LOL": "Something that is very funny",
            "TYSM": "It means Thank You So Much",
            "IDC": "It means I Dont Care",
            "VIP": "Very Important Person"
            }

word = input("Write a non understandable word (With Large Characters!): ")

if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("Sorry, That word doesnt exist... But we are currently working on it!")
