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

def getClassmate():
    allPeople = {}
    while True:
        a = raw_input('Continue? y/n')
        if a == 'y':
            name = raw_input('input the name')
            num = raw_input('input the num')
            tel = raw_input('input the tel')
            email = raw_input("Input the email")
            classmate = Classmate(name, num, tel, email)
            allPeople[name] = classmate
            allPeople[num] = classmate
        else:
            return allPeople

def searchClassmate(allPeople):
    while True:
        a = raw_input('Continue? y/n')
        if a == 'y':
            item = raw_input("Please input the name or id of your classmate")
            people = allPeople[item]
            print people
        else:
            break
            
def main():
    allPeople = getClassmate()
    searchClassmate(allPeople)

main()
