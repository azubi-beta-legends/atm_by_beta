import json


def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data


#updating the user data in the json file
def updateData(dataFileJson, userData ):
    with open(dataFileJson, 'w') as json_file2:
        json.dump(userData, json_file2)
        