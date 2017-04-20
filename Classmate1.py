class Classmate:
    def __init__(self, name, num, tel, email):
        self.name = name
        self.num = num
        self.tel = tel
        self.email = email

    def newName(self, name):
        self.name = name

    def newNum(self, num):
        self.num = num

    def newTel(self, tel):
        self.tel = tel

    def newEmail(self, email):
        self.email = email

    def __str__(self):
        return "%s %s %s % s" % (self.name, self.num, self.tel, self.email)

def getClassmate(allPeople):
    People = allPeople
    print People
    while True:
        a = raw_input('Continue? y/n')
        if a == 'y':
            name = raw_input('input the name')
            num = raw_input('input the num')
            tel = raw_input('input the tel')
            email = raw_input("Input the email")
            classmate = Classmate(name, num, tel, email)
            People[name] = classmate
            People[num] = classmate
            return People

def searchClassmate(allPeople):
    while True:
        a = raw_input('Continue? y/n')
        if a == 'y':
            item = raw_input("Please input the name or id of your classmate")
            people = allPeople[item]
            print people
        else:
            break

def doCommand(allPeople):
    print 'Read(1) Search(2) Save(3) Add(4) Refresh(5) Delete(6) Exit(7)'
    command = input("Please input the command")
    if command == 1:
        allPeople = readFile()
        return allPeople
    elif command == 2:
        search(allPeople)
        return allPeople
    elif command == 3:
        saveFile(allPeople)
        return allPeople
    elif command == 4:
        temp = add(allPeople)
        return temp
    elif command == 5:
        refresh(allPeople)
    elif command == 6:
        temp = delete(allPeople)
        return allPeople
    elif command == 7:
        leave()

def readFile():
    infilename = raw_input("Please input the directory and filename you want to open")
    infile = open(infilename, 'r')
    allPeople = {}
    while True:
        text = infile.readline()
        if text == "":
            break
        content = text.split()
        name = content[0]
        num = content[1]
        tel = content[2]
        email = content[3]
        classmate = Classmate(name, num, tel, email)
        allPeople[name] = classmate
    return allPeople

def search(allPeople):
    searchClassmate(allPeople)
    return allPeople
    

def saveFile(allPeople):
    infilename = raw_input("Please input the dir and name")
    infile = open(infilename, 'w')
    for key, value in allPeople.iteritems():
        temp = [key, value]
        name = temp[1].name
        num = temp[1].num
        tel = temp[1].tel
        email = temp[1].email
        message = str(name) + ' ' + str(num) + str(tel) + ' ' + str(email)
        infile.write(message)
        infile.write('\n')
    return allPeople

def add(allPeople):
    temp = getClassmate(allPeople)
    return temp

def delete(People):
    s = raw_input("Enter the classmates you want to delete")
    del allPeople[s]
    return allPeople

def refresh(allPeople):
    return allPeople

def leave():
    return 1
def main():
    wholePeople ={}
    while True:
         temp = doCommand(wholePeople)
         if temp == 1:
             break
         else:
             wholePeople = temp

main()
