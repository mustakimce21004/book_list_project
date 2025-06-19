# Book List Project

A simple Django-based CRUD application for managing books with user authentication and responsive design.

---

## Features

- ✅ User authentication with login and logout functionality.
- ✅ Responsive and clean UI built with Bootstrap.
- ✅ Display book listings including author images.

---

## Current Limitations

- ❌ Role-based access control is **not yet implemented**:
  - Currently, all authenticated users have full access to add, edit, and delete books.
  - The plan is to restrict these actions so that only admin users can modify book data.
- ❌ PDF export functionality for book listings is still under development.

---

## Getting Started

1. Clone the repository and install dependencies.
2. Run database migrations:

   ```bash
   python manage.py migrate
3.Start the development server:
  python manage.py runserver
4.Access the app at http://127.0.0.1:8000/ and log in.

##Planned Improvements##
Implement role-based permissions:

Admins will be able to add, edit, and delete books.

Regular users will have view-only access.

Add PDF export feature for book lists.

Enhance UI and add form validations

##Contributions##
Contributions, feedback, and suggestions are warmly welcome! Feel free to open issues or submit pull requests.
