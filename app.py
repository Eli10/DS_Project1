from db import MongoDB




db = MongoDB()
print(db.client.database_names())
