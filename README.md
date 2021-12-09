# Instalation

### 1. Make Environment

[How to Make Environment Python](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

### 2. Activate Environment

> env\Scripts\activate

### 3. Install Dependencies

> pip install -r /path/to/requirements.txt

### 4. Buat Database

> Name : ikhsan

### 5. Init Backend

> python manage.py makemigrations

> python manage.py migrate

### 6. Buat Superuser

> python manage.py createsuperuser

# API

### Egg

`localhost:8000/egg/`

`GET`
`POST`
`PUT`
`DELETE`
`localhost:8000/egg/`
##### POST
    REQUEST-------------------------
    curl --location --request POST 'http://localhost:8000/egg/' \
    --form 'total="10"' \
    --form 'good="7"' \
    --form 'not_good="3"'
    
    RESPONSE----------------------------
    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Location: /thing/2
    Content-Length: 35

    {id:2 ,total:10, good:7,not_good:3}
