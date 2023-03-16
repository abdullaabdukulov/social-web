<h1>Social Web Application</h1>
<p>This is a social web application built with Django Framework, utilizing best practices and the latest versions of libraries and packages. It allows users to create profiles, connect with other users, post updates, follow other users, and comment on updates.</p>
<h2>Features</h2>
<ul>
<li>User authentication and authorization using Django's built-in 'auth' module</li>
<li>User profile creation and editing using Django's 'models' and 'forms' modules</li>
<li>User can post updates using Django's 'models' and 'forms' modules</li>
<li>User can follow/unfollow other users using Django's 'models' and 'forms' modules</li>
<li>User can comment on updates using Django's 'models' and 'forms' modules</li>
<li>User can view updates from people they follow using Django's 'views' and 'templates' modules</li>
<li>User can view a list of their followers and people they follow using Django's 'views' and 'templates' modules</li>
</ul>
<h2>Installation</h2>
<ol>
<li>Clone the repository:</li>

```bash
git clone https://github.com/abdullaabdukulov/social-web.git
```

<li>Create and activate a virtual environment:</li>

```bash
python3 -m venv env
source env/bin/activate
```

<li>Install the requirements:</li>

```bash
pip install -r requirements.txt
```

<li>Set up the database:</li>

```bash
python manage.py migrate
```

<li>Create a superuser (admin) account:</li>

```bash
python manage.py createsuperuser
```

<li>Run the server:</li>

```bash
python manage.py runserver
```

</ol>
<h2>Usage</h2>
<p>Open your browser and navigate to http://localhost:8000/. You should see the home page of the application. From there, you can create a new account or log in to an existing one. Once logged in, you will be able to access all the features of the application.</p>
<h2>Contributing</h2>
<p>Contributions are welcome! If you would like to contribute, please open a pull request or issue.</p>
<h2>Credits</h2>
<p>This project was created by Abdulla Abdukulov.</p>
<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="https://en.wikipedia.org/wiki/MIT_License">LICENSE</a> file for more information.</p>
