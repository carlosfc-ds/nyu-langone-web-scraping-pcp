from pymongo import MongoClient

def main():
    # 1. Connect to MongoDB (change the URI if needed)
    client = MongoClient("mongodb://127.0.0.1:27017")

    # 2. Get a database and collection
    db = client["pymongo_test_db"]
    collection = db["pymongo_test_collection"]

    # 3. Insert a simple document
    doc = {"message": "Hello from PyMongo!", "ok": True}
    result = collection.insert_one(doc)

    # 4. Read the document back
    found = collection.find_one({"_id": result.inserted_id})

    print("Inserted _id:", result.inserted_id)
    print("Found document:", found)

    # 5. Clean up (optional)
    db.drop_collection("pymongo_test_collection")

if __name__ == "__main__":
    main()
