Installation

Clone the repository:

git clone https://github.com/bitunishant/jansurajVolunteers.git

cd yourproject

Create a virtual environment and activate it:

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:

python manage.py runserver