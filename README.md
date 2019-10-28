# smartcowtask

Requirements
- Python3
- Django frame work
- Dependency modules
  - django-middleware-global-request (To acces Logged user in Model)
  - front end developed with bootstrap and Jquery
- Data base SQlite

Modules Include and process flow.
1. Signup form wih username, password and Project name
    - User specific Project directory will create and redirect to login
2. Login, Logout Inherited from Django framework
3. Upload : can able to upload multiple images at a time with ajax file upload functionality
            - user need to click any one of the image to annotate
4. Annotate : can able to annotate multiple objects in image, Once done redirecting to Myannotate
5. MyAnnotate : will have particular user Annotated images, user can able to check what objects he annotated in that image
6. Download CSV : User can able to export annotated image coordinates to CSV file

DEMO : https://youtu.be/ze0jXX4JEj4
