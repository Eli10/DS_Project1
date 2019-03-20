from pymongo import MongoClient
import pandas as pd


class MongoDB():

    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['collaboration_net_db']
        self.user_collection = self.db['users']

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
        return pd.DataFrame( list( self.user_collection.find({}, {"Name": 1}) ) )

    def answer_for_question2(self, name):
        result = self.user_collection.find_one({"Name": name}, {"CurrentProject": 1})
        return pd.DataFrame( list( self.user_collection.find({"CurrentProject": result["CurrentProject"]}, {"Name": 1, "Skills": 1})))

    def setupv2(self):
        users = self.user_collection

        users.insert_many( [
            {
                "Name": "Eli",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Backend",
                "Skills": [
                            { "Python": 5},
                            {"Linux": 4},
                            {"MySQL": 3},
                            {"Critical Thinking": 4},
                            {"Java": 2}
                ],
                "Interests": [
                    {"Weightlifting": 4},
                    {"Martial Arts": 6},
                    {"Videogames": 7},
                    {"Basketball": 2},
                    {"Traveling": 9}

                ]
            },
            {
                "Name": "Navid",
                "Organization": {
                    "OrgName": "Hunter College",
                    "OrgType": "University",
                    "Distances": [
                        {"Hunter College": 1},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "McAfee",
                "Skills": [
                            { "Python": 4},
                            {"Linux": 5},
                            {"BigData": 4},
                            {"C++": 4},
                            {"McAfee": 5},
                            {"Network":5}
                ]
            },
            {
                "Name": "Bob",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Backend",
                "Skills": [
                            { "Java": 5},
                            {"Python": 4},
                            {"MySQL": 4},
                            {"Time Management": 2},
                            {"C++": 5}
                ],
                "Interests": [
                    {"Kart racing": 5},
                    {"Hiking": 3},
                    {"Bowling": 6},
                    {"Swimming": 8},
                    {"Traveling": 4}

                ]
            },
            {
                "Name": "Sandy",
                "Organization": {
                    "OrgName": "Hunter College",
                    "OrgType": "University",
                    "Distances": [
                        {"SSC": 8},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills": [
                            { "Web Development": 1},
                            {"Networking": 5},
                            {"MySQL": 5},
                            {"Communication": 4},
                            {"Software Development": 3}
                ],
                "Interests": [
                    {"Hiking": 2},
                    {"Ultimate Frisbee": 8},
                    {"Martial Arts": 7},
                    {"Swimming": 4},
                    {"Bowling": 5}

                ]
            },
            {
                "Name": "Jake",
                "Organization": {
                    "OrgName": "Hunter College",
                    "OrgType": "University",
                    "Distances": [
                        {"SSC": 8},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills": [
                            { "Web Development": 3},
                            {"Networking": 2},
                            {"MySQL": 2},
                            {"Communication": 4},
                            {"Software Development": 5}
                ],
                "Interests": [
                    {"Kart racing": 6},
                    {"Ultimate Frisbee": 4},
                    {"Basketball": 9},
                    {"Weightlifting": 6},
                    {"Videogames": 7}

                ]
            },
            {
                "Name": "Ruby",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Hunter College": 8},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills": [
                            { "Web Development": 5},
                            {"Javascript": 5},
                            {"MySQL": 3},
                            {"HTML": 1},
                            {"Accounting": 4}
                ],
                "Interests": [
                    {"Bowling": 5},
                    {"Traveling": 5},
                    {"Swimming": 6},
                    {"Volleyball": 8},
                    {"Cycling": 6}

                ]
            },
            {
                "Name": "Amy",
                "Organization": {
                    "OrgName": "NSA",
                    "OrgType": "Company",
                    "Distances": [
                        {"Hunter College": 20},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills": [
                            { "Web Development": 3},
                            {"Information Security": 2},
                            {"MySQL": 2},
                            {"C++": 3},
                            {"Copywriting": 1}
                ],
                "Interests": [
                    {"Gardening": 9},
                    {"Volleyball": 6},
                    {"Swimming": 4},
                    {"Kart racing": 7},
                    {"Cycling": 4}

                ]
            },
            {
                "Name": "Paul",
                "Organization": {
                    "OrgName": "NSA",
                    "OrgType": "Company",
                    "Distances": [
                        {"Hunter College": 20},
                        {"NSA": 20}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills": [
                            { "Information Security": 5},
                            {"C++": 3},
                            {"Foreign Languages": 2},
                            {"MySQL": 5},
                            {"Linux": 3}
                ],
                "Interests": [
                    {"Weightlifting": 4},
                    {"Ultimate Frisbee": 6},
                    {"Martial Arts": 7},
                    {"Hiking": 2},
                    {"Basketball": 9}

                ]
            }

        ] )
