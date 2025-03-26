# TeaStore Using Django

TeaStore Django is a robust and user-friendly e-commerce web application built with the Django framework. This application provides an online platform for browsing, purchasing, and managing a variety of teas, complete with user authentication, a product catalog, a shopping cart, and order management features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Product Catalog:** Browse a wide range of teas with detailed descriptions, images, and prices.
- **Admin Panel:** Comprehensive backend for managing inventory, orders, and user data.

## Installation

Follow these steps to set up on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aditya007777/TeaStore_Django.git
   cd TeaStore_Django

2. Create a Virtual Environment

python3 -m venv env
Activate the virtual environment:

On macOS/Linux:

source env/bin/activate

On Windows:

env\Scripts\activate


3) Install Dependencies

pip install -r requirements.txt

4) Apply Database Migrations

python manage.py migrate
python manage.py makemigrations


5) Create a Superuser

python manage.py createsuperuser

Follow the prompts to set up an admin account.

6) Run the Development Server

python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

##Usage

Home Page: Explore featured teas and categories.

Product Details: Click on a tea product to view detailed information, reviews, and pricing.


##Project Structure

A brief overview of the project structure:


├── manage.py
├── requirements.txt
├── tea_store/           # Main Django project directory
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── apps/                # Contains individual Django apps (e.g., products, orders, users)
│   ├── products/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── templates/
│   │   └── ...
│   └── ...
└── static/              # Static files (CSS, JavaScript, images)


## Contributing
Contributions are welcome! If you would like to contribute to TeaStore Django, please follow these steps:

## Fork the Repository

First, Create a New Branch : 

git checkout -b feature/YourFeature
Commit Your Changes
git commit -m "Add new feature: [Your Feature]"

Now, Push to Your Branch : 


git push origin feature/YourFeature

## Open a Pull Request

Please ensure your contributions adhere to the project's coding standards and include tests where appropriate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, feel free to reach out:


## Screenshots :

# Home Page listing different sections : 
<img width="956" alt="image" src="https://github.com/user-attachments/assets/00782ced-450a-44a7-ba1a-8a58c12f6252" />


# Description for each tea showing its' details, implemented using CSS cards : 
<img width="959" alt="image" src="https://github.com/user-attachments/assets/4464ad45-9403-4b36-bce0-995d940a269f" />

# Store Locator, implemented using django forms.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/42683006-06b3-418c-82c5-9fe8cfe0c75e" />







