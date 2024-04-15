import os, time, math, random, string, pygame
from colorama import Fore, Style, Back, init

#Initialize colorama
init()

#Initialize pygame mixer
pygame.mixer.init()

#Load the song
pygame.mixer.music.load('data/data/com.termux/files/home/Cryptify/panther.mp3')

#Play song in the background
pygame.mixer.music.play(-1)
# -l means loop the song indefinitely

os.system('clear')

print("")
print(Fore.MAGENTA +"""
                             .--.            .--.
                            ( (`\\\\.\"--``--\".//`) )
                             '-.   __   __    .-'
                              /   /__\\ /__\\   \\
                             |    \\ 0/ \\ 0/    |
                             \\     `/   \\`     /
                              `-.  /-\"\"\"-\\  .-`  
                                /  '.___.'  \\       
                                \\     I     /       
                                 `;--'`'--;`        
                                   '.___.'    
                                  ___| |___           .\"`-.
                               .-`  .---.  `-.       /     )
                              /   .'     '.   \\     /      )
                             /  /||       ||\\  \\   /  /`\"\"`
                            /  / ||       || \\  \\ /  /
                           /  /  ||       ||  \\  /  /
                          /  (___||___.-=--.   \\   /
                         (                -;    '-'
                          `-----------.___~;

                                    Cryptify

                    https://github.com/Ladder521/Crytify.git
          """ + Style.RESET_ALL)
print("")

def calcu_entropy(password):
    character_set_size = 0
    for char_range in [range(97, 123), range(65, 91), range(48, 58), range(32, 48), range(58, 65), range(91, 97), range(123, 127)]:
        if any([chr(i) in password for i in char_range]):
            character_set_size += len(char_range)
    password_length = len(password)
    entropy = math.log2(character_set_size ** password_length)
    return entropy

    
def print_thank_you():
    message = " [~] THANK YOU [~] "
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL)
    time.sleep(0.3)
    print()


def generate_password():
    while True:
        try:
            passlen = int(input("Enter the length of password: "))
            time.sleep(0.5)
            print()
            if passlen <=0:
                raise ValueError("Password length must be a positive integer")
            break
        except ValueError as e:
            print(Fore.RED + "[INVALID INUT] Please enter a valid positive integer for the password length" + Style.RESET_ALL)

    complexity_options = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'spl_charact': string.punctuation
    }

    #Allow user to use the complexity options
    use_lowercase = input("Include lowercase letters? (Y/N): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    use_digits = input("Include digits? (Y/N): ").lower() == 'y'
    use_spl_charars = input("Include special characters? (Y/N):").lower() == 'y'

    #Combine selected complexities
    characters = ''
    if use_lowercase:
        characters += complexity_options['lowercase']
    if use_uppercase:
        characters += complexity_options['uppercase']
    if use_digits:
        characters += complexity_options['digits']
    if use_spl_charars:
        characters += complexity_options['spl_charact']

    #check if atleast one complexity is chosen
    if not any([use_lowercase, use_uppercase, use_digits, use_spl_charars]):
        print(Fore.YELLOW + Style.BRIGHT + "AT LEAST ONE COMPLEXITY MUST BE CHOSEN" + Style.RESET_ALL)
        time.sleep(0.5)
        return

    #Generate password from the selected complexity(s)
    password = ''.join(random.sample(characters, passlen))
    print()


    def print_select():
        message = " [¢] Selecting The Characters "
        print(Fore.YELLOW + message + Style.RESET_ALL)
        time.sleep(0.25)

    print_select()
    print()


    def print_
    choose(passlen):
        message1 = " [!] "
        message2 = str(passlen)
        message3 = " Characters Choosed "
        message = f"{Fore.RED}{message1}{Style.RESET_ALL} {Fore.CYAN}{message2}{Style.RESET_ALL} {Fore.GREEN}{message3}{Style.RESET_ALL}"
        print(message)
        time.sleep(0.5)

    print_choose(passlen)
    print()


    def print_permut():
        message = " [•] Permutating The Characters "
        print(Fore.YELLOW + message + Style.RESET_ALL)
        time.sleep(0.5)

    print_permut()
    print()



    def print_arrange():
        message1 = " [&] Arrangement Of Characters ..."
        message2 = "..."
        message3 = "...✓✓✓ COMPLETE "
        message = f"{Fore.RED}{message1}{Style.RESET_ALL} {Fore.YELLOW}{message2}{Style.RESET_ALL} {Fore.GREEN}{message3}{Style.RESET_ALL}"
        print(message)
        time.sleep(0.5)

    print_arrange()
    print()


    def print_pass():
        message1 = " [x] Your Password Is: "
        message2 = password
        message = f"{Fore.GREEN}{message1}{Style.RESET_ALL} {Fore.MAGENTA}{message2}{Style.RESET_ALL}"
        print(message)
        time.sleep(0.25)

    print_pass()
    print()



    def print_strength():
        strength = " [$] Password Strength: "
        m1 = "Weak"
        m2 = "Moderate"
        m3 = "Strong"
        if passlen < 9:
            strength += m1
            print(Fore.RED + strength + Style.RESET_ALL)
            time.sleep(0.25)
        elif 9 <= passlen < 12:
            strength += m2
            print(Fore.YELLOW + strength + Style.RESET_ALL)
            time.sleep(0.25)
        else:
            strength += m3
            print(Fore.GREEN + strength + Style.RESET_ALL)
            time.sleep(0.25)
        print()
        
        entropy = calcu_entropy(password)
        #IN THIS CODE, Entropy IS A MEASURE OF RANDOMNESS OR UNCERTAINITY OF THE GENERATED PASSWORD
        print(Fore.CYAN + " [E] Entropy: {:.2f} bits". format(entropy))
        time.sleep(1.2)
        print(Style.RESET_ALL)
        print()
        if entropy < 27:
            print(Fore.RED + " [E] Password has LOW RANDOMNESS" + Style.RESET_ALL)
            time.sleep(1)
        elif entropy < 36:
            print(Fore.BLUE + " [E] Password has MODERATE RANDOMNESS" + Style.RESET_ALL)
            time.sleep(1)
        else:
            print(Fore.GREEN + " [E] Password has HIGH RANDOMNESS" + Style.RESET_ALL)
            time.sleep(1)
        
    print_strength()
    print()

while True:
    user_input = input("Enter 'G' to generate a password or 'E' to exit: ")
    if user_input.lower() == 'g':
        print()
        generate_password()
    elif user_input.lower() == 'e':
          print()
          print_thank_you()
          #Stop the song when program exists
          pygame.mixer.music.stop()
          break
