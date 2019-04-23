import sqlite3

#Create DB from an unparsed text file

def parse_task_file(fileLoc):
    f = open(fileLoc)
    try:
        lines = f.readlines()
    except:
        print "Error parsing file:", fileLoc
        raise
    finally:
        f.close()

    # im just fucking around at this point
    return map(lambda x: map(lambda y: y.replace("~", ""), x.split("^")[:-2]), lines)


def init_and_populate_food_DB(dbname, task_file_loc):
    try:
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()
        curs.execute(
            "CREATE TABLE IF NOT EXISTS food(code TEXT, descript TEXT, nmbr integer, nutname TEXT, retention integer)")

        itemLists = parse_task_file(task_file_loc)
        for itemList in itemLists:
            curs.execute("INSERT INTO food values(?, ?, ?, ?, ?)", (itemList[0], itemList[1], itemList[2], itemList[3], itemList[4]))
        conn.commit()
    except:
        print "There was a problem creating and populating the DB"
        raise
    finally:
        curs.close()
        conn.close()


task_DB_name = "FOOD_DB.db"
db_data_loc = "./foodData.txt"

init_and_populate_food_DB(task_DB_name, db_data_loc)

conn = sqlite3.connect("FOOD_DB.db")
curs = conn.cursor()
curs.execute("Select * from food")
print curs.fetchall()
