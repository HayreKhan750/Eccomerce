#!/usr/bin/env python3
"""
Database setup script for RedStore E-commerce
Run this script to create the database and tables
"""

import os
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_database():
    """Create the database if it doesn't exist"""
    
    # Get database configuration from environment
    db_url = os.getenv('DATABASE_URL', 'mysql+pymysql://username:password@localhost/redstore_db')
    
    # Parse the database URL
    # Format: mysql+pymysql://username:password@host/database
    if db_url.startswith('mysql+pymysql://'):
        db_url = db_url.replace('mysql+pymysql://', '')
    
    # Split into parts
    credentials_host, database = db_url.split('/', 1)
    username_password, host = credentials_host.split('@')
    username, password = username_password.split(':')
    
    try:
        # Connect to MySQL server (without specifying database)
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print(f"✅ Database '{database}' created successfully!")
        
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    return True

def create_tables():
    """Create tables using Flask-SQLAlchemy"""
    try:
        from server import server, create_tables
        
        with server.app_context():
            create_tables()
            print("✅ Tables created successfully!")
            
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Setting up RedStore Database...")
    
    # Step 1: Create database
    if create_database():
        print("📊 Database created/verified successfully!")
    else:
        print("❌ Failed to create database")
        exit(1)
    
    # Step 2: Create tables
    if create_tables():
        print("📋 Tables created successfully!")
    else:
        print("❌ Failed to create tables")
        exit(1)
    
    print("🎉 Database setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Update your .env file with correct database credentials")
    print("2. Run 'python server.py' to start the application")
    print("3. Test the contact form at /contact.html")
    print("4. View submissions at /admin/submissions") 