from db import MongoDB
from neo4j import NeoDB
import os

print("Welcome To Collaboration NET DB")

def main_menu():
    print("************************************")
    print("* 1 - Create DBs (Mongo and Neo4j)**")
    print("* 2 - Perform Query 1             **")
    print("* 3 - Perform Query 2             **")
    print("************************************")
    print("NOTE: Please run Option 1 before any others")


def parse_choice(choice):
    if(choice=="1"):
        neo_db = NeoDB()
        neo_db.setup()
        neo_db.query_for_answer_1("Eli", "SSC")


while(True):
    os.system('clear')
    main_menu()
    choice = input("Choice: ")
    parse_choice(choice)

# db = MongoDB()
# db.setupv2()
