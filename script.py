tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

# Creating an empty dictionary
spread = {}

# Popping tarot's 13 key's value and putting it to spread dict's "past" key
spread["past"] = tarot.pop(13)

# Popping tarot's 22 key's value and putting it to spread dict's "present" key
spread["present"] = tarot.pop(22)

# Popping tarot's 10 key's value and putting it to spread dict's "future" key
spread["future"] = tarot.pop(10)

# Iterating through the spread dictionary with a for loop
for key, value in spread.items():
  print("Your " + str(key) + " is the " + value + " card.")
