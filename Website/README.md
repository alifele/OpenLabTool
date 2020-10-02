Here is how you can setup the website on your local machine:

create the virtual env:
```bash
python3 -m venv webdev

```

activate the vnev:
```bash
source webdev/bin/activate

```

install requitements:
```bash
pip install -r requirements.txt

```


make migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

run the dev server:
```bash
python3 manage.py runserver 

```

Now you can access the website with: localhost:8000



