AirBnB Clone
This project is an implementation of the AirBnB clone, developed as part of the training program at Holberton School.

Description
The AirBnB Clone project is a recreation of the AirBnB website, allowing users to search and book accommodation, and owners to manage their listings. This implementation is based on a modular and object-oriented approach, using the Python programming language and a relational database.

The main goal of this project is to develop a deep understanding of object-oriented programming, database manipulation, and user interface implementation through a command line interface (CLI).

Use
The project can be used through a command line interface. Once you have started the application, you can run different commands to interact with the database and perform actions such as creating users, managing accommodations, making reservations, etc.

Here are some sample commands available:

* Create a new user:

(hbnb) create User

* List all available accommodation:

(hbnb) all Place

* Make a reservation for a specific accommodation:

(hbnb) reserve <place_id> <user_id>

Project Architecture
The AirBnB Clone project is divided into several modules, each with a specific responsibility:

* models: Contains the classes that represent the domain objects, such as User, Place, Review, etc. These classes map to tables in the relational database.

*engine: Provides an abstraction layer to interact with the database and perform CRUD (Create, Read, Update, Delete) operations on domain objects.

*console: Implements the command line interface (CLI) to interact with the application and perform actions such as creating users, managing accommodations, making reservations, etc.
