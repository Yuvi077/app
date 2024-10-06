from flask import Flask, request, jsonify
import mysql.connector as c

app = Flask(__name__)

# Database connection
con = c.connect(user='root', host="localhost", passwd="admin", database="blood_bank")
cur = con.cursor()

@app.route('/register', methods=['POST'])
def register():
    try:
        # Get form data
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        blood_group = request.form['bloodGroup']
        email = request.form['email']
        address = request.form['address']
        contact_number = request.form['contactNumber']

        # Insert the data into MySQL
        query = """
        INSERT INTO donors (name, age, gender, blood_group, email, address, contact_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (name, age, gender, blood_group, email, address, contact_number))
        con.commit()

        return jsonify({'message': 'Registration successful!'})

    except Exception as e:
        con.rollback()  # Roll back in case of error
        return jsonify({'error': str(e)}), 500

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)

