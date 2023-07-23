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

## Database Schema![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features

- [X] Order stories by date![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Styled "new story" form![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Story images![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Log-in/log-out![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Account view" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Account" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] View stories by author![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Story" functionality only available when user is logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:

- [ ] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
