import mysql.connector

conn = mysql.connector.connect( 
    user="ardit700_student", 
    password="ardit700_student", 
    host="108.167.140.122", 
    database="ardit700_pm1database",
    connect_timeout=300, 
) 

cursor = conn.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")