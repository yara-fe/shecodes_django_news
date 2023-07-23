# {{ Yara Fe Tuguinay }} - She Codes News Project

## About This Project
This project is a news website created for the SheCodes 2023 program using Django framework.

This website has the following features:
- Visitors can visit the home page and view the latest stories. 
- Visitors can also see all the stories available and filter the stories by author using the search query.
- Navigation bar is available at the top-right corner. This will display different options depending if user is logged in or not.
- If a user is not logged in, they can either log in or create an account.
- If a user is logged in, the following features will be enabled:
    - create, edit or delete stories
    - view and edit user profile
    - log out

## How To Run This Code
{{Give a quick step-by-step guide on how to download and run your codebase.It's ok to assume the reader is another developer here, so don't feel like youhave to explain what a virtual environment is, etc.Give directions like "clone the repo to your local machine", "create a virtualenvironment", "migrate the database", etc.
When you need to specify terminal commands, you can surround them withbackticks, like so: `python manage.py runserver`. This formats them ascode in the markdown document. (The backtick key is to the left of thenumber 1 at the top of your keyboard.)}}

Step | Action | Command
| :--- | :--- | :--- 
| 1 | Clone repo to your local machine - run git bash from local directory and clone repo via terminal| `git clone https://github.com/yara-fe/shecodes_django_news.git`
| 2 | Check pip version | `python -m pip --version`
| 3 | If not available, run command to install |`python -m ensurepip --upgrade`
| 4 | Create and activate virtual environment to run Django app |`python -m venv venv` <br> `. venv/Scripts/activate`
| 5 | Install project requirements |`python -m pip install -r requirements.txt`
| 6 | Check installation successful |`python -m pip freeze`
| 7 | Launch VS code <br> Note: VS code will open. Leave as is and return to GitBash terminal to continue |`code .`
| 8 | Make initial migrations in project directory | `cd she_codes_news` <br> `python manage.py migrate`
| 9 | Run local web server | `python manage.py runserver`
| 10 | Launch news website | http://127.0.0.1:8000/news 

## Project Features

- [X] Home page and Order stories by date ![Order by date](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-57-24.png)

- [x] "New story" Form with Story Images ![New Story](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-57-35.png)

- [x] Log-in ![ {{ Login }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-24_0-12-38.png)

- [x] Logout button in Nav bar when user is logged in ![ {{ Logout }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-57-24.png)
      
- [x] "Account view" page ![ {{ Profile }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-58-32.png)

- [x] "Create Account" page ![ {{ Create Account }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-24_0-15-44.png)

- [x] View stories by author ![ {{ Author }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-58-15.png)

- [x] "Create Story" functionality only available when user is logged in
![ {{ User logged in - edit story }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-58-48.png)

![ {{ User logged out - no edit story }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-59-21.png)

## Additional Features:

- [x] Add the ability to update and delete stories (only when logged in).
- [x] Additionally, the publish date is now automatically set to the date the story is created or edited, rather than a manual input.
![ {{ Update and Delete Story }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-58-55.png)
![ {{ Confirm delete }} ](https://github.com/yara-fe/shecodes_django_news/blob/main/images/2023-07-23_23-59-05.png)
