# Shopify Backend Coding Challenge
This program was created as part of a coding challenge for a **Shopify Software Engineering internship**. 
This program is a simple backend web application that allows users to interact with an inventory database using basic CRUD functionality (Create, Read, Update, Delete).
As an added feature for the coding challenge, users can also download a .CSV file of the database.


# Sample screenshot
![alt text](/screenshot.jpg)


# Technologies used
- Python 3.9
- Django 4.0
- HTML5


# How to run
### Installing Python

1. Navigate to the system's Command Line and check to see if Python is already installed with the below command. If a Python version number appears, 
it is already installed on the system.

<pre><code>python --version</code></pre>

2. If no such version number is given, Python will need to be installed. It can be downloaded [here](https://www.python.org/downloads/).

### Installing Git

1. To download this code repository, Git will need to be installed on the system. The below command can be used to check if Git is already installed. 
If a Git version number appears, it is already installed on the system.

<pre><code>git --version</code></pre>

2. If no such version number is given, Git will need to be installed. It can be downloaded [here](https://git-scm.com/downloads).

### Installing Django

1. In addition to Python, this program will also require Django to be installed. The below command can be used to check if Django is already installed. 
If a Django version number appears, it is already installed on the system.

<pre><code>django-admin --version</code></pre>

2. If no such version number is given, Django will need to be installed. It can be installed with the below command:

<pre><code>pip install django </code></pre>

*Note that the pip function is included with Python 3.4 and above. Previous versions may require an external download*

### Running the program

1. Once Python, Git, and Django are installed, download the code repository via the Command Line:

<pre><code> git clone https://github.com/MikeReeves27/Shopify-backend-coding-challenge.git </code></pre>

2. Navigate to the newly created repository on the system:

<pre><code>cd shopify-backend-coding-challenge </code></pre>

3. To start running the server, use the below command. Note that this server will need to remain active in order for the program to function.

<pre><code>python manage.py runserver</code></pre>

4. The command line will then output a local IP address (http://127.0.0.1:8000/). Either click this or copy and paste it into a web browser.

5. To close the program, exit the web browser and then stop the server by interrupting it with CTRL-C on the command line.

# What the program does
Users are presented with a current list of inventory items. Each item is stored in a SQL database. Users can click 'Add' to add more items to the current list. They can also click
'Edit' to update a current item's values or 'Delete' to permanently remove it from the database.
Users can also click on 'Download' to download all of the items as a .CSV file, which can then be imported into Excel.
