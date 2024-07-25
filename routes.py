from flask import Flask, request, jsonify, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

def setup_routes(app, mysql):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
    
        hashed_password = generate_password_hash(password)
        
     
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify(message="User registered successfully"), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
      
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cursor.fetchone()
        cursor.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return jsonify(message="Login successful"), 200
        else:
            return jsonify(message="Invalid credentials"), 401

    @app.route('/add_contact', methods=['POST'])
    def add_contact():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        user_id = session.get('user_id')
        
        if not user_id:
            return jsonify(message="User not logged in"), 401
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO contacts (user_id, name, email, phone) VALUES (%s, %s, %s, %s)", (user_id, name, email, phone))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify(message="Contact added successfully"), 201

    @app.route('/contacts', methods=['GET'])
    def contacts():
        user_id = session.get('user_id')
        
        if not user_id:
            return jsonify(message="User not logged in"), 401
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE user_id = %s", [user_id])
        contacts = cursor.fetchall()
        cursor.close()
        
        return jsonify(contacts=contacts), 200

    @app.route('/contact/<int:contact_id>', methods=['GET'])
    def contact_details(contact_id):
        user_id = session.get('user_id')
        
        if not user_id:
            return jsonify(message="User not logged in"), 401
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = %s AND user_id = %s", (contact_id, user_id))
        contact = cursor.fetchone()
        cursor.close()
        
        if contact:
            return jsonify(contact=contact), 200
        else:
            return jsonify(message="Contact not found"), 404
