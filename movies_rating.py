movie = "sinners"
rating = 3
popularity = 72.65

if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommend, it is good")
elif rating <= 2 and popularity > 60:
    print("You should check it out")
elif rating <= 2 and popularity < 50:
    print("Don't watch it, it is a waste of time")