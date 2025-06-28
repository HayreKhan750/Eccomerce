# RedStore - E-commerce Website

A modern, responsive e-commerce website built with Flask and MySQL. Features a clean design with product listings, shopping cart functionality, and contact forms with database storage.

## 🚀 Features

- **Responsive Design**: Mobile-friendly interface
- **Product Catalog**: Browse featured and latest products
- **Shopping Cart**: Add and manage items
- **Contact Form**: Customer support with MySQL database storage
- **User Account**: Login and registration pages
- **Live Chat**: Integrated Smartsupp chat widget
- **Google Maps**: Location integration
- **MySQL Database**: Persistent data storage for contact submissions

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- MySQL Server (local or cloud)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/redstore-ecommerce.git
   cd redstore-ecommerce
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up MySQL Database**
   - Install MySQL Server on your machine
   - Create a new database: `redstore_db`
   - Create a user with permissions for this database

6. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   FLASK_APP=server.py
   FLASK_ENV=development
   SECRET_KEY=your-super-secret-key-change-this-in-production
   DATABASE_URL=mysql+pymysql://username:password@localhost/redstore_db
   SMARTSUPP_KEY=your_smartsupp_key_here
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
   ```

7. **Initialize the database**
   ```bash
   python setup_database.py
   ```

## 🚀 Running the Application

1. **Start the Flask server**
   ```bash
   python server.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
redstore-ecommerce/
├── server.py              # Flask application
├── models.py              # Database models
├── setup_database.py      # Database initialization script
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── README.md             # Project documentation
├── .gitignore           # Git ignore rules
├── static/              # Static files
│   ├── images/          # Product and UI images
│   ├── style.css        # Main stylesheet
│   └── script.js        # JavaScript functionality
└── templates/           # HTML templates
    ├── index.html       # Homepage
    ├── product.html     # Product listings
    ├── cart.html        # Shopping cart
    ├── contact.html     # Contact form
    └── ...              # Other pages
```

## 🗄️ Database Schema

### Contacts Table
- `id` (Primary Key)
- `email` (String, Required)
- `subject` (String, Required)
- `message` (Text, Required)
- `created_at` (DateTime, Auto-generated)

## 🌐 Deployment on Render

1. **Push your code to GitHub**

2. **Create a new Web Service on Render**
   - Connect your GitHub repository
   - Use the `render.yaml` configuration

3. **Set up MySQL Database on Render**
   - Create a new MySQL database service
   - Copy the database URL to your web service environment variables

4. **Configure Environment Variables**
   - `DATABASE_URL`: Your Render MySQL database URL
   - `SECRET_KEY`: Generated automatically
   - `SMARTSUPP_KEY`: Your Smartsupp chat key
   - `GOOGLE_MAPS_API_KEY`: Your Google Maps API key

5. **Deploy**
   - Render will automatically build and deploy your application

## 🔒 Security Notes

- API keys are stored in environment variables
- Database credentials are secured
- Form validation is implemented on both client and server side
- SQL injection protection through SQLAlchemy ORM

## 📊 Viewing Contact Submissions

- **Development**: Visit `/admin/submissions` to see all contact form submissions
- **Production**: Implement proper authentication for admin access

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support, email support@redstore.com or create an issue in this repository.

## 🙏 Acknowledgments

- Font Awesome for icons
- Google Fonts for typography
- Smartsupp for live chat functionality
- SQLAlchemy for database ORM