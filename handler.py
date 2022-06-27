import json
import pyrebase, firebase_admin
from firebase_admin import credentials, firestore

def authFS():
    cred = credentials.Certificate("/path/to/firebase-config.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

# testing with firestore-collections
# doc_ref = db.collection('siege-pl-eul22-s2')
# docs = doc_ref.stream()
# print(docs)
# t = list(doc_ref.stream())
# print(len(t))
# # print(str(len(list(docs()))))
# for doc in docs:
#     if bool(doc.to_dict()):
#         print('{} => {} '.format(doc.id, doc.to_dict()))

def enterDictToDb(data):
    db = authFS()

    doc_ref = db.collection('collection-name').document(data.get("id"))
    doc = doc_ref.get()
    if doc.exists:
        print("exists")


# .replace(" ", "").lower()
