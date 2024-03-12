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
# -l means loo[p the song indefinitely

os.system('clear')

print(Fore.MAGENTA + Back.WHITE + """
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

                                  PINKY Pink

                                   LADDER521
          """ + Style.RESET_ALL)
print()

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
    print(Fore.RED + Back.WHITE + message + Style.RESET_ALL)
    time.sleep(0.3)
    print()


def generate_password():
    while True:
        try:
            passlen = int(input("Enter the length of password: "))
            if passlen <=0:
                raise ValueError("Password length must be a positive integer")
            break
        except ValueError as e:
            print(Fore.RED + "Invalid input. Please enter a valid positive integer for the password length" + Style.RESET_ALL)

    complexity_options = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'spl_charact': string.punctuation
    }

    #Allow user to use the complexity options
    use_lowercase = input("Include lowercase letters? (y\n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y\n): ").lower() == 'y'
    use_digits = input("Include digits? (y\n): ").lower() == 'y'
    use_spl_charars = input("Include special characters? (y\n):").lower() == 'y'

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


    def print_your():
        message = " [¢] Selecting The Characters "
        print(Fore.YELLOW + message + Style.RESET_ALL)
        time.sleep(0.25)
        print()

    print_your()
    print()


    def print_length(passlen):
        message1 = str(passlen)
        message2 = " Characters Choosed "
        message3 = " [!] "
        print(Fore.RED + message3 + Fore.CYAN + message1 + Fore.GREEN + message2 + Style.RESET_ALL)
        time.sleep(0.25)
        print()

    print_length(passlen)
    print()


    def print_you():
        message = " [•] Permutating The Characters "
        print(Fore.YELLOW + message + Style.RESET_ALL)
        time.sleep(0.25)
        print()

    print_you()
    print()



    def print_arrange():
        message1 = "     Arrangement Of Characters ..."
        message2 = "..."
        message3 = "...✓✓✓ COMPLETE "
        print(Fore.RED + message1 + Fore.YELLOW + message2 + Fore.GREEN + message3)
        time.sleep(0.25)
        print(Style.RESET_ALL)
        print()

    print_arrange()
    print()


    def print_your_pass():
        message1 = " [✓] Your Password Is: "
        message2 = password
        print(Fore.GREEN + message1 + Style.RESET_ALL)
        time.sleep(0.25)
        print(Fore.MAGENTA + message2 + Style.RESET_ALL)
        time.sleep(0.4)
        print()

    print_your_pass()
    print()



    def print_strength():
        strength = "Password Strength: "
        m1 = "Weak"
        m2 = "Moderate"
        m3 = "Strong"
        if passlen < 8:
            strength += m1
            print(Fore.RED + strength + Style.RESET_ALL)
            time.sleep(0.25)
        elif 8 <= passlen < 12:
            strength += m2
            print(Fore.YELLOW + strength + Style.RESET_ALL)
            time.sleep(0.25)
        else:
            strength += m3
            print(Fore.GREEN + strength + Style.RESET_ALL)
            time.sleep(0.25)
        print()
        entropy = calcu_entropy(password)
        if entropy < 28:
            print(Fore.RED + "Password Weak" + Style.RESET_ALL)
            time.sleep(0.3)
        elif entropy < 36:
            print(Fore.BLUE + "Password Moderate" + Style.RESET_ALL)
            time.sleep(0.3)
        else:
            print(Fore.GREEN + "Password Strong" + Style.RESET_ALL)
            time.sleep(0.3)

        print(Fore.CYAN + "Entropy: ", entropy, "bits")
        time.sleep(0.25)
        print(Style.RESET_ALL)
        print()
        
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
