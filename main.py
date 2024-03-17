import os

if '__main__' == __name__:
    print('Welcome to Robo speaker 1.1 Created by Harsh')
    while True:
        x = input('Enter what you want me to speak: ')
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)
