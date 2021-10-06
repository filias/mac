# mac

To make the site work basically you need to do this:

1. Clone this repository or pull the latest master: 
   1. `git pull origin master`
2. Install mysql server for your operating system. In ubuntu 20.04:
    1. `sudo apt install mysql-server`
3. In the mysql shell: `mysql -u root -p`
    1. Create a database and a user:
        1. `CREATE USER <username> IDENTIFIED BY '<password>';`
        2. `CREATE DATABASE mac;`
        3. `GRANT ALL PRIVILEGES ON mac.* TO <username>;`
        4. `exit;`
        5. Load the database dump into the new table: `mysql -u <username> -p mac < mac_backup.sql` (if you do not have the database dump please ask in the slack channel)
4. Install Poetry. [Installation](https://python-poetry.org/docs/#installation) and [update](https://python-poetry.org/docs/#updating-poetry) instructions are available on the project's [documentation](https://python-poetry.org/docs/).
5. Install the project's dependencies with the command: `poetry install`.
    1. On ubuntu 20.04 I had to remove the system's virtualenv package for this to work:
        ```sudo apt remove python3-virtualenv```
6. Start a shell in the with project's virtualenv activated with the command: `poetry shell`.
7. Create a .env file with this:
    ```
    DB_USER=<dbuser>
    DB_PASSWORD=<dbpass>
    AWS_STORAGE_BUCKET_NAME=mac-media
    ```
8. Load these variables into your venv, in linux shell this can be done like this: 
   1. `set -a && source .env && set +a`
9. Run the migrations:
   1. `./manage.py migrate`
10. Create a user for you to use the django admin: 
    1. `./manage.py createsuperuser` 
11. Run the django development server: 
    1. `./manage.py runserver`. 
    2. For Windows you should try `python manage.py runserver` instead.
12. You can see the django admin site in:
    1. `localhost:8000/admin` 
    2. and the website at `localhost:8000` 

It is possible that, depending on your OS, you need to install some dependencies. On ubuntu 20.04 I had to install or do the following:
- `sudo apt install default-libmysqlclient-dev libmysqlclient-dev libssl-dev`
and do this:
- `sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -P /usr/include/mysql/`

To deploy the website:

1. `poetry update` to update the lock file
2. Regenerate the requirements.txt file when changing dependencies: 
   1. `poetry export -o requirements.txt`
3. `git commit`
4. `git push origin master`
5. In pythonanywhere virtualenv shell:
    1. `git pull origin master`
    1. `pip install -r requirements.txt`
    1. Apply migration if needed: `./manage.py migrate`
    1. Collect static files: `./manage.py collectstatic`
    1. Reload the application
