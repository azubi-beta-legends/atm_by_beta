import json
import csv


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

# the function below is for logging transactions
def loguserData(txtfile, transactdatetime, transactype, transactamount, recipient, oldbalance, updatedbalance):
    log_data = [str(transactdatetime), transactype, str(transactamount), str(recipient), str(oldbalance), str(updatedbalance)]
    with open(txtfile, 'w') as userfile:
        writer = csv.writer(userfile)
        writer.writerow(log_data)

def logallData(txtfile, userID, transactdatetime, transactype, transactamount, recipient, oldbalance, updatedbalance):
    log_data = [str(userID), str(transactdatetime), transactype, str(transactamount), str(recipient), str(oldbalance), str(updatedbalance)]
    with open(txtfile, 'w') as userfile:
        writer = csv.writer(userfile)
        writer.writerow(log_data)

        