from flask import Flask, render_template, abort, request, redirect, flash, jsonify
import os
from dotenv import load_dotenv
from models import db, Contact

# Load environment variables
load_dotenv()

server = Flask(__name__)

# Database Configuration - Use SQLite as fallback for compatibility

database_url = os.getenv('DATABASE_URL')
if database_url and database_url.startswith('postgresql'):
    server.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Use /tmp for SQLite on Render (always writable)
    server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/redstore.db'

server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Initialize database
db.init_app(server)

@server.route('/')
def home():
    return render_template('index.html')

@server.route('/<page>.html')
def render_page(page):
    # Only allow rendering of known templates for security
    allowed_pages = [
        'about', 'account', 'product', 'contact', 'productsdetails', 'cart', 'thankyou', 'admin'
    ]
    if page in allowed_pages:
        return render_template(f'{page}.html')
    abort(404)

@server.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            
            # Basic validation
            if not data.get('email') or not data.get('subject') or not data.get('message'):
                flash('All fields are required!', 'error')
                return redirect('contact.html')
            
            # Email validation (basic)
            if '@' not in data['email']:
                flash('Please enter a valid email address!', 'error')
                return redirect('contact.html')
            
            # Save to database
            new_contact = Contact(
                email=data['email'],
                subject=data['subject'],
                message=data['message']
            )
            
            db.session.add(new_contact)
            db.session.commit()
            
            flash('Message sent successfully!', 'success')
            return redirect('thankyou.html')
            
        except Exception as e:
            db.session.rollback()
            flash('Could not save to database. Please try again.', 'error')
            return redirect('contact.html')
    else:
        return redirect('contact.html')

# Admin route to view submissions (for development/testing)
@server.route('/admin/submissions')
def view_submissions():
    try:
        contacts = Contact.query.order_by(Contact.created_at.desc()).all()
        return jsonify([contact.to_dict() for contact in contacts])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Database initialization route (for manual setup)
@server.route('/init-db')
def init_database():
    try:
        with server.app_context():
            db.create_all()
        return jsonify({'message': 'Database tables created successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@server.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@server.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@server.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Create database tables
def create_tables():
    with server.app_context():
        try:
            db.create_all()
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"❌ Error creating database tables: {e}")

if __name__ == '__main__':
    # Create tables if they don't exist
    create_tables()
    
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    server.run(debug=debug_mode, host='0.0.0.0', port=5000)