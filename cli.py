from lib.models import Base, Role, Audition
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///database.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    while True:
        print("\nMoringa Theater CLI")
        print("1. View All Roles")
        print("2. View All Auditions")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            roles = session.query(Role).all()
            if roles:
                for role in roles:
                    print(f"Role: {role.character_name}, Actors: {role.actors()}")
            else:
                print("No roles found.")
            
            input("\nPress Enter to return to the menu...")  
        
        elif choice == "2":
            auditions = session.query(Audition).all()
            if auditions:
                for audition in auditions:
                    print(f"Actor: {audition.actor}, Location: {audition.location}, Hired: {audition.hired}")
            else:
                print("No auditions found.")
            
            input("\nPress Enter to return to the menu...")  

        elif choice == "3":
            print("Goodbye!")
            break  

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
