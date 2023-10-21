# Infinite scroll example with Django + htmx

This is a simple example of infinite scroll with Django and htmx. It also uses the [django-htmx](https://django-htmx.readthedocs.io/en/latest/) package.


## Setup

```console
git clone https://github.com/franciscobmacedo/infinite-scroll-django-htmx
cd infinite-scroll-django-htmx
poetry install
poetry shell
```

## Load fake data (optional)

There's only one relevant model in `core/models.py`, called `Product`. In order to load some fake data, run the following command:

```console
python manage.py load-fixtures.py
```

## Run
```console
python manage.py runserver
```

You should be able to go to http://localhost:8000 and as you scroll down, new products will be loaded automatically.


