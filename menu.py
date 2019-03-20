from db import MongoDB
from neo4j import NeoDB
import os



class Menu():

    def __init__(self):
        self.neo_db = NeoDB()
        self.mongo_db = MongoDB()
        self.query_history = []


    def main_menu(self):
        print("*******SELECT AN OPTION*************")
        print("************************************")
        print("* 1 - Create DBs (Mongo and Neo4j)**")
        print("* 2 - Perform Query for Answer 1  **")
        print("* 3 - Perform Query for Answer 2  **")
        print("* 4 - Query MongoDB               **")
        print("* 5 - Query Neo4j                 **")
        print("* 6 - Query History               **")
        print("* 7 - Return to Main Menu         **")
        print("* 8 - Quit the APP                **")
        print("************************************")
        print("NOTE: Please run Option 1 before any others")


    def parse_choice(self, choice):
        if(choice=="1"): #todo: show all the user
            self.neo_db.setup()
            self.mongo_db.setupv2()
            input("Press Enter to continue...")
        if(choice=="2"):
            self.get_user_list() 
        if(choice=="3"):
            print(self.mongo_db.return_users()) #todo: return each user once
            user = input("\nSelect User you would like to find \ntrusted colleagues-of-colleagues \nwith one or more interests: ")
            print(self.mongo_db.answer_for_question2(user))
            input("Press Enter to continue...")
            pass
        if(choice=="4"):
            query = input("Write Query for MongoDB: ")
            self.query_history.append(query)
            pass
        if(choice=="5"):
            query = input("Write Query for Neo4j: ")
            self.query_history.append(query)
            pass
        if(choice=="6"):
            print(self.query_history)
            pass
        if(choice=="7"):
            print("Import CSV file ...") #todo: Working -Ns
            pass
        if(choice=="8"):
            quit()

    def get_user_list(self):
        print( self.neo_db.get_all_users() )
        user = input("SELECT User (Type Name): ")
        company = input("SELECT Company Name of Same User: ")
        self.neo_db.query_for_answer_1(user, company)
        input("Press ENTER to Continue...")


    def run(self):
        print("Welcome To Collaboration NET DB")
        while(True):
            self.main_menu()
            choice = input("Choice: ")
            self.parse_choice(choice)
