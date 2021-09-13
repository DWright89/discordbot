import random

fortune_list = ["You will find vague joy", "If you work hard, something will happen", "Your future looks like your past", "Telling someone they're ugly will bring you joy",
                "A glizzy in the throat is worth two on the grill", "Your best is not good enough", "There will come a day when your lack of preparation will not pay off",
                "Try being more proactive with your hygiene", "Ugggggghhhhhh", "There is a promotion on the horizon for someone else", "This service is no more or less accurate than a 'professional'",
                "Settling down is just another form of settling", "If you push the people around you to be their best, wait until they break first and pick up their shifts for overtime", 
                "Start a business by stealing the labor of your friends", "Hide behind someone more competent than you and try to take credit for their work", "The sun never sets on someone traveling west at ~1,200mph",
                "Tell someone they're good enough without lying to make yourself feel morally justified for what you're about to do", "Your minimalist approach to having a work ethic isn't impressing anyone",
                "No matter how hard you work, you'll never make something better than Bloodborne", "Trick yourself and those around you into believing that you are happy"]

#user_number = random.randint(1,4) - 1
#print(user_number)

def fortune():
    user_number = random.randint(1,20) - 1
    print(fortune_list[user_number])

play = input ("Do you want your fortune told? y/n  ")
if play == "y":
    fortune()
else:
    print("okay bye loser")