# Hospital
### Current root directoy
```
    hospital-\  <-- Root directory
        backend\
            docker\
            ...
             >requirements.txt
        >.gitignore
        >docker-compose.yml
        >env.template
        >Hospital Diagram.drawio
        >README.md
        >server.py
```

## 1. Installing dependencies  

Open a terminal to create the <b>virtual environment</b> called <b><i>venv</i></b>.

```
python -m venv venv
```

Activate the <b>virtual environment</b>.
```
# On Windows
venv\Scripts\activate

# On UNIX
source venv/bin/activate
```

Install dependencies.
```
pip install -r backend/requirements.txt
```

Additionally (not mandatory) upgrade pip.
```
python.exe -m pip install --upgrade pip
```

Create a new <b><i>env</i></b> file to store informations specific to our working environment.
```
# On Windows
copy env.template .env

# On UNIX
cp env.template .env
```

## 2. Run Server


### Current root directoy
```
    hospital-\  <-- Root directory
        backend\
            core\
            ...
             >requirements.txt
        venv\
        >.env
        >.gitignore
        >docker-compose.yml
        >env.template
        >Hospital Diagram.drawio
        >README.md
        >server.py
```

Change directory to the backend.
```
cd backend
```

Migrate (the migration already exist in backend/core/migrations/0001_initial.py).
```
python manage.py migrate  
```

Run server
```
python manage.py runserver
```

CTRL + Clink on the URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

> **NOTE:**  
> After changing anything regarding the structure of the models run the following commands to make a new migration and migrate
>```
>python manage.py makemigrations
>python manage.py migrate  
>```


## 3. Admin Panel
To creat an admin run
```
python manage.py createsuperuser
```
On the following prompts provide:
- Username (otherwise it will be auto-complited with the the name of the current User of the machine)
- Email address
- Password
- Password (again)


To access the admin panel add <b><i>/admin/</i></b> to the end of the URL.  

Login with the <b>Username</b> and <b>Password</b>  
  
You now have access to the <b>admin panel</b> and can operate <b>CRUD</b> operations on the models of the app with more ease.

## 4. URLs
You can access a view for each model by adding <b><i>/core/modelName/</b></i> to the end of the URL.  
On this interface is exposed a field where you can 
- <b><i>POST</b></i> new data to the model's table
- <b><i>GET</b></i> existing data (click the top right button)  
  
To use the <b><i>GET(by id), PUT, PATCH, DELETE</b></i> endpoints you must add the <b><i>/id</b></i> at the end of the URL.   
(Also use an external app such as <b>[Postman](https://www.postman.com/)</b> to process the requests.)  
  
  Example:
```
http://127.0.0.1:8000/core/user/a3c9f5f1-2b55-4ec8-a312-7f85f506c9f2
```

Read the names of the possible URL suffixes from the <b><i>backend/df_ospital/urls.py</b></i> file.