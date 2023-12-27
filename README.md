# ToDoList

A ToDoList python based web application which works with mongoDB and uses the Flask framework.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alexhalcazar/To_Do_List.git
cd ToDoList
```

## Dependencies 

This project relies on the following dependencies:

- [Flask](https://palletsprojects.com/p/flask/): A web framework for Python.
- [pymongo](https://pymongo.readthedocs.io/): The official MongoDB driver for Python.
- [python-dotenv](https://pypi.org/project/python-dotenv/)

2. Install Dependencies

Make sure you have Python and pip installed on your system.

```bash
pip3 install -r requirements.txt
```

3. Create a MongoDB Atlas Account:

+ Users need to create their own MongoDB Atlas account if they don't have one. They can sign up for a free account on the [MongoDB Atlas website](https://www.mongodb.com)

4. Set Up a Cluster:

+ After creating an account, users need to set up a MongoDB Atlas cluster. This involves configuring the cluste's location, cluster tier, and other settings.

5. Create a Database User:

+ Users should create a database user with appropriate privileges for their application. The credentials (username and password) of this user will be part of the MongoDB Atlas connection string.

6. Get the connection String:

+ Once the cluster is set up and the database user is created, users can obtain the MongoDB Atlas connection string. This string includes information about the cluster, authentication credentials, and other details.

7. Set Up Environment Variable Locally:

+ Users should set up their own environment variable locally on their machines to store the MongoDB Atlas connection string. This can be done by copying the **'.env.template'** and customizing with their MongoDB Atlas credentials:

Example **'.env'**



Users would replace **username** **<password>** and **<dbname>** with their own MongoDB Atlas credentials.

**Note:** Be sure to add your newly created **'.env'** to your **'.gitignore'** file.

## Usage

8. Once Flask is installed, you can run the application using the provided **'server.py'** file:

```bash
python3 server.py
```
## Acces the ToDoList endpoints

Currently this ToDoList web application has two endpoints. 

### Search

[A search endpoint used to search created tasks.](http://localhost:4000/search/) 

### Create

[A create endpoint used to create a new task](http://localhost:4000/create/)

## Reporting Issues

If you encounter any issues or have suggestions for improvement, please [create an issue](https://github.com/alexhalcazar/To_Do_List/issues)

## Authors

Alex Alcazar
