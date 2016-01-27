import sqlite3

conn = sqlite3.connect('tempBundling.db')
cur = conn.cursor()

def main():
    answer = raw_input("Do you have an account? Y/N ")
    
    if answer == "N":
        username = new_user()
            
    else:
        while(True):
            username = raw_input("Please enter your username: ")
            cur.execute('SELECT username from users where username = ? ', (username, ) )
            db_username = cur.fetchone()


            if db_username == None:
                print "I'm sorry, I didn't recognize your username."
                continue
                
            else:
                break
    
    print "Hi, %s, let's get started!" %username
    print "The following are the tasks you"
    print "have indicated you want to track."
    
    print_tasks(username)
    print "--------------------------"
    print "\n"
    
    #put while loop here, asks user what they would like to do
    #write up different functions for each option
    task_to_update = raw_input("So what task would you like to update?")
    


def new_user():
    """
    Creates a new user in the database
    """
    print "Then let's set you up with your account!"
    
    while(True):
        username = raw_input("Please enter your desired username: ")
        
        cur.execute('SELECT username from users where username = ? ', (username, ) )
        db_username = cur.fetchone()
        
        if db_username == None:
        
            cur.execute('INSERT INTO users (username) VALUES (?)', (username,) )
            break
            
        else:
            print "I'm sorry, that username name is taken. Please try again."
            continue
    return username
    
def print_tasks(username):
    """
    Prints habits/tasks that the user has indicated they want to track
    """

    cur.execute('SELECT user_id from users where username = ? ', (username, ) )
    db_user_id = cur.fetchone()[0]  
    #Should probably test here that user_id isn't None but I don't run this 
    #unless I have a valid username so it should be okay?
    
    cur.execute('SELECT habit_id from user_habit where user_id = ? ', (db_user_id, ))
    db_tasks = cur.fetchall()
    
    #Stack Overflow, ljust tabular output
    print "{} {}".format("Tasks:".ljust(20),"Description:".ljust(20))
    for habit_id in db_tasks:

        cur.execute('SELECT habit_name, habit_desc from habits where habit_id = ?', (habit_id[0], ))
        db_habit = cur.fetchone()
        
        print "{} {}".format(db_habit[0].ljust(20),db_habit[1].ljust(20))
    
    
    
main()

conn.commit()

cur.close()