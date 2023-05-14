from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import Session

# from config import connection

def main():
    print("Welcome to the database.")

    # set up sqlalchemy session
    engine = create_engine(connection)
    session = Session(engine)

    entry = ''
    while True:
        entry = input("What information would you like to extract? Enter respective keys listed below \n \
                       1: Info 1 \
                       2: Info 2 \
                       3: Info 3 \
                       E: Exit ")
        
        result = ''
        if entry == '1':
            result = session.query(func.your_schema.your_function_name()).all()
        elif entry == '2':
            result = session.query(func.your_schema.your_function_name()).all()
        elif entry == '3':
           result = session.query(func.your_schema.your_function_name()).all()
        elif entry == 'E':
            print("Exiting")
            break
        else:
            print("Unrecognized key. Try again.")

        print(result)
    
if __name__ == "__main__":
    main()