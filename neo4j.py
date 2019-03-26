from py2neo import Graph, Node, Relationship
import pandas as pd

class NeoDB():

    def __init__(self):
        self.graph = Graph(host="127.0.0.1", user="neo4j",bolt=True, password="12345")
        self.csv_command_list = [
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/user.csv' AS line MERGE (u:user { User_id: line.User_id, name: line.`First name`, lastname: line.`Last name`})",
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/project.csv' AS line MATCH (u:user {User_id: line.User_id}) MERGE (p:project { User_id: line.User_id, Project: line.Project}) MERGE (u)-[:WORKING_ON]->(p)",
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/skill.csv' AS line MATCH (u:user {User_id: line.User_Id}) MERGE (s:skill { Skill: line.`Skill `})MERGE (u)-[:SKILLED_ON {Skill_level: toInteger(line.`Skill level`) }]->(s)",
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/interest.csv' AS line MATCH (u:user {User_id: line.User_id}) MERGE (i:interest {Interest: line.`Interest` })MERGE (u)-[:INTERESTED_IN {InterestLevel: toInteger(line.`Interest level`)} ]->(i)",
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/organization.csv' AS line MATCH (u:user {User_id: line.User_id}) MERGE (o:organization {organization: line.`organization`, organization_type: line.`organization type`})MERGE (u)-[:WORKS_FOR]->(o)",
            "LOAD CSV WITH HEADERS FROM 'file:///project1_test/distance.csv' AS line MATCH (o1:organization {organization: line.`Organization 1`}) MATCH (o2:organization {organization: line.`Organization 2`}) MERGE (o1)-[:DISTANCE {Distance: toInteger(line.Distance)}]->(o2)"
        ]
        # self.setup_node_list = [
        #     "CREATE (u1:User {First_Name:'Eli', Last_Name:'Augustin', Project: 'Backend', User_Id:1})",
        #     "CREATE (u2:User {First_Name:'Bob', Last_Name:'Mcintosh', Project: 'Backend', User_Id:3})",
        #     "CREATE (u4:User {First_Name:'Sandy', Last_Name:'Anderson', Project: 'Capstone', User_Id:4})",
        #     "CREATE (u5:User {First_Name:'Jake', Last_Name:'Ryan', Project: 'Capstone', User_Id:5})",
        #     "CREATE (u3:User {First_Name:'Ruby', Last_Name:'Rodriguez', Project:'Frontend', User_Id:6})",
        #     "CREATE (u6:User {First_Name:'Amy', Last_Name:'Pascal', Project: 'Data Discovery', User_Id:7})",
        #     "CREATE (u7:User {First_Name:'Navid', Last_Name:'Saboori',  Project: 'Data Discovery', User_Id:8})",
        #     "CREATE (u9:User {First_Name:'Paul', Last_Name:'Wade', ProjectProject: 'Backend', User_Id:2})",
        #     "CREATE (o1:Organization {organization: 'Hunter College', organization_type:'University'})",
        #     "CREATE (o2:Organization {organization: 'SSC', organization_type:'Company'})",
        #     "CREATE (o3:Organization {organization: 'NSA', organization_type:'Government'})",
        #     "CREATE (s:Skill {Skill:'Python'})",
        #     "CREATE (s1:Skill {Skill:'Java'})",
        #     "CREATE (s2:Skill {Skill:'C++'})",
        #     "CREATE (s3:Skill {Skill:'Julia'})",
        #     "CREATE (s4:Skill {Skill:'Genetic Algorithms'})",
        #     "CREATE (s5:Skill {Skill:'Discrete Math'})",
        #     "CREATE (s6:Skill {Skill:'Accounting'})",
        #     "CREATE (s7:Skill {Skill:'Copywriting'})",
        #     "CREATE (s8:Skill {Skill:'Foreign Languages'})",
        #     "CREATE (s9:Skill {Skill:'Web Development'})",
        #     "CREATE (s10:Skill {Skill:'Critical Thinking'})",
        #     "CREATE (s11:Skill {Skill:'Communication'})",
        #     "CREATE (s12:Skill {Skill:'Time Management'})",
        #     "CREATE (s13:Skill {Skill:'Statistical Analysis'})",
        #     "CREATE (s14:Skill {Skill:'Software Development'})",
        #     "CREATE (s15:Skill {Skill:'MySQL'})",
        #     "CREATE (s16:Skill {Skill:'Linux'})",
        #     "CREATE (s17:Skill {Skill:'Information Security'})",
        #     "CREATE (s18:Skill {Skill:'Data Modeling'})",
        #     "CREATE (s19:Skill {Skill:'Networking'})",
        #     "CREATE (s22:Skill {Skill:'McAfee'})",
        #     "CREATE (s20:Skill {Skill:'Javascript'})",
        #     "CREATE (s21:Skill {Skill:'HTML'})",
        #     "CREATE (i1:Interest {Interest:'Weightlifting'})",
        #     "CREATE (i2:Interest {Interest:'Bowling'})",
        #     "CREATE (i3:Interest {Interest:'Swimming'})",
        #     "CREATE (i4:Interest {Interest:'Basketball'})",
        #     "CREATE (i5:Interest {Interest:'Ultimate Frisbee'})",
        #     "CREATE (i6:Interest {Interest:'Kart racing'})",
        #     "CREATE (i7:Interest {Interest:'Traveling'})",
        #     "CREATE (i8:Interest {Interest:'Martial Arts'})",
        #     "CREATE (i9:Interest {Interest:'Videogames'})",
        #     "CREATE (i10:Interest {Interest:'Hiking'})",
        #     "CREATE (i11:Interest {Interest:'Cycling'})",
        #     "CREATE (i12:Interest {Interest:'Volleyball'})",
        #     "CREATE (i13:Interest {Interest:'Boxing'})",
        #     "CREATE (i14:Interest {Interest:'Gardening'})"
        #
        #     ]
        # self.relationship_list = [
        #     "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Eli'}),(b:Skill {Skill:'Java'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Java'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'Time Management'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Networking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Communication'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Skill {Skill:'Software Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Networking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Communication'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Skill {Skill:'Software Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Javascript'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'HTML'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Skill {Skill:'Accounting'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Web Development'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Information Security'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Skill {Skill:'Copywriting'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 1}]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Information Security'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'C++'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Foreign Languages'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 2}]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'MySQL'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 3}]->(b)",
        #
        #     "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Python'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Linux'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #     "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'McAfee'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 5}]->(b)",
        #     "MATCH (a:User {First_Name:'Navid'}),(b:Skill {Skill:'Critical Thinking'}) MERGE (a)-[r:SKILLED_IN {Skill_Level: 4}]->(b)",
        #
        #     "MATCH (a:User {First_Name:'Eli'}), (b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Navid'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Bob'}),(b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(b:Organization {organization:'SSC'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Jake'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Amy'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:User {First_Name:'Paul'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:WORKS_FOR]->(b)",
        #     "MATCH (a:Organization {organization:'SSC'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",
        #     "MATCH (a:Organization {organization:'SSC'}),(b:Organization {organization:'Hunter College'}) MERGE (a)-[r:DISTANCE {miles: 8}]->(b)",
        #     "MATCH (a:Organization {organization:'Hunter College'}),(b:Organization {organization:'NSA'}) MERGE (a)-[r:DISTANCE {miles: 20}]->(b)",
        #
        #     "MATCH (a:User {First_Name:'Eli'}),(i:Interest {Interest:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Eli'}),(i:Interest {Interest:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Eli'}),(i:Interest {Interest:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 7}]->(i)",
        #     "MATCH (a:User {First_Name:'Eli'}),(i:Interest {Interest:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 2}]->(i)",
        #     "MATCH (a:User {First_Name:'Eli'}),(i:Interest {Interest:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 9}]->(i)",
        #     "MATCH (a:User {First_Name:'Bob'}),(i:Interest {Interest:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 5}]->(i)",
        #     "MATCH (a:User {First_Name:'Bob'}),(i:Interest {Interest:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 3}]->(i)",
        #     "MATCH (a:User {First_Name:'Bob'}),(i:Interest {Interest:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Bob'}),(i:Interest {Interest:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 8}]->(i)",
        #     "MATCH (a:User {First_Name:'Bob'}),(i:Interest {Interest:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {Interest:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 2}]->(i)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {Interest:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 8}]->(i)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {Interest:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 7}]->(i)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {Interest:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Sandy'}),(i:Interest {Interest:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 5}]->(i)",
        #     "MATCH (a:User {First_Name:'Jake'}),(i:Interest {Interest:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Jake'}),(i:Interest {Interest:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Jake'}),(i:Interest {Interest:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 9}]->(i)",
        #     "MATCH (a:User {First_Name:'Jake'}),(i:Interest {Interest:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Jake'}),(i:Interest {Interest:'Videogames'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 7}]->(i)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {Interest:'Bowling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 5}]->(i)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {Interest:'Traveling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 5}]->(i)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {Interest:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {Interest:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 8}]->(i)",
        #     "MATCH (a:User {First_Name:'Ruby'}),(i:Interest {Interest:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Amy'}),(i:Interest {Interest:'Gardening'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 9}]->(i)",
        #     "MATCH (a:User {First_Name:'Amy'}),(i:Interest {Interest:'Volleyball'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Amy'}),(i:Interest {Interest:'Swimming'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Amy'}),(i:Interest {Interest:'Kart racing'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 7}]->(i)",
        #     "MATCH (a:User {First_Name:'Amy'}),(i:Interest {Interest:'Cycling'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Paul'}),(i:Interest {Interest:'Weightlifting'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 4}]->(i)",
        #     "MATCH (a:User {First_Name:'Paul'}),(i:Interest {Interest:'Ultimate Frisbee'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 6}]->(i)",
        #     "MATCH (a:User {First_Name:'Paul'}),(i:Interest {Interest:'Martial Arts'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 7}]->(i)",
        #     "MATCH (a:User {First_Name:'Paul'}),(i:Interest {Interest:'Hiking'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 2}]->(i)",
        #     "MATCH (a:User {First_Name:'Paul'}),(i:Interest {Interest:'Basketball'}) MERGE (a)-[r:INTERESTED_IN {Interest_Level: 9}]->(i)"
        # ]

    def setup(self):
        self.graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
        for s in self.setup_node_list:
            self.graph.run(s)
        for r in self.relationship_list:
            self.graph.run(r)

    def dump_csv(self):
        for com in self.csv_command_list:
            self.graph.run(com)

    def get_all_users(self):
        query_string = """MATCH (u:user)-[]->(o:organization)
                        RETURN u.name as Name,
                        o.organization as OrgName, o.organization_type as OrgType"""
        return pd.DataFrame(self.graph.run(query_string).data()).to_string()


    def query_for_answer_1(self, username, company_name):
        query_string = """
        MATCH (u:user)-[r1]-(s:skill)-[]-(u1:user)-[]-(o:organization)-[r2]-(o1:organization)
        WHERE u1.name='{}' and (o.organization="{}" or (o1.organization="{}" and r2.Distance <= 10) )
        WITH DISTINCT u.name as name, o.organization as organization, collect(s.Skill) as Common_Skills, sum(r1.Skill_level) as weight
        ORDER BY weight DESC
        RETURN name, organization, Common_Skills, weight""".format(username, company_name, company_name)
        print( pd.DataFrame(self.graph.run(query_string).data()).to_string() )
