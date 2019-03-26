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
        print("* 0 - Get all Users               **")
        print("* 1 - Perform Query for Answer 1  **")
        print("* 2 - Perform Query for Answer 2  **")
        print("* 3 - Query MongoDB               **")
        print("* 4 - Query Neo4j                 **")
        print("* 5 - Query History               **")
        print("* 6 - Import CSV file to DBs      **")
        print("* 7 - Quit the APP                **")
        print("************************************")
        # print("NOTE: Please run Option 1 before any others")


    def parse_choice(self, choice):
        if(choice=="0"):
            input(self.neo_db.get_all_users())
        if(choice=="1"):
            self.get_user_list()
        if(choice=="2"):
            print(self.mongo_db.return_users()) #todo: return each user once
            user_id = input("\nSelect User_id you would like to find \ntrusted colleagues-of-colleagues \nwith one or more interests: ")
            print(self.mongo_db.answer_for_question2(user_id))
            input("Press Enter to continue...")
            pass
        if(choice=="3"):
            query = input("Write Query for MongoDB: ")
            self.query_history.append(query)
            pass
        if(choice=="4"):
            query = input("Write Query for Neo4j: ")
            self.query_history.append(query)
            pass
        if(choice=="5"):
            print(self.query_history)
            pass
        if(choice=="6"):
            print("Importing csv files to neo4j DB...\n")
            self.neo_db.dump_csv()
            input("Importing to neo4j is done. Press Enter to continue....\n")
            print("Import CSV file to Mongo ... \n")
            print("For example: /home/Navid/Documents/BigData/project1_sample/user.csv\n")
            filepath = input ("enter file path:")
            self.mongo_db.import_content(filepath)

            pass

        if(choice=="7"):
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
