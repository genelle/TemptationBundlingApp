import sqlite3

conn = sqlite3.connect('tempBundling.db')
cur = conn.cursor()

def main():
    answer = raw_input("Do you have an account? Y/N ")
    
    if answer == "N" or answer == "n":
        db_username = new_user()
            
    else:
        while(True):
            username = raw_input("Please enter your username: ")
            cur.execute('SELECT user_id, username from users where username = ? ', (username, ) )
            db_username = cur.fetchone()


            if db_username == None:
                print "I'm sorry, I didn't recognize your username."
                print "Please try again."
                continue
                
            else:
                break
    
    print "Hi, %s, let's get started!" %db_username[1]
    #initial menu
    while(True):
    
        print "Main Menu:"
        print "1. Add task/habit to track."
        print "2. Track task/habit you accomplished."
        print "3. Add reward to list of redeemable rewards."
        print "4. Redeem award."
        print "5. Print current week's accomplishments and rewards redeemed."
        print "6. Update user preferences."
        #week start on sunday or monday?
        print "7. Exit."
    
        choice = raw_input("What would you like to do?")
        
        if choice == 1 or 2:
            print "The following are the tasks/habits you"
            print "have indicated you want to track."
    
            print_tasks(db_username[0])
            print "--------------------------"
            print "\n"
            
            if choice == 1:
                #def add-task(db_username[0])
                continue
            else:
                #def track-task(db_username[0])
                continue
                
        elif choice == 3 or 4:  
            print "The following are the rewards you"
            print "have indicated you want to track."
    
            #print_rewards(db_username[0])
            print "--------------------------"
            print "\n"
            
        
        
        conn.commit()

    cur.close()
    

def update_habit(user_id):
    task_to_update = raw_input("So what task would you like to update?")
    #need to put option in if user types in habit that doesn't exist
    #or maybe just have user choose 1,2, etc.
    cur.execute('SELECT habit_id, hourly from habits where habit_name = ? ', (task_to_update, ) )
    task_info = cur.fetchone()
       
    try:
        habit_id = task_info[0]
        hourly = task_info[1]
        if hourly == 0:
            #update the non hourly task for the user
            #needs to take user_id as well
            Upd_non_hourly_task(habit_id)
        else:
            #update the hourly task for the user
            #needs to take user_id as well
                Upd_hourly_task(habit_id)
    except TypeError:
        print "ooops"
        


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
            user_id = cur.lastrowid
            break
            
        else:
            print "I'm sorry, that username name is taken. Please try again."
            continue
    return (user_id,username)
    
def print_tasks(user_id):
    """
    Prints habits/tasks that the user has indicated they want to track
    """

    cur.execute('SELECT habit_id from user_habit where user_id = ? ', (user_id, ))
    db_tasks = cur.fetchall()
    
    #Stack Overflow, ljust tabular output
    print "{} {}".format("Tasks:".ljust(20),"Description:".ljust(20))
    for habit_id in db_tasks:

        cur.execute('SELECT habit_name, habit_desc from habits where habit_id = ?', (habit_id[0], ))
        db_habit = cur.fetchone()
        
        print "{} {}".format(db_habit[0].ljust(20),db_habit[1].ljust(20))
        
def Upd_non_hourly_task(user_id, habit_id):
    """
    Updates the non-hourly task for the user
    """
    #Need to add database to track users info before writing this code
    #also need to add keeping track of user_id everywhere I grab username
    return True 
    
def Upd_hourly_task(user_id, habit_id):
    return True
    
main()

