import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL              
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_videos(Video_ID, newName, newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(newName,newTime,Video_ID))
    conn.commit()

def delete_videos(Video_Id):
    cursor.execute("DELETE FROM videos where id = ?", (Video_Id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List Videos of DB")
        print("2. Add Videos in DB")
        print("3. Update Videos in DB")
        print("4. Delete videos in DB")
        print("5. Exit App")
        choice = input("Enter Your Choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        
        elif choice == '3':
            Video_ID = input("Enter Your Video number: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(Video_ID, name, time)

        elif choice == '4':
            Video_ID = input("Enter Your Video number: ")
            delete_videos(Video_ID)

        elif choice == '5':
            break
        
        else:
            print("Invalid Choice")

    conn.close()
if __name__ == "__main__":
    main()