
import random


def random_number_generated(ranFrom,ranTo):
    randomNumber= random.randint(ranFrom,ranTo)
    return randomNumber

def Number_GuessingFunction(userNumber, randomNumber):
    if userNumber == randomNumber:
        return True
    else:
        return False
def Number_guessing_game_level(ranFrom,ranTo):
    random_number= random_number_generated(ranFrom,ranTo)
    return random_number,ranTo

# def Number_Guessing_score(signal,score):
#     if signal:
#         score=+1
#     return score

turnNumberGuessing=5
Game_score=0

print("\n\n\n🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟  Welcome to the Number Guessing Game! 🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟\n")

def LevelSelection():
    ## Easy prace 1, Medium prace 2, and Hard prace 3
    try :
        user_select_lavel=int(input("Select a Level (\nprace 1 to Easy\n prace 2 to Medium\n And prace 3 Hard) : "))
    except ValueError:
        print(" �� Invalid input! Please enter a number. ��")
        exit()

    if user_select_lavel == 1:
        print("Grate you select Easy Level guess number 1 to 10")
        actual_random,ranTo= Number_guessing_game_level(1,10)
    elif user_select_lavel == 2:
        print("Grate you select Medium Level guess number 1 to 50")
        actual_random,ranTo= Number_guessing_game_level(1,50)
    elif user_select_lavel == 3:
        print("Grate you select Hard Level guess number 1 to 100")
        actual_random,ranTo= Number_guessing_game_level(1,100)
    else:
        print("�� Invalid Level Selection! Please try again. ��")
        exit()
    return actual_random,ranTo

actual_random,ranTo = LevelSelection()
print("You have Next ➡️ ", turnNumberGuessing, " turns left.")



while  turnNumberGuessing > 0:
    try:

        User_guess_number = int(input(f"Enter your Guessing number between {1} and {ranTo} : "))


        if User_guess_number < 1 or User_guess_number > ranTo or User_guess_number == '':
            print(f" ❌ please enter a number between {1} and {ranTo} ! ")
            continue

        if Number_GuessingFunction(User_guess_number, actual_random):
            print(" 🎉 Congratulations! You guessed the correct ✅ number! 🎉 🥰")
            Game_score+=10
            actual_random=random_number_generated(1,ranTo)
            continue
        else:
            print("❌ Sorry you dodn't match number!")
            print(f"HINT:- The number is {'even' if actual_random % 2 == 0 else 'odd'}.")


            turnNumberGuessing -= 1
            if turnNumberGuessing == 0:
                print("��  ⏳ Time's up! You lost the game! ��")
                print("\n🎮 Game over! 💀🔥 \n")
                print(f"\nScore: {Game_score}\n")
                print("The correct number was ", actual_random)
            
                exit()
            print("You have Next ➡️ ", turnNumberGuessing, " turns left.")

    except ValueError:
        print("�� Invalid input! Please enter a number. try again 🔄 ��")
        break