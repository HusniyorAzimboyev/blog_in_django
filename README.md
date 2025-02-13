# Blog Site using Django

A powerful and user-friendly blog site 📝 built with the Django framework 🐍. This project allows users to create, edit, and manage blog posts effortlessly. It is fully customizable, scalable, and follows best practices for web development.

## Features
- 🖊️ Create, edit, and delete blog posts
- 🔎 Search functionality for posts
- 🏷️ Categories and tags for better organization
- 📅 Display posts by date
- 🛡️ User authentication and authorization
- 🎨 Responsive and customizable design

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/HusniyorAzimboyev/blog_in_django.git
   cd blog-site
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

Now, open your browser and go to `http://127.0.0.1:8000/` to start blogging! 🚀

## Technologies Used
- Django 🐍
- HTML, CSS🎨
- SQLite (default, can be changed to PostgreSQL/MySQL) 🗄️

## Contributing
Feel free to fork the project, submit issues, or make pull requests to improve the blog site!

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
