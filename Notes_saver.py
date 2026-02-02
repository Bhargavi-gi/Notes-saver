import mysql.connector
from datetime import date
 
# ---------- Connection ----------
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chinni@1901",   # change here
        database="Notes_saver"
    )
 
# ---------- Common Function to Execute Queries ----------
def run_query(query, values=(), fetch=False):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
 
    if fetch:
        result = cursor.fetchall()
        conn.close()
        return result
 
    conn.commit()
    conn.close()
 
# ---------- Add Note ----------
def add_note():
    title = input("Title: ")
    content = input("Content: ")
 
    if not title or not content:
        print("❌ Cannot be empty")
        return
 
    today = date.today()
    q = "INSERT INTO notes (title, content, note_date) VALUES (%s, %s, %s)"
    run_query(q, (title, content, today))
    print("✅ Note added")
 
# ---------- View Notes ----------
def view_notes():
    rows = run_query("SELECT * FROM notes", fetch=True)
    for r in rows:
        print(f"\nID:{r[0]} | {r[1]} | {r[3]}")
        print(r[2])
 
# ---------- Search ----------
def search_note():
    key = "%" + input("Search: ") + "%"
    q = "SELECT * FROM notes WHERE title LIKE %s OR content LIKE %s"
    rows = run_query(q, (key, key), True)
 
    for r in rows:
        print(f"\nID:{r[0]} | {r[1]} | {r[3]}")
        print(r[2])
 
# ---------- Update ----------
def update_note():
    nid = input("ID to update: ")
    title = input("New Title: ")
    content = input("New Content: ")
 
    q = "UPDATE notes SET title=%s, content=%s WHERE id=%s"
    run_query(q, (title, content, nid))
    print("✅ Updated")
 
# ---------- Delete ----------
def delete_note():
    nid = input("ID to delete: ")
    run_query("DELETE FROM notes WHERE id=%s", (nid,))
    print("✅ Deleted")
 
# ---------- Menu ----------
while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    ch = input("Choice: ")
 
    if ch == '1': add_note()
    elif ch == '2': view_notes()
    elif ch == '3': search_note()
    elif ch == '4': update_note()
    elif ch == '5': delete_note()
    elif ch == '6': break
    else: print("Invalid")
 