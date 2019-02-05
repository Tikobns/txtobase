from pymongo import MongoClient
import os
import sys

print("The text to base Convertor. Will understand That, Who will understand.")
print("USAGE: Type 1: if one file \n       Type 2: if files are many")
print("P.S: if your choise is 2. make all file in one dir please")

choise = int(input("Your Choice: "))
client = MongoClient('localhost', 27017)
db = client['leakScraper']
collection1 = db["credentials"]
def conver(file, type):
    if type == 1:
        openedf = open(str(file), "r")
        readed = openedf.read()
        print(readed)
    elif type == 2:
        for i in os.listdir(file):
            path = file + str(i)
            anyoped = open(path, "r")
            reads = anyoped.readlines()
            for line in reads:
                user = line.split("::")[0]
                paswd = line.split("::")[1]
                post = {"user" : str(user),
                        "pass" : str(paswd)}
                posts = db.posts
                post_id = posts.insert_one(post).inserted_id
                print(post_id)

		
if choise == 1:
    file = input("path_to_file: ")
    conver(file, 1)
elif choise == 2:
    file = input("path_to_dir: ")
    conver(file, 2)
else:
    print("use 1 or 2 please")
    exit()



