import mysql.connector as mysql

con = mysql.connect(host="localhost", user="root", passwd="admin")
cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
cursor.execute("USE TODOAPP")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")

for i in cursor:
    print(i)

while True:
    print("\n=== Task Management System ===")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Update an Existing Task")
    print("4. Remove a Task")
    print("5. Exit")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        task = input("Enter the task description: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        con.commit()
        print("✅ Task successfully added!")

    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if tasks:
            print("\n📌 Your Task List:")
            for task in tasks:
                print(f"🔹 {task[0]}. {task[1]} ({task[2]})")
        else:
            print("ℹ️ No tasks found!")

    elif choice == "3":
        task_id = input("Enter the Task ID to update: ")
        new_task = input("Enter the updated task description: ")
        cursor.execute("UPDATE tb_todo SET task = %s WHERE id = %s", (new_task, task_id))
        con.commit()
        print("✏️ Task updated successfully!")

    elif choice == "4":
        task_id = input("Enter the Task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        print("🗑️ Task deleted successfully!")

    elif choice == "5":
        print("👋 Exiting Task Management System... Goodbye!")
        break

    else:
        print("❌ Invalid selection! Please enter a number between 1-5.")

cursor.close()
con.close()
