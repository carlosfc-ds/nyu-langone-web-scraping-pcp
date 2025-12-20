# MongoDB Python Driver (PyMongo) Setup

This guide explains how to install the official MongoDB Python driver **PyMongo** and run a minimal Python script to verify that the driver works correctly.

---

## 1. Prerequisites

Before installing PyMongo, ensure:

- Python 3.x is installed (`python --version` or `python3 --version`)  
- `pip` is available (`pip --version` or `python -m pip --version`)[web:40]  
- A MongoDB instance is running (for local testing, usually at `mongodb://127.0.0.1:27017`)

---

## 2. Install PyMongo

Use `pip` (recommended method):

```bash
# On many systems
python -m pip install pymongo

# Or explicitly with python3
python3 -m pip install pymongo
```

This installs the latest stable version of PyMongo from PyPI.

To upgrade an existing installation:

```bash
python -m pip install --upgrade pymongo
```

## 3. Minimal Test Application
Create a file named test_pymongo.py with the following contents:

```python
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
```

This script demonstrates a basic connect → insert → read → cleanup flow using PyMongo.

## 4. Run the Test Application
Make sure MongoDB is running (for example, locally on port 27017).

In a terminal in the same folder as test_pymongo.py, run:

```bash
python test_pymongo.py
```
You should see output similar to:
```text
Inserted _id: 651f...
Found document: {'_id': ObjectId('651f...'), 'message': 'Hello from PyMongo!', 'ok': True}
```
This indicates that:

- The PyMongo driver imported successfully

- The client connected to MongoDB

- A document was inserted and then read back correctly

## 5. Common Issues
``ModuleNotFoundError: No module named 'pymongo'``

- Ensure you installed PyMongo in the same Python environment you are using to run the script (``python -m pip install pymongo``).

Connection errors (e.g., ``ServerSelectionTimeoutError``)

- Confirm MongoDB is running and listening on the URI you used (default local is ``mongodb://127.0.0.1:27017``).

Once this test works, you can reuse the same connection pattern (MongoClient, select DB, select collection) in your real application code.