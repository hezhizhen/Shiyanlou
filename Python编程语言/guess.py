# -*- coding:utf-8 -*-


true_num = 88

guess_num = int(raw_input("\nInput the number: "))

if guess_num > true_num:
    print "Sorry, It's lower than that......\n"
elif guess_num < true_num:
    print "Sorry, It's higher than that......\n"
else:
    print "Amazing, You guessed it!\n"

print "Game will exit :)"
