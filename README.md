VeggieHub - Online Vegetable Marketing Platform
Project Description

VeggieHub is a Django-based web application designed to connect vegetable suppliers and consumers. The platform allows suppliers to post their products, including images, descriptions, and prices, while consumers can browse, search, and filter the available products. The system facilitates seamless interaction between suppliers and customers, offering a user-friendly interface and efficient product management features.
Features

    User Registration and Login: Consumers and suppliers can create accounts using their email addresses.
    Supplier Profile Management: Suppliers can update their profile details and manage their product listings.
    Product Posting: Suppliers can add, edit, and delete vegetable product listings, including images, prices, and descriptions.
    Product Browsing and Search: Users can browse the products and search by name, category, and other filters.
    Responsive Design: The interface is fully responsive and adapts to different screen sizes (mobile, tablet, desktop).
    Admin Dashboard: Admin users have access to manage users, suppliers, and products.

Technologies Used

    Backend: Python, Django Framework
    Frontend: HTML5, CSS3, JavaScript, Bootstrap
    Database: SQLite (can be replaced with MySQL or PostgreSQL)
    Version Control: Git
    Web Server: Django's built-in development server for local testing

Installation Instructions
1. Prerequisites

Before you begin, ensure you have the following installed:

    Python 3.x
    Git
    Django (can be installed via pip)
    Virtual environment (recommended)

2. Clone the Repository

Clone the repository from GitHub to your local machine:

bash

git clone https://github.com/yourusername/veggiehub.git
cd veggiehub

3. Create and Activate a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies

Install the required dependencies using pip:

bash

pip install -r requirements.txt

5. Apply Migrations

Before running the project, ensure that you apply the database migrations:

bash

python manage.py makemigrations
python manage.py migrate

6. Create a Superuser (Admin Account)

To access the Django admin dashboard, create a superuser account:

bash

python manage.py createsuperuser

Follow the prompts to set up your admin credentials.
7. Run the Development Server

Start the Django development server to view the application locally:

bash

python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser to access VeggieHub.
Usage
For Suppliers:

    Register and log in as a supplier.
    Update your profile with necessary details.
    Post your vegetable products, adding images, descriptions, and prices.
    Manage your products (edit or delete as needed).

For Consumers:

    Browse or search for vegetables on the platform.
    Contact the supplier for purchasing details.

Admin Access:

    Log in using the admin credentials.
    Manage users, suppliers, and products through the Django admin dashboard at http://127.0.0.1:8000/admin.
