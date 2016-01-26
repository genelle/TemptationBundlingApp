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

            if db_username[0] == username:
                break
                
            else:
                print "I'm sorry, I didn't recognize your username."
                continue
    
    print "Hi, %s, let's get started!" %username


def new_user():
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
    
main()

conn.commit()

cur.close()