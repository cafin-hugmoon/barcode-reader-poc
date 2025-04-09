# barcode-reader-poc


# To Run
1. Create a virtual environment using python -m venv myenv
2. Activate the virtual environment
3. run pip install -r requirements.txt to install all dependencies (NOTE: pyzbar may require further dependencies to be installed on specific devices)
4. Ensure docker desktop is installed
5. Run "docker-compose up" to spin up the database instance
6. Run python manage.py makemigrations and then python manage.py migrate to update the newly created database with required tables.
7. Run the webserver "python manage.py runserver".


## packages required
asgiref==3.8.1
certifi==2025.1.31
charset-normalizer==3.4.1
Django==4.2.20
idna==3.10
numpy==2.0.2
opencv-python==4.11.0.86
playsound==1.3.0
psycopg2-binary==2.9.9
pydub==0.25.1
pygame==2.6.1
pyzbar==0.1.9
requests==2.32.3
sqlparse==0.5.3
typing_extensions==4.13.1
urllib3==2.3.0