questions= [
    ["Which language is used to create fb?", "Python","Java","PHP","CSharp",3],
    ["Which language is used to create google?", "Python","Java","PHP","CSharp",2],
    ["Which language is used to create youtube?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create twitter?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create whatsapp?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create instagram?", "Python","Java","PHP","CSharp",3],
    ["Which language is used to create tiktok?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create linkedin?", "Python","Java","PHP","CSharp",2],
    ["Which language is used to create snap?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create reddit?", "Python","Java","PHP","CSharp",3],
    ["Which language is used to create pinterest?", "Python","Java","PHP","CSharp",2],
    ["Which language is used to create quora?", "Python","Java","PHP","CSharp",1],
    ["Which language is used to create telegram?", "Python","Java","PHP","CSharp",2],
    ["Which language is used to create discord?", "Python","Java","PHP","CSharp",3],
    ["Which language is used to create slack?", "Python","Java","PHP","CSharp",2]


    ]

levels= [1000,2000,3000,4000,5000,6000,7000,8000,16000,32000,64000,125000,250000,500000,1000000]
lifelines= ["50:50","Phone a friend","Ask the audience"]
pricemoney = 0
level = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}, b. {question[2]}, c. {question[3]}, d. {question[4]}")
    correctanswer = question[5]

    answer = input("enter your answer:")
    print(f"{answer} is your answer")
    useranswer = 0
    if answer == "a":
        useranswer = 1
    elif answer == "b":
        useranswer = 2
    elif answer == "c":
        useranswer = 3
    elif answer == "d":
        useranswer = 4
    if correctanswer == useranswer:
        print("correct answer")
        level += 1
        pricemoney = levels[level]
        if level == 14:
            print("you have won 1 million")
            break
    else:
        print("wrong answer")
        print(f"you have won {pricemoney}")
        break




