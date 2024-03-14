# Hospital
Add story here:

The <b><i>conceptual schema</i></b> and the <b><i>entity/relationship schema</i></b> can be found in the <b><i>Hospital Diagram.drawio</b></i> file and can be opened with [draw.io](https://app.diagrams.net/).    

<img src="https://github.com/Matoka26/Hospital-/assets/106425405/5bdb02d0-7dda-4004-9a47-f376dfa77371" length=700 width=1000 >

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

Read the names of the possible URL suffixes from the <b><i>backend/drf_ospital/urls.py</b></i> file.  

  ## Great sources of inspiration:
  - [Django REST framework](https://www.django-rest-framework.org/) documentation
  - [bobby-didcoding](https://github.com/bobby-didcoding/drf_course) 's course
  - [CodingEntrepreneurs](https://www.youtube.com/watch?v=c708Nf0cHrs&t=2815s&ab_channel=CodingEntrepreneurs) 's course
      
### Other relevant links:
  - [Codemy.com](https://youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&si=rTx0mO6DSjuhChtW) 's playlist
  - [admin panel](https://www.youtube.com/watch?v=qP1PMri9oq4&ab_channel=GeeksCoders)
  - [hash password](https://www.youtube.com/watch?v=PSY6bI5fU9Y&ab_channel=FeelFreeToCode)
  - [table relationships](https://www.youtube.com/watch?v=QB9gGEwxxM4&ab_channel=PrettyPrinted)
  - [views](https://www.youtube.com/watch?v=DiSoVShaOLI&list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV&index=3&ab_channel=CodingWithMitch)

