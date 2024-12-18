# Assignment(CRUD Application)

## Project Description
This project is a Django-based web application that demonstrates basic CRUD (Create, Read, Update, Delete) operations. The application allows users to manage a list of items through a simple, user-friendly interface. It is designed to showcase Django's core functionalities, including models, views, templates, forms, and URL routing.

---

## Features
- **Add Items:** Create new items with a name and optional description.
- **View Items:** Display a list of all items and view details for a specific item.
- **Update Items:** Edit existing items using a form.
- **Delete Items:** Remove items with a confirmation step.
- **Responsive Design:** Styled using Bootstrap to ensure the application is visually appealing and user-friendly.

---

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django database)
- **Version Control:** Git (GitHub for repository hosting)

---

## Installation Instructions
Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/pramo22/Assignment>
   cd Assignment

## Project set-up:
1. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Create a Django Project: Run the following command to create project**
   ```bash
   django-admin startproject Assignment

3. **Create an App: Inside the project directory, create a new app for managing items:**
   ```bash
   py manage.py startapp project
   
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Development Server**
   ```bash
   python manage.py runserver
   
5. **Access the Application: Open your web browser and navigate to http://127.0.0.1:8000/.**

## Explanation:
1. **Item Details:**
   - Displays the item's name, description, creation date, and last updated date in a table format.
   - Dynamically pulls data from the item object passed to the template.
2. **Action Buttons:**
   - Update: Navigates to the item update page.
   - Delete: Navigates to the item delete confirmation page.
   - Back To Home: Returns to the main item list view.
3. **Styling:**
   - Uses a Bootstrap table (table table-bordered) to make the details clear and organized.
   - Adds buttons with relevant Bootstrap classes for consistent UI styling.
  
## Documentation:

**Models**

| Field Name    | Data Type     | Description            | Required/Optional   |
|:------------: |:------------: |:---------------------: |:------------------: |
| name          | CharField     | Name of the item       | Required            |
| description   | TextField     | Description of the item| Optional            |
| created_at    | DateTimeField |Timestamp when the item was created                        | Auto-generated            |
| updated_at    | DateTimeField |Timestamp when the item was last updated                        | Auto-generated       |




**Views**

| View Name     |  URL Pattern              | Description                            |  HTTP Method                   |
|:-------------:| :------------------------:| :-------------------------------------:|:------------------------------:|
| home          | '/'                       | Displays a list of all items           | GET                            |
| create        | '/create_data/'           | Provides a form to create a new item   | GET, POST                      |
| view          | '/view/<int:pk>/'         | Display details of single item         | GET                            |
| update        | '/update/<int:pk>/'       | Provides a form to edit existing item  | GET, POST                      |
| delete        | '/delete_data/<int:pk>/'  | Confirmation page to delete a single item | GET, POST                   |

Open the application in your browser at http://127.0.0.1:8000/home/.

## Assignment Documentation
![em_webdev_assignment_dec2024](https://github.com/pramo22/Assignment/blob/main/em_webdev_assignment_dec2024.doc)
