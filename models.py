from flask_mysqldb import MySQL

def create_user(mysql: MySQL, email: str, password_hash: str):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password_hash))
    mysql.connection.commit()
    cursor.close()

def get_user_by_email(mysql: MySQL, email: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", [email])
    user = cursor.fetchone()
    cursor.close()
    return user

def create_contact(mysql: MySQL, user_id: int, name: str, email: str, phone: str):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO contacts (user_id, name, email, phone) VALUES (%s, %s, %s, %s)", (user_id, name, email, phone))
    mysql.connection.commit()
    cursor.close()

def get_contacts_by_user(mysql: MySQL, user_id: int):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE user_id = %s", [user_id])
    contacts = cursor.fetchall()
    cursor.close()
    return contacts

def get_contact_by_id(mysql: MySQL, contact_id: int, user_id: int):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = %s AND user_id = %s", (contact_id, user_id))
    contact = cursor.fetchone()
    cursor.close()
    return contact
