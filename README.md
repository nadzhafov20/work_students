# Project "Freelance Student"

A freelance platform tailored for students.

## How to Use

0. Before proceeding, configure `settings.py`:

    1. Open `templates/templates/settings.py`.
    2. Find the lines `EMAIL_FROM` and `EMAIL_API_KEY` and replace them with your values.
        - `EMAIL_FROM`: Sender's email address.
        - `EMAIL_API_KEY`: API key obtained from https://app.sendgrid.com/.

1. Start by creating a virtual environment (if not already done). In the terminal, type:

    For Windows
    ```bash
    python -m venv myenv
    ```

    For Linux
    ```bash
    python3 -m venv myenv
    ```

2. Activate the virtual environment:

    For Windows
    ```bash
    .\myenv\Scripts\activate
    ```

    For Linux
    ```bash
    source myenv/bin/activate
    ```

    If you encounter any issues with activating the virtual environment, delete `myenv` and start from step 1.

3. Install all necessary dependencies by executing the command:

    For Windows
    ```bash
    pip install -r requirements.txt
    ```

    For Linux
    ```bash
    pip3 install -r requirements.txt
    ```

4. If the `db.sqlite` database is missing, perform the following steps:

    Go to `templates` where the `manage.py` file is located and enter:

    For Windows
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    For Linux
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

    Then create a superuser:

    For Windows
    ```bash
    python manage.py createsuperuser
    ```

    For Linux
    ```bash
    python3 manage.py createsuperuser
    ```

    Follow the prompts in the terminal to fill in all the required details: username, email, password, and confirm password.

5. Start the local server by running the command:

    For Windows
    ```bash
    python manage.py runserver
    ```

    For Linux
    ```bash
    python3 manage.py runserver
    ```

    A link will appear in the terminal. Click on it to access the application.

    To access the admin panel, add `/admin` at the end of the link.