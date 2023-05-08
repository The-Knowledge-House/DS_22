from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import Session

def main():
    print("Welcome to the database.")

    entry = ''
    while(True):
        entry = input("What information would you like to extract? Enter respective keys listed below \n \
                       1: Info 1 \
                       2: Info 2 \
                       3: Info 3 \
                       E: Exit ")
        
        if entry == '1':
            pass
        elif entry == '2':
            pass
        elif entry == '3':
            pass
        elif entry == 'E':
            print("Exiting")
            break
        else:
            print("Unrecognized key. Try again.")
    
if __name__ == "__main__":
    main()