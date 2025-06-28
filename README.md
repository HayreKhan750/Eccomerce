# RedStore - E-commerce Website

A modern, responsive e-commerce website built with Flask and HTML/CSS. Features a clean design with product listings, shopping cart functionality, and contact forms.

## 🚀 Features

- **Responsive Design**: Mobile-friendly interface
- **Product Catalog**: Browse featured and latest products
- **Shopping Cart**: Add and manage items
- **Contact Form**: Customer support with form submission
- **User Account**: Login and registration pages
- **Live Chat**: Integrated Smartsupp chat widget
- **Google Maps**: Location integration

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

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

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   FLASK_APP=server.py
   FLASK_ENV=development
   SMARTSUPP_KEY=your_smartsupp_key_here
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
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
├── requirements.txt       # Python dependencies
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

## 🔒 Security Notes

- API keys are stored in environment variables
- Database file is excluded from version control
- Form validation is implemented on both client and server side

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