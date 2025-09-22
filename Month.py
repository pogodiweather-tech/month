# List of summer months
L = ["june", "july", "august"]

# All months
S = ["january", "february", "march", "april", "may",
     "june", "july", "august",
     "september", "october", "november", "december"]

# Ask the user for the current month
M = input("What month is it now? ").strip().lower()

# Check if it is in the list of months
if M not in S:
    print("This is not a real month.")
else:
    if M in L:
        print("✈️🌍Vacation✈️🌍!")
    else:
        print("🎒🏫School🎒🏫!")
