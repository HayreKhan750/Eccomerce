from flask import Flask, render_template, abort,request,redirect
import csv
import os

server = Flask(__name__)

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


@server.route('/submit_form', methods = ['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "Could not save to database"
    else:
        return "somthing went wrong!"





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
