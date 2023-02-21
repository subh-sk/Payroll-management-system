# Start
## We need some software for setup our local database. 
1. We need to download xammp application and install it on your system
2. Open the xammp application and start Apache and MYSQL service
3. Go to your phppmyadmin/localhost website (http://localhost/phpmyadmin) 
4. Click on new and create a database named = payroll  [Note:-the database name should be same as here mentioned](http://localhost/phpmyadmin/index.php?route=/server/databases)
5. Click on import option on top of menu bar (http://localhost/phpmyadmin/index.php?route=/server/import)
6. Select your payroll.sql file and import it

## Install requirements.txt
1. Open cmd or any terminal
2. Locate your *requirements.txt* file using cd command  [cd file_location_path]
3. Run the command = `pip install -r requirements.txt`

You setup is done now open main.py, run it and open http://127.0.0.1:5000
