from pymongo import MongoClient


class MongoDB():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
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

    

    def setupv2(self):
        users = self.user_collection

        users.insert_many( [
            {
                "FirstName": "Eli",
                "LastName": "Augustin",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Government": 7},
                        {"University": 10}
                    ]    
                },
                "CurrentProject": "Back-end",
                "Skills": [
                        { "Go": 3},
                            {"Python": 4},
                            {"C++": 2},
                            {"Javascript": 3},
                            {"OCaml": 5}
                ]
            },
            {
                "FirstName": "Bob",
                "LastName": "Johnson",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Government": 7},
                        {"University": 10}
                    ]
                },
                "CurrentProject": "Front-end",
                "Skills": [
                            { "Go": 1},
                            {"Python": 5},
                            {"C++": 4},
                            {"Javascript": 2},
                            {"OCaml": 3},
                            {"HTML": 3},
                            {"CSS": 4}

                ]
            },
            {
                "FirstName": "Jane",
                "LastName": "Foster",
                "Organization": {
                    "OrgName": "SSC",
                    "OrgType": "Company",
                    "Distances": [
                        {"Government": 7},
                        {"University": 10}
                    ]
                },
                "CurrentProject": "Back-end",
                "Skills": [
                            { "Go": 3},
                            {"Python": 4},
                            {"C++": 2},
                            {"Scala": 4},
                            {"Haskell": 5},
                            {"PostgresDB": 3}
                ]
            },
            {
                "FirstName": "Jimmy",
                "LastName": "Crickets",
                "Organization": {
                    "OrgName": "Hunter College",
                    "OrgType": "University",
                    "Distances": [
                        {"Government": 7},
                        {"Company": 13}
                    ]
                },
                "CurrentProject": "Capstone",
                "Skills":  [
                            { "Julia": 3},
                            {"Python": 4},
                            {"Genetic Algorithms": 2},
                            {"Discrete Math": 3},
                            {"OCaml": 5}
                ]
            },
            {
                "FirstName": "Dav",
                "LastName": "Macintosh",
                "Organization": {
                    "OrgName": "NSA",
                    "OrgType": "Government",
                    "Distances": [
                        {"Company": 7},
                        {"University": 13}
                    ]
                },
                "CurrentProject": "Data Mining",
                "Skills": [
                        { "Security": 5},
                        {"Python": 4},
                        {"Networking": 3},
                        {"Routing": 4},
                        {"C": 3},
                        {"Java": 2}
                ]
            }
        ] )


    
