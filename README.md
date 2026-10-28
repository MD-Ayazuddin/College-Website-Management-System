# College Management System

This is a college management website I built with Django. It has separate logins for admin, teachers, and students, so each person only sees what they need.

## Why I built this

A college has a lot to handle every day, like attendance, results, notices, and fees, and it often gets messy when it is done on paper or in many different files. I wanted to learn Django by building something real, so I tried to put all of this in one simple website.

## What it can do

- Separate login for admin, teachers, and students
- Add and manage student and teacher records (name, department, contact details)
- Teachers can take attendance and update it later if needed
- Teachers can upload marks, and students can see their results
- Notice board for posting announcements
- Basic fee records, so you can check who has paid and who hasn't

## Built with

- Python and Django
- SQLite for the database
- HTML, CSS and JavaScript for the front end
- Git, GitHub and VS Code

## How to run it on your computer

1. Clone the project

```bash
git clone https://github.com/mdayazuddin/college-management-system.git
cd college-management-system
```

2. Make a virtual environment and turn it on

On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

On Linux or Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Django

```bash
pip install django
```

If the project has a `requirements.txt` file, you can use `pip install -r requirements.txt` instead.

4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create an admin account

```bash
python manage.py createsuperuser
```

6. Start the server

```bash
python manage.py runserver
```

Now open http://127.0.0.1:8000/ in your browser.

## How to use it

- **Admin:** Go to `/admin` to add students and teachers and manage everything else.
- **Teacher:** Log in to take attendance, add marks, and post notices.
- **Student:** Log in to check your attendance, see your results, and read notices.

## Things I want to add later

- Online fee payment
- Email and SMS alerts
- Download attendance and mark sheets as PDF or Excel

## About me

I'm MD Ayazuddin. If you have any suggestions or find a bug, feel free to contact me.

- GitHub: [@mdayazuddin](https://github.com/mdayazuddin)
- LinkedIn: [aliaslegal0](https://linkedin.com/in/aliaslegal0)
- Email: Aliaslegal0@gmail.com
