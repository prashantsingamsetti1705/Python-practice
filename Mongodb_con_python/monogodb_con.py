#wite a python program wchich connent the monogodb
# Import the required libraries:
from pymongo import MongoClient,errors
try:
    # Establish a connection to the MongoDB server:
    client = MongoClient("mongodb://localhost:27017/")
    # Select the database and collection:
    db = client["your_database_name"]
    # Perform operations on the collection:
    collection = db["your_collection_name"]
    print("your amngo db is conected sucessfully")
except errors.ServerSelectionTimeoutError as err:
    print("Could not connect to MongoDB server:", err)

except errors.ConnectionFailure as err:
    print("MongoDB connection failed:", err)

except errors.OperationFailure as err:
    print("MongoDB operation failed:", err)

except Exception as e:
    print("An error occurred:", e)
