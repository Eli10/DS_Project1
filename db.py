from pymongo import MongoClient
import pandas as pd
import sys
import json
import os # Import file

class MongoDB():

    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['collaboration_net_db']
        self.user_collection = self.db['users']

    def import_content(self, filepath): #Import CSV
        mng_client = MongoClient('localhost', 27017)
        mng_db = mng_client['collaboration_net_db']
        collection_name = 'users'
        db_cm = mng_db[collection_name]
        cdir = os.path.dirname(__file__)
        file_res = os.path.join(cdir, filepath)

        data = pd.read_csv(file_res)
        data_json = json.loads(data.to_json(orient='records'))
       # db_cm.remove()
        db_cm.insert(data_json)
    # def setup(self):
    #     users = self.user_collection

    #     users.insert_many( [
    #         {
    #             "FirstName": "Eli",
    #             "LastName": "Augustin",
    #             "Organization": "SSC",
    #             "OrgDistance": 12,
    #             "CurrentProject": "Capstone",
    #             "Skills": { "Go": 3,
    #                         "Python": 4,
    #                         "C++": 2,
    #                         "Javascript": 3,
    #                         "OCaml": 5

    #             }
    #         },
    #         {
    #             "FirstName": "Bob",
    #             "LastName": "Johnson",
    #             "Organization": "SSC",
    #             "OrgDistance": 5,
    #             "CurrentProject": "Capstone",
    #             "Skills": { "Go": 1,
    #                         "Python": 5,
    #                         "C++": 4,
    #                         "Javascript": 2,
    #                         "OCaml": 3,
    #                         "HTML": 3,
    #                         "CSS": 4

    #             }
    #         },
    #         {
    #             "FirstName": "Jane",
    #             "LastName": "Foster",
    #             "Organization": "SSC",
    #             "OrgDistance": 7,
    #             "CurrentProject": "Capstone",
    #             "Skills": { "Go": 3,
    #                         "Python": 4,
    #                         "C++": 2,
    #                         "Scala": 4,
    #                         "Haskell": 5,
    #                         "PostgresDB": 3

    #             }
    #         },
    #         {
    #             "FirstName": "Jimmy",
    #             "LastName": "Crickets",
    #             "Organization": "Hunter College",
    #             "OrgDistance": 15,
    #             "CurrentProject": "Gene Sequencing",
    #             "Skills": { "Julia": 3,
    #                         "Python": 4,
    #                         "Genetic Algorithms": 2,
    #                         "Discrete Math": 3,
    #                         "OCaml": 5

    #             }
    #         },
    #         {
    #             "FirstName": "Dav",
    #             "LastName": "Macintosh",
    #             "Organization": "NSA",
    #             "OrgDistance": 30,
    #             "CurrentProject": "Data Mining",
    #             "Skills": { "Security": 5,
    #                         "Python": 4,
    #                         "Networking": 3,
    #                         "Routing": 4,
    #                         "C": 3,
    #                         "Java": 2

    #             }
    #         }
    #     ] )

    def return_users(self):
        return pd.DataFrame( list( self.user_collection.find({}, {"First Name": 1}) ) )

    def answer_for_question2(self, name):
        result = self.user_collection.find_one({"First Name": name}, {"Project": 1})
        df =  pd.DataFrame( list( self.user_collection.find({"Project": result["Project"]}, {"First Name": 1, "Skills": 1})))
        fixed_df = df.drop(df[df["First Name"] == name].index)
        return fixed_df

    def setupv2(self):
        users = self.user_collection

        users.insert_many( [
            {
                "First Name": "Eli",
                "Last Name": "Augustin",
                "User_Id": 1,
                "Organization": {
                    "organization": "SSC",
                    "organization_type": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "Project": "Backend",
                "Skills": [
                            {"Skill":"Python", "Skill Level":5},
                            {"Skill":"Linux", "Skill Level":4},
                            {"Skill":"MySQL", "Skill Level": 3},
                            {"Skill":"Critical Thinking", "Skill Level":4},
                            {"Skill":"Java", "Skill Level":2}
                ],
                "Interests": [
                    {"Interest":"Weightlifting", "Interest Level":4},
                    {"Interest":"Martial Arts", "Interest Level":6},
                    {"Interest":"Videogames", "Interest Level":7},
                    {"Interest":"Basketball", "Interest Level":2},
                    {"Interest":"Traveling", "Interest Level":9}

                ]
            },
            {
                "First Name": "Navid",
                "Last Name": "Saboori",
                "User_Id": 2,
                "Organization": {
                    "organization": "Hunter College",
                    "organization_type": "University",
                    "Distances": [
                        {"Hunter College": 1},
                        {"NSA": 20}
                    ]
                },
                "Project": "McAfee",
                "Skills": [
                            {"Skill":"Python", "Skill Level":4},
                            {"Skill":"Linux", "Skill Level":5},
                            {"Skill":"BigData", "Skill Level":4},
                            {"Skill":"C++", "Skill Level":4},
                            {"Skill":"McAfee", "Skill Level":5},
                            {"Skill":"Network", "Skill Level":5}
                ]
            },
            {
                "First Name": "Bob",
                "Last Name": "Mcintosh",
                "User_Id": 3,
                "Organization": {
                    "organization": "SSC",
                    "organization_type": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "Project": "Backend",
                "Skills": [
                            {"Skill":"Java", "Skill Level":5},
                            {"Skill":"Python", "Skill Level":4},
                            {"Skill":"MySQL", "Skill Level":4},
                            {"Skill":"Time Management", "Skill Level":2},
                            {"Skill":"C++", "Skill Level":5}
                ],
                "Interests": [
                    {"Interest":"Kart racing", "Interest Level":5},
                    {"Interest":"Hiking", "Interest Level":3},
                    {"Interest":"Bowling", "Interest Level":6},
                    {"Interest":"Swimming", "Interest Level":8},
                    {"Interest":"Traveling", "Interest Level":4}

                ]
            },
            {
                "First Name": "Sandy",
                "Last Name": "Anderson",
                "User_Id": 4,
                "Organization": {
                    "organization": "Hunter College",
                    "organization_type": "University",
                    "Distances": [
                        {"SSC": 8},
                        {"NSA": 20}
                    ]
                },
                "Project": "Capstone",
                "Skills": [
                            {"Skill":"Web Development", "Skill Level":1},
                            {"Skill":"Networking", "Skill Level":5},
                            {"Skill":"MySQL", "Skill Level":5},
                            {"Skill":"Communication", "Skill Level":4},
                            {"Skill":"Software Development", "Skill Level":3}
                ],
                "Interests": [
                    {"Interest":"Hiking", "Interest Level":2},
                    {"Interest":"Ultimate Frisbee", "Interest Level":8},
                    {"Interest":"Martial Arts", "Interest Level":7},
                    {"Interest":"Swimming", "Interest Level":4},
                    {"Interest":"Bowling", "Interest Level":5}

                ]
            },
            {
                "First Name": "Jake",
                "Last Name": "Ryan",
                "User_Id": 5,
                "Organization": {
                    "organization": "Hunter College",
                    "organization_type": "University",
                    "Distances": [
                        {"SSC": 8},
                        {"NSA": 20}
                    ]
                },
                "Project": "Capstone",
                "Skills": [
                            {"Skill":"Web Development", "Skill Level":3},
                            {"Skill":"Networking", "Skill Level":2},
                            {"Skill":"MySQL", "Skill Level":2},
                            {"Skill":"Communication", "Skill Level":4},
                            {"Skill":"Software Development", "Skill Level":5}
                ],
                "Interests": [
                    {"Interest":"Kart racing", "Interest Level":6},
                    {"Interest":"Ultimate Frisbee", "Interest Level":4},
                    {"Interest":"Basketball", "Interest Level":9},
                    {"Interest":"Weightlifting", "Interest Level":6},
                    {"Interest":"Videogames", "Interest Level":7}

                ]
            },
            {
                "First Name": "Ruby",
                "Last Name": "Rodriguez",
                "User_Id": 6,
                "Organization": {
                    "organization": "SSC",
                    "organization_type": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "Project": "Capstone",
                "Skills": [
                            {"Skill":"Web Development", "Skill Level":5},
                            {"Skill":"Javascript", "Skill Level":5},
                            {"Skill":"MySQL", "Skill Level":3},
                            {"Skill":"HTML", "Skill Level":1},
                            {"Skill":"Accounting", "Skill Level":4}
                ],
                "Interests": [
                    {"Interest":"Bowling","Interest Level":5},
                    {"Interest":"Traveling","Interest Level":5},
                    {"Interest":"Swimming", "Interest Level":6},
                    {"Interest":"Volleyball", "Interest Level":8},
                    {"Interest":"Cycling", "Interest Level":6}

                ]
            },
            {
                "First Name": "Amy",
                "Last Name": "Pascal",
                "User_Id": 7,
                "Organization": {
                    "organization": "NSA",
                    "organization_type": "Company",
                    "Distances": [
                        {"Hunter College": 20},
                        {"NSA": 20}
                    ]
                },
                "Project": "Capstone",
                "Skills": [
                            {"Skill":"Web Development", "Skill Level":3},
                            {"Skill":"Information Security", "Skill Level":2},
                            {"Skill":"MySQL", "Skill Level":2},
                            {"Skill":"C++", "Skill Level":3},
                            {"Skill":"Copywriting", "Skill Level":1}
                ],
                "Interests": [
                    {"Interest":"Gardening", "Interest Level":9},
                    {"Interest":"Volleyball", "Interest Level":6},
                    {"Interest":"Swimming", "Interest Level":4},
                    {"Interest":"Kart racing", "Interest Level":7},
                    {"Interest":"Cycling", "Interest Level":4}

                ]
            },
            {
                "First Name": "Paul",
                "Last Name": "Wade",
                "User_Id": 8,
                "Organization": {
                    "organization": "NSA",
                    "organization_type": "Company",
                    "Distances": [
                        {"Hunter College": 20},
                        {"NSA": 20}
                    ]
                },
                "Project": "Capstone",
                "Skills": [
                            {"Skill":"Information Security", "Skill Level":5},
                            {"Skill":"C++", "Skill Level":3},
                            {"Skill":"Foreign Languages", "Skill Level":2},
                            {"Skill":"MySQL", "Skill Level":5},
                            {"Skill":"Linux", "Skill Level":3}
                ],
                "Interests": [
                    {"Interest":"Weightlifting", "Interest Level":4},
                    {"Interest":"Ultimate Frisbee", "Interest Level":6},
                    {"Interest":"Martial Arts", "Interest Level":7},
                    {"Interest":"Hiking", "Interest Level":2},
                    {"Interest":"Basketball", "Interest Level":9}

                ]
            }

        ] )
