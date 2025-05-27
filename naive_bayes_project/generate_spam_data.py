import csv
import random


spam_phrases = [
    "Win cash now! Click here: http://spam.com",
    "Congratulations, you've won a prize! Call 12345",
    "Free entry in a weekly contest, text WIN to 54321",
    "Urgent! Your account is compromised, verify now!",
    "You have been selected for a $1000 reward",
    "Claim your free gift card by clicking here",
    "Limited offer, buy now and get 50% off",
    "You won a free ticket to Bahamas, reply YES",
    "Get cheap meds without prescription",
    "Lowest price on electronics, order today",
    "Earn money from home, no experience required",
    "Your loan is approved, call immediately",
    "Win iPhone now, enter your details",
    "You have an unpaid invoice, pay now",
    "Earn $5000 a week working online",
    "Special discount for you, shop now",
    "Free subscription for 3 months, register here",
    "Your package delivery failed, confirm address",
    "Act fast! Limited time offer ends soon",
    "You’ve won a lottery, send your bank info"
]

ham_phrases = [
    "Hey, how are you doing today?",
    "Let's meet for lunch tomorrow.",
    "Can you send me the report by tonight?",
    "Happy birthday! Hope you have a great day.",
    "Don't forget the meeting at 3 PM.",
    "I will call you when I reach home.",
    "Thanks for your help with the project.",
    "Are you coming to the party this weekend?",
    "I'll pick you up at 6 o'clock.",
    "Please send me the address.",
    "That movie was really good!",
    "I'm running late, sorry.",
    "Can you share the notes from class?",
    "What time does the train arrive?",
    "Good luck with your exam!",
    "Let's catch up soon.",
    "Did you watch the game last night?",
    "I have sent the documents to your email.",
    "Please remind me to buy groceries.",
    "Thanks for the invitation, see you there."
]


rows = []
for i in range(500):
    msg = random.choice(spam_phrases)
    rows.append([msg, "Spam"])
for i in range(500):
    msg = random.choice(ham_phrases)
    rows.append([msg, "Ham"])


random.shuffle(rows)


with open("data.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Message", "Label"])
    writer.writerows(rows)

print("data.csv with 1000 spam/ham messages created successfully.")
