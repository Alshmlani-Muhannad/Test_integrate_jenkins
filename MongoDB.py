from pymongo import MongoClient, errors

try:
    # Connect to MongoDB (update the connection string if necessary)
    client = MongoClient("mongodb://192.168.200.86:27017/")
    
    # Access the 'test' database (change to your database name if different)
    db = client["creative"]
    name_to_find = 'Mark'
    # Access the 'employees' collection
    collection = db["employees"]
    
    # Query the collection for documents where the name is 'John'
    query = {"first_name": name_to_find}
    
    # Find documents that match the query
    results = collection.find(query)
    
    # Check if any documents were found and print them
    found = False
    for document in results:
        print(document)
        found = True
    
    if not found:
        print("No documents found with the name"+name_to_find)

except errors.ConnectionError as ce:
    print(f"Connection Error: {ce}")
except errors.InvalidName as ine:
    print(f"Invalid Database or Collection Name: {ine}")
except Exception as e:
    print(f"An error occurred: {e}")
