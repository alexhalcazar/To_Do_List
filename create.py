from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.index import get_database
# was having attempted relative import beyond top-level package

# special Python variable that represents the name of the current module. 
# in this case, it refers to the module where the blueprint is defined.
create_blueprint = Blueprint('create', __name__)

@create_blueprint.route('/')

def renderHTML():
    return render_template('index.html')

# decorator used to associate the createTask function with the specified route
# handles form submissions via a POST request
@create_blueprint.route('/', methods=['POST'])

def createTask():
    # get the database
    db = get_database()

     # access the "List" collection
    collection = db['List']

    # to access form data (data transmitted in a POST or PUT request) you can use the form attribute
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    due_date = request.form['dueDate']

    # create a document (data) to be inserted
    task = {
        'title': title,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }

    # insert the document into the collection
    result = collection.insert_one(task)

    # print the inserted document's ID
    print('Inserted document ID:', result.inserted_id)

    # Set a flash message to inform the user about the successful task creation
    message = 'Task created successfully!'

    # Redirect the user back to the form page with the flash message
    # url_for function is a Flask helper function that generates URLs dynamically 
    # by using the name of the view function or endpoint rather than hardcoding the URL path
    flash(message)
    return redirect(url_for('create.renderHTML'))