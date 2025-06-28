from flask import Flask, render_template, abort, request, redirect, flash
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

server = Flask(__name__)
server.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

@server.route('/')
def home():
    return render_template('index.html')

@server.route('/<page>.html')
def render_page(page):
    # Only allow rendering of known templates for security
    allowed_pages = [
        'about', 'account', 'product', 'contact', 'productsdetails', 'cart', 'thankyou'
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
            
            write_to_csv(data)
            flash('Message sent successfully!', 'success')
            return redirect('thankyou.html')
        except Exception as e:
            flash('Could not save to database. Please try again.', 'error')
            return redirect('contact.html')
    else:
        return redirect('contact.html')

def write_to_csv(data):
    file_path = 'database.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only once, if the file is new
        if not file_exists or os.stat(file_path).st_size == 0:
            writer.writeheader()

        # Write the actual form data
        writer.writerow({
            'email': data['email'],
            'subject': data['subject'],
            'message': data['message']
        })

@server.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@server.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    server.run(debug=debug_mode, host='0.0.0.0', port=5000)
