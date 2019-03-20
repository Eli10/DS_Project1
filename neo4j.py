from py2neo import Graph, Node, Relationship
import pandas as pd

class NeoDB():

    def __init__(self):
        self.graph = Graph(host="127.0.0.1", user="neo4j",bolt=True, password="12345")
        self.setup_node_list = [
            "CREATE (u1:User {First_Name:'Eli', Last_Name:'Augustin', Project: 'Backend', User_Id:1})",
            "CREATE (u2:User {First_Name:'Bob', Last_Name:'Mcintosh', Project: 'Backend', User_Id:3})",
            "CREATE (u4:User {First_Name:'Sandy', Last_Name:'Anderson', Project: 'Capstone', User_Id:4})",
            "CREATE (u5:User {First_Name:'Jake', Last_Name:'Ryan', Project: 'Capstone', User_Id:5})",
            "CREATE (u3:User {First_Name:'Ruby', Last_Name:'Rodriguez', Project:'Frontend', User_Id:6})",
            "CREATE (u6:User {First_Name:'Amy', Last_Name:'Pascal', Project: 'Data Discovery', User_Id:7})",
            "CREATE (u7:User {First_Name:'Amy', Last_Name:'Pascal',  Project: 'Data Discovery', User_Id:8})",
            "CREATE (u9:User {First_Name:'Paul', Last_Name:'Wade', ProjectProject: 'Backend', User_Id:2})",
            "CREATE (o1:Organization {organization: 'Hunter College', organization_type:'University'})",
            "CREATE (o2:Organization {organization: 'SSC', organization_type:'Company'})",
            "CREATE (o3:Organization {organization: 'NSA', organization_type:'Government'})",
            "CREATE (s:Skill {Skill:'Python'})",
            "CREATE (s1:Skill {Skill:'Java'})",
            "CREATE (s2:Skill {Skill:'C++'})",
            "CREATE (s3:Skill {Skill:'Julia'})",
            "CREATE (s4:Skill {Skill:'Genetic Algorithms'})",
            "CREATE (s5:Skill {Skill:'Discrete Math'})",
            "CREATE (s6:Skill {Skill:'Accounting'})",
            "CREATE (s7:Skill {Skill:'Copywriting'})",
            "CREATE (s8:Skill {Skill:'Foreign Languages'})",
            "CREATE (s9:Skill {Skill:'Web Development'})",
            "CREATE (s10:Skill {Skill:'Critical Thinking'})",
            "CREATE (s11:Skill {Skill:'Communication'})",
            "CREATE (s12:Skill {Skill:'Time Management'})",
            "CREATE (s13:Skill {Skill:'Statistical Analysis'})",
            "CREATE (s14:Skill {Skill:'Software Development'})",
            "CREATE (s15:Skill {Skill:'MySQL'})",
            "CREATE (s16:Skill {Skill:'Linux'})",
            "CREATE (s17:Skill {Skill:'Information Security'})",
            "CREATE (s18:Skill {Skill:'Data Modeling'})",
            "CREATE (s19:Skill {Skill:'Networking'})",
            "CREATE (s22:Skill {Skill:'McAfee'})",
            "CREATE (s20:Skill {Skill:'Javascript'})",
            "CREATE (s21:Skill {Skill:'HTML'})",
            "CREATE (i1:Interest {name:'Weightlifting'})",
            "CREATE (i2:Interest {name:'Bowling'})",
            "CREATE (i3:Interest {name:'Swimming'})",
            "CREATE (i4:Interest {name:'Basketball'})",
            "CREATE (i5:Interest {name:'Ultimate Frisbee'})",
            "CREATE (i6:Interest {name:'Kart racing'})",
            "CREATE (i7:Interest {name:'Traveling'})",
            "CREATE (i8:Interest {name:'Martial Arts'})",
            "CREATE (i9:Interest {name:'Videogames'})",
            "CREATE (i10:Interest {name:'Hiking'})",
            "CREATE (i11:Interest {name:'Cycling'})",
            "CREATE (i12:Interest {name:'Volleyball'})",
            "CREATE (i13:Interest {name:'Boxing'})",
            "CREATE (i14:Interest {name:'Gardening'})"

            ]
        self.relationship_list = [
            "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Java'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Java'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Time Management'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Networking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Communication'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Software Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Networking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Communication'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Software Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Javascript'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'HTML'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Accounting'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Information Security'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Copywriting'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Information Security'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Foreign Languages'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
            
            "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
            "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'McAfee'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
            "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",

            "MATCH (a:User {First_Name:'Eli'}), (b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Navid'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Bob'}),(b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Ruby'}),(b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Sandy'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Jake'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Amy'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:User {First_Name:'Paul'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
            "MATCH (a:Organization {organization:'SSC'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",
            "MATCH (a:Organization {organization:'SSC'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:DISTANCE {miles: 8}]->(b)",
            "MATCH (a:Organization {organization:'Hunter College'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",

            "MATCH (a:User {First_Name:'Eli'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Eli'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Eli'}),(i:Interest {name:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {First_Name:'Eli'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {First_Name:'Eli'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {First_Name:'Bob'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {First_Name:'Bob'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 3}]->(i)",
            "MATCH (a:User {First_Name:'Bob'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Bob'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {First_Name:'Bob'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {First_Name:'Jake'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Jake'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Jake'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {First_Name:'Jake'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Jake'}),(i:Interest {name:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {name:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {name:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {level: 5}]->(i)",
            "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {name:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {level: 8}]->(i)",
            "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {name:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Amy'}),(i:Interest {name:'Gardening'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)",
            "MATCH (a:User {First_Name:'Amy'}),(i:Interest {name:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Amy'}),(i:Interest {name:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Amy'}),(i:Interest {name:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {First_Name:'Amy'}),(i:Interest {name:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Paul'}),(i:Interest {name:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {level: 4}]->(i)",
            "MATCH (a:User {First_Name:'Paul'}),(i:Interest {name:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {level: 6}]->(i)",
            "MATCH (a:User {First_Name:'Paul'}),(i:Interest {name:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {level: 7}]->(i)",
            "MATCH (a:User {First_Name:'Paul'}),(i:Interest {name:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {level: 2}]->(i)",
            "MATCH (a:User {First_Name:'Paul'}),(i:Interest {name:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {level: 9}]->(i)"
        ]

    def setup(self):
        self.graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
        for s in self.setup_node_list:
            self.graph.run(s)
        for r in self.relationship_list:
            self.graph.run(r)

    def get_all_users(self):
        query_string = """MATCH (u:User)-[]->(o:Organization)
                        RETURN u.First_Name as Name, u.Project as Project,
                        o.name as OrgName, o.type as OrgType"""
        return pd.DataFrame(self.graph.run(query_string).data()).to_string()


    def query_for_answer_1(self, username, company_name):
        query_string = """
        MATCH (u:User)-[r]->(s:Skill)<-[r1]-(u1:User)-[]-(o:Organization)-[r2]-(o1:Organization)
        WHERE (u.First_Name='{}') and (o.name='{}' or o1.name='{}') and (r2.miles <=10)
        WITH DISTINCT u1.First_Name as name, o.name as org_name, collect(s.name) as common_skills, sum(r1.level) as weight
        ORDER BY weight DESC
        RETURN name, org_name, common_skills, weight""".format(username, company_name, company_name)
        print( pd.DataFrame(self.graph.run(query_string).data()).to_string() )
