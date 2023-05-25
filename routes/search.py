from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from db.index import get_database
from bson import json_util, ObjectId
# was having attempted relative import beyond top-level package

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/')

def renderHTML():
    return render_template('search.html')


@search_blueprint.route('/', methods=['POST'])

def findTask():
    try:
        # get the database
        db = get_database()

        # access the "List" collection
        collection = db['List']

        title = request.form['title']

        if title == '':
            tasks = list(collection.find({}))
            render_template('search_results.html')
        else:
            tasks = list(collection.find({'title': title}))

        if tasks:
            # in Flask's render_template function, any keyword arguments provided after
            # the template name are considered variables that can be accessed within the template
            return render_template('search_results.html', tasks=tasks)
        else:
            flash('No tasks found')
            return redirect(url_for('search.renderHTML'))
        

    except Exception as error:
        print(error)

@search_blueprint.route('/task/<task_id>', methods=['POST'])
def updateTask(task_id):
    try:
        # get the database
        db = get_database()

        # access the "List" collection
        collection = db['List']

        completed = request.form.get('completed')

        collection.update_one({'_id': ObjectId(task_id)}, 
                              {'$set': {'completed': bool(completed)}})

        flash('Task updated successfully!')
        
        return redirect(url_for('search.renderHTML'))

    except Exception as error:
        flash('An error occured')
        print(error)
        return redirect(url_for('search.renderHTML'))