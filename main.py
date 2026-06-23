import substances
import config
import database



def main():
    printDB(database.db)
    # ask foor next dose substance
    # ask for next dose quantity
    # ask for next dose timedate
    # add to db 
    # main()

def printDB(db):
    for key,data in db:
        if data[timedate]+substances.substances[key][life]*5>now:
            print(key,"|",data[timedate],"|",data[dose])
main()
