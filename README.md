# Python test assessment by DevelopsToday

Simple MVP. It will have a list of news with functionality to upvote and comment on them. Similar platform to HackerNews.

## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count

## **Technical Requirements**

- Code should be written with Python 3
- REST API should be Django and Django REST Framework based
- API should be well documented with Postman collection. Make sure to use [Postman environments and variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/#understanding-variables-and-environments), so you can switch between local API and deployed version. Add Postman collection link to the README
- API has to run as a Docker container. API + Postgres should be launched with docker-compose
- Code should be formatted with [Black](https://github.com/psf/black)
- Necessary to make sure that Flake8 linter passes. Would be great to have typing with [pyright](https://github.com/microsoft/pyright) as well
- The project should have clear README with steps to run it
- The code should be clean, passing linter checks and simple to understand. Code quality matters a lot
- Deploy API for testing to [Heroku](https://www.heroku.com/) or [DevSpace](https://devspace.cloud/). Add deployment link to the README

## **Brief description**

The projects works on PostgreSQL using psycopg2 library at Python site. So be sure you have installed Postgre on your local machine.

## **Movements**

### **Steps to start on**

You can move right through the steps to start the project on your computer, or just use Docker container (next chapter).

Make sure you have venv at your machine or just 
pip install virtualenv

Choose local place to put the project (cd ....) and follow next steps:    
Python 2:    
`virtualenv env`    

Python 3:    
`python -m venv yourvenv`    
or    
`python3 -m venv yourvenv`    

Download the project from github    
`git pull https://github.com/IefremovRoman/drf_test_developstoday.git`

Install all depencies:    
`pip install -r requirements.txt`    

Start project:    
`python manage.py runserver`

(after that you can follow the link you can see in the terminal)

DB migration:    
`python manage.py migrate`

To use all function, you can check Postman documentation using prepared Postman collection.

## **Postman**
[Postman collection](https://www.postman.com/supply-cosmonaut-28000462/workspace/developstoday-postman-collection/request/17927909-edac785d-fca3-4cac-8910-597433eb56fd)    
[Postman documentation](https://documenter.getpostman.com/view/17927909/UV5f7DhZ)

## **Deploy**
[Deploy on Heroku link](https://still-sea-84215.herokuapp.com/)
