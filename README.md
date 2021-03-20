# mac

To make the site work basically you need to do this:

1. Clone this repository or pull the latest master: `git pull origin master`
1. Install mysql server for you operating system. In ubuntu 20.04:
1.1. `sudo apt install mysql-server
1. In the mysql shell: `mysql -u root -p`
1.1 Create a database and a user: 
1.1.1. `CREATE USER <username> IDENTIFIED BY '<password>';`
1.1.1. `CREATE DATABASE mac;`
1.1.1. `GRANT ALL PRIVILEGES ON mac.* TO <username>;`
1.Load the database dump into the new table: `mysql -u <username> -p mac < mac_backup.sql` (if you do not have the database dump please ask in the slack channel)
1. Create a virtualenv with python2.7
1. Activate the virtualenv
1. Install the requirements: `pip install -r requirements.txt`
1. Run the django development server: `./manage.py runserver`

It is possible that, depending on your OS, you need to install some dependencies. On ubuntu 20.04 I had to install or do the following:
- `sudo apt install default-libmysqlclient-dev python2.7-dev libmysqlclient-dev libssl-dev` 
and do this:
- `sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -P /usr/include/mysql/`
