# mac

To make the site work basically you need to do this:

1. Clone this repository or pull the latest master: `git pull origin master`
1. Install mysql server for your operating system. In ubuntu 20.04:
    1. `sudo apt install mysql-server`
1. In the mysql shell: `mysql -u root -p`
    1. Create a database and a user:
        1. `CREATE USER <username> IDENTIFIED BY '<password>';`
        1. `CREATE DATABASE mac;`
        1. `GRANT ALL PRIVILEGES ON mac.* TO <username>;`
1.Load the database dump into the new table: `mysql -u <username> -p mac < mac_backup.sql` (if you do not have the database dump please ask in the slack channel)
1. Install Poetry. [Installation](https://python-poetry.org/docs/#installation) and [update](https://python-poetry.org/docs/#updating-poetry) instructions are available on the project's [documentation](https://python-poetry.org/docs/).
1. Install the project's dependencies with the command: `poetry install`.
    1. On ubuntu 20.04 I had to remove the system's virtualenv package for this to work:
        ```sudo apt remove python3-virtualenv```
1. Extract the media files zip into a `media` directory in the root of the project (if you do not have the media zip please ask in the slack channel)
1. Start a shell in the with project's virtualenv activated with the command: `poetry shell`.
1. Create a .env file with this:
    ```
    DB_USER=<dbuser>
    DB_PASSWORD=<dbpass>
    MEDIA_URL=http://127.0.0.1/media/
    ```
1. Load these variables into your venv, in linux shell this can be done like this: `set -a && source .env && set +a`
1. Run the migrations: `./manage.py migrate`
1. Run the django development server: `./manage.py runserver`

It is possible that, depending on your OS, you need to install some dependencies. On ubuntu 20.04 I had to install or do the following:
- `sudo apt install default-libmysqlclient-dev python2.7-dev libmysqlclient-dev libssl-dev`
and do this:
- `sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -P /usr/include/mysql/`

To deploy the website:

1. `poetry update` to update the lock file
1. Regenerate the requirements.txt file when changing dependencies: `poetry export -o requirements.txt`
1. `git commit`
1. `git push origin master`
1. In pythonanywhere shell:
    1. `git pull origin master`
    1. `pip install -r requirements.txt`
    1. Apply migration if needed: `./manage.py migrate`
    1. Collect static files: `./manage.py collectstatic`
    1. Reload the application