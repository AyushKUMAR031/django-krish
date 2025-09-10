# django-krish

This is a multi-step user registration form built with Django.

## How to run the application

1.  **Clone the repository:**

    ```
    git clone <repository-url>
    ```

2.  **Create a virtual environment and activate it:**

    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the dependencies:**

    ```
    pip install -r requirements.txt
    ```

4.  **Run the migrations:**

    ```
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```
    python manage.py runserver
    ```

6.  **Open your browser and go to:**

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## How to test the registration form

1.  **Go to the registration page:**

    [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)

2.  **Fill out the form in three steps:**

    *   **Step 1: Basic Info** (username, email, phone)
    *   **Step 2: Address & Password**
    *   **Step 3: Profile Photo & Terms**

3.  **After completing the form, you will be redirected to a success page.**