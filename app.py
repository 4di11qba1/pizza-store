from flask import Flask, render_template, session, jsonify
from db import initialize_db
from routes import api_bp

app = Flask(__name__)

app.secret_key = 'mysecretkey'

# MongoDB configuration
app.config['MONGODB_SETTINGS'] = {
    'db': 'PIZZA',
    'host': 'localhost',
    'port': 27017
}

# Initialize DB
initialize_db(app)

# Register API Blueprint
app.register_blueprint(api_bp)

# Routes for rendering HTML pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Function to check session
@app.route('/api/session', methods=['GET'])
def check_session():
    admin_session = session.get('admin')
    print(f"Admin session value: {admin_session}")

    if admin_session is not None:
        return "true", 200  # Return as string with 200 status
    else:
        return "false", 403  # Return as string with 403 status



if __name__ == '__main__':
    app.run(debug=True)
