if __name__ == '__main__':
    from os import system
    cls = lambda: system('cls')
    global tot_points
    def show_record():
        print('The highest score is: ', highest_score)

    def reset_score():
        global highest_score
        highest_score = 0


    def show_help():
        print("HELP".center(95,'-'))
        print('-'*95)
        print('Quiz Game'.center(95,'-'))
        print(">>  This quiz has two rounds - Preliminary Round & Final Round".ljust(95))
        print(""">>  In Preliminary round, you will be asked a total of 3 questions which will test
            your general knowledge. You are eligible to play the game if you given at least 2
            right answers, otherwise you can't proceed further to the Final Round.""")
        print(""">>  Your game starts with Preliminary Round. In this round you will be asked a
            total of 10 questions. Each correct answer will be awarded $100,000!
            This way, by answering all questions correctly, you can win upto ONE MILLION cash prize!!!""")
        print(""">>  You will be given 4 options and you have to press A, B ,C or D for the
            right option.""")
        print(">>  You will be asked questions continuously, until your answers are correct.")
        print(">>  No negative markings for wrong answers.")
        print(":ALL THE BEST:\n".center(95, '-'))

    def quit_game():
        quit()

    def test():
        global countr
        countr = 0
        for i in range(1,11):
            if i == 1:
                print("1.What is the National Game of England?")
                choices1 = input("A.Football\t\tB.Basketball\n\nC.Cricket\t\tD.Baseball\n")
                if choices1.upper() == 'C':
                    print('Correct!!')
                    countr += 1
                    input()
                else:
                    print('Wrong!! The correct answer is C.Cricket')
                    input()
                    score()
            if i == 2:
                print("2.Study of Earthquake is called?")
                choices2 = input('A.Seismology\t\tB.Cosmology\n\nC.Orology\t\tD.Etimology\n')
                if choices2.upper() == 'A':
                    print('Correct!!')
                    countr += 1
                    input()
                else:
                    print("Wrong!! The correct answer is A.Seismology")
                    input()
                    score()
            if i == 3:
                print("3.Among the top 10 highest peaks in the world, how many lie in Nepal?")
                choices3 = input("A.6\t\tB.7\n\nC.8\t\tD.9\n")
                if choices3.upper() == 'C':
                    print('Correct!!')
                    countr += 1
                    input()
                else:
                    print("Wrong!! The correct answer is C.8")
                    input()
                    score()
            if i == 4:
                print("4.The Laws of Electromagnetic Induction were given by?")
                choices4 = input('A.Faraday\t\tB.Tesla\n\nC.Maxwell\t\tD.Coulomb\n')
                if choices4.upper() == 'A':
                    print('Correct!!')
                    countr +=1
                    input()
                else:
                    print('Wrong!! The correct answer is A.Faraday')
                    input()
                    score()
            if i == 5:
                print("5.In what unit is electric power measured?")
                choices5 = input("A.Coulomb\t\tB.Watt\n\nC.Power\t\tD.Units\n")
                if choices5.upper() == 'B':
                    print("Correct!!")
                    countr +=1
                    input()
                else:
                    print("Wrong!! The correct answer is B.Watt")
                    input()
                    score()
            if i == 6:
                print('6.Which element is found in Vitamin B12?')
                choices6 = input('A.Zinc\t\tB.Cobalt\n\nC.Calcium\t\tD.Iron\n')
                if choices6.upper() == 'B':
                    print('Correct!!')
                    countr +=1
                    input()
                else:
                    print("Wrong!! The correct ans is B.Cobalt")
                    input()
                    score()
            if i == 7:
                print('7.What is the national name of Japan?')
                choices7 = input('A.Polska\t\tB.Hellas\n\nC.Drukyul\t\tD.Nippon\n')
                if choices7.upper() == 'D':
                    print('Correct!!')
                    countr +=1
                    input()
                else:
                    print('Wrong!! The correct answer is D.Nippon')
                    input()
                    score()
            if i == 8:
                print('8.How many times a piece of paper can be folded at the most?')
                choices8 = input('A.6\t\tB.7\n\nC.8\t\tD.Depends on the size of paper\n')
                if choices8.upper() == 'B':
                    print("Correct!!")
                    countr +=1
                    input()
                else:
                    print('Wrong!! The correct answer is B.7')
                    input()
                    score()
            if i == 9:
                print('9.What is the capital of Denmark?')
                choices9 = input('A.Copenhagen\t\tB.Helsinki\n\nC.Ajax\t\tD.Galatasaray\n')
                if choices9.upper() == 'A':
                    print('Correct!!')
                    countr+=1
                    input()
                else:
                    print('Wrong!! The correct answer is A.Copenhagen')
                    input()
                    score()
            if i == 10:
                print('10.Which is the longest river in the world?')
                choices10 = input('A.Nile\t\tB.Koshi\n\nC.Ganga\t\tD.Amazon\n')
                if choices10.upper() == 'A':
                    print('Correct!!')
                    countr +=1
                    input()
                    score()
                else:
                    print("Wrong!! The correct answer is A.Nile")
                    input()
                    score()



    def go():
        decision = input("""Press Y if you want to play the next game
Press any key if you want to go to main menu.\n""")
        if decision.upper() == 'Y':
            home()
        else:
            main_home()


    def score():
        tot_points = float(countr)*100000
        global  highest_score
        if tot_points > highest_score:
            highest_score = tot_points
        if tot_points in range(1,1000000):
            print(':CONGRATULATIONS:'.center(95,'-'))
            print(f'You won ${round(tot_points,2)}'.center(95),'-')
            go()
        elif tot_points == 1000000.00:
            print(':CONGRATULATIONS:'.center(95, '-'))
            print('!!YOU ARE A MILLIONAIRE!!'.center(95,'-'))
            print(f'You won ${round(tot_points, 2)}'.center(95), '-')
            print('Thank You!!'.center(95))
            go()
        else:
            print("SORRY, YOU DIDN'T WIN ANY CASH".center(95,'-'))
            print('Thanks for participating'.center(95))
            print('Try again'.center(95))
            go()


    def home():
        count = 0
        for i in range(1,4):
            if i == 1:
                print("1.Which of the following is a Palindrome number?")
                options1 = input("A.42042\t\tB.101010\n\nC.23232\t\tD.01234\n")
                if options1.upper() == 'C':
                    print('Correct!!')
                    count += 1
                    input()
                else:
                    print('Incorrect, the correct ans is C.23232')
                    input()
            if i == 2:
                print("2.The country with the highest environmental performance index is?")
                options2 = input("A.France\t\tB.Denmark\n\nC.Switzerland\t\tD.Finland\n")
                if options2.upper() == 'C':
                    print('Correct!!')
                    count += 1
                    input()
                else:
                    print('Incorrect, the correct ans is C.Switzerland')
                    input()
            if i == 3:
                print("3.Which animal laughs like human being?")
                options3 = input("A.Polar Bear\t\tB.Hyena\n\nC.Donkey\t\tD.Chimpanzee\n")
                if options3.upper() == 'B':
                    print('Correct!!')
                    count += 1
                    input()
                else:
                    print('Incorrect, the correct ans is B.Hyena')
                    input()
        if count >= 2:
            print(f"Congratulations {player_name} you are eligible to play the game!!\n")
            input('Press any key to start the game!\n')
            test()
        else:
            print("Sorry you are not eligible for the test.")
            input()
            main_home()


    def main_home():
        print("QUIZ GAME".center(35))
        print('-' * 35)
        print("WELCOME TO THE GAME".center(35))
        print('-' * 35)
        print("> PRESS S to start the game".ljust(30))
        print("> PRESS V to view the highest score".ljust(30))
        print("> PRESS R to reset score".ljust(30))
        print("> PRESS H for help".ljust(30))
        print("> PRESS Q to quit".ljust(30))
        choice = input()
        if choice.upper() == 'V':
            show_record()
            input()
            main_home()

        elif choice.upper() == 'R':
            reset_score()
            input()
            main_home()

        elif choice.upper() == 'H':
            show_help()
            input()
            main_home()

        elif choice.upper() == 'Q':
            quit_game()

        elif choice.upper() == 'S':
            global player_name
            player_name = input("Enter your name: ")
            print(f"Welcome {player_name} to the quiz game".center(95,'-'))
            print("Following are some tips that will help you to understand the game:".center(35))
            print('-'*95)
            print(">>  This quiz has two rounds - Preliminary Round & Final Round".ljust(95))
            print(""">>  In Preliminary round, you will be asked a total of 3 questions which will test
    your general knowledge. You are eligible to play the game if you given at least 2
    right answers, otherwise you can't proceed further to the Final Round.""")
            print(""">>  Your game starts with Preliminary Round. In this round you will be asked a
    total of 10 questions. Each correct answer will be awarded $100,000!
    This way, by answering all questions correctly, you can win upto ONE MILLION cash prize!!!""")
            print(""">>  You will be given 4 options and you have to press A, B ,C or D for the
    right option.""")
            print(">>  You will be asked questions continuously, until your answers are correct.")
            print(">>  No negative markings for wrong answers.")
            print(":ALL THE BEST:".center(95,'-'))
            start_game = input("""Press Y to start the game!
Press any other key to return to the main menu!\n""")
            if start_game.upper() == 'Y':
                home()
            else:
                main_home()


    reset_score()
    main_home()