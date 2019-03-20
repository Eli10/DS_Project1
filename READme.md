
# Project Questions
1) Do users only have one organization and project that they work for? Or do we store a history of past current organizations and projects that a user has either worked for or worked on?
2) Are we suppose to store the location of an organization?
3) If yes to Question 2, how so? Latitude and Longitude?


# Mongo Data Models

User
- First Name (string)
- Last Name (string)
- Organization (object)
- Skills (list of dictionaries (skill_name: weight))
- Project (string)

# Neo4j Data Models

User
- Nane
- Current Project

Organization
- name
- type


Skil
- name

Interest
- name

Relations
- User WORKS_FOR Organization
- Orgnization DISTANCE Organization
- User SKILLED_In Skill (level property)
- User INTERESTED_IN Interest (level property)


# Menu Options
 1) Create User (Creates user in both databases)
 2) Run Direct Query (Must pick with database to Query)
 3) Answer the first Question Given list of interests
 4) Answer the second Question for a user

# Databases
- MongoDB
- Neo4j



# Queries

db.getCollection('users').find({$or: [{"Organization.OrgType": "University"}, {"Organization.Distances.Government": {$lte: 10}  }, {"Organization.Distances.Company": {$lte: 10}  } ]})

----------

var my_skills = ["Python", "Go"]

db.getCollection('users').find({$or: [{"Organization.OrgType": "University"}, {"Organization.Distances.Government": {$lte: 10}  }, {"Organization.Distances.Company": {$lte: 10}  } ]}).forEach(function(user) {
    
    var user_skills = user.Skills;
    //print(user_skills);
    var total_weight = 0;
    //var user_skill_list = Object.keys(user.Skills)
    my_skills.forEach(function(skill) {
            if( skill in user_skills) {
                    total_weight = total_weight + user_skills[skill]
            }
    });
    //print(total_weight)
    //print(user_skill_list)
    
    print( user.FirstName, user.Organization.OrgName, total_weight);
    
});



db.getCollection('users').find({"CurrentProject": "Back-end"}, {"FirstName": 1, "LastName": 1 ,"Skills": 1})


# Installation
- Install and run pyhton3 and pip or pip3
- Install and start neo4j and mongodb

Run the Makefile 
- make run

or the following commands
- pip3 install pymongo
- pip3 install pandas
- pip3 install neo4j
