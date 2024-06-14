from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="testdb"
)

cursor = db.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        users = []
        
        for user in result:
            user_dict = {
                'id': user[0],
                'name': user[1],
                'age': user[2]
            }
            users.append(user_dict)
        
        return jsonify(users), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        
        if result:
            user = {
                'id': result[0],
                'name': result[1],
                'age': result[2]
            }
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        db.commit()
        
        return jsonify({"message": "User added successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        
        cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
        db.commit()
        
        return jsonify({"message": "User updated successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        db.commit()
        
        return jsonify({"message": "User deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
