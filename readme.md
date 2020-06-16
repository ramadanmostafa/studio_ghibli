## Python Back-end Assignment: Movie List
Studio Ghibli is a Japanese movie company. They offer a REST API where one can query
information about movies and people (characters).

The task is to write a Python application which serves a page on localhost:8000/movies/. This
page should contain a plain list of all movies from the Ghibli API. For each movie the people that
appear in it should be listed.

Do not use the people field on the /films endpoint, since it’s broken. There is a list field called
films on the /people endpoint which you can use to get the relationship between movies and
the people appearing in them.

You don’t have to worry about the styling of that page.

Since accessing the API is a time-intensive operation, it should not happen on every page load.

But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so
make sure that the information on the page is not older than 1 minute when the page is loaded.

The code should be submitted in a clean and refactored state. Please format the code
according to the PEP8 conventions.

Don’t forget to test your code. Your tests don’t have to be complete, but you should describe
how you would extend them if you had the time.

If you have to skip some important work due to time limitations, feel free to add a short
description of what you would improve and how if you had the time for it.

# How to Run
```
cd studio_ghibli
cp .env.dist .env
cd ..
docker-compose build
docker-compose up
docker-compose run web python manage.py test --keepdb
```
# How it works
the task_trigger calls ```python manage.py sync_movies_data``` command once when created which will trigger
 a celery task that fetches the data and call itself again after sleeping for 60 seconds.
# How to improve
maybe use celery beat to handle the schedule task