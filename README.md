<p align="center">
<img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="hbnb" width=40% heigth=40% >
</p>

<h1 align="center">AirBnB clone: the project</h1>

<h2>description</h2>
The AirBnB Clone project is a recreation of the AirBnB website, allowing users to search and book accommodation, and owners to manage their listings. This implementation is based on a modular and object-oriented approach, using the Python programming language and a relational database.

The main goal of this project is to develop a deep understanding of object-oriented programming, database manipulation, and user interface implementation through a command line interface (CLI).

<h2>Characteristics</h2>
<ul>
<li> User registration and authentication.</li>
<li>Search and filter of available accommodations.</li>
<li>Creation, editing and deletion of accommodation ads.</li>
<li>Reservation and management of reservations by users.</li>
<li>Rating and user comments on accommodation.</li>
</ul>

<h2>Project Architecture</h2>
<li><Models: Contains the classes that represent the domain objects, such as User, Place, Review, etc. These classes map to tables in the relational database.
</li>
<li>Engine: It provides an abstraction layer for interacting with the database and performing CRUD (Create, Read, Update, Delete) operations on domain objects.</li>
<li>Console: It provides an abstraction layer for interacting with the database and performing CRUD (Create, Read, Update, Delete) operations on domain objects.</li>

<h2>Use</h2>
The project is used through a command line interface (CLI). Once you have started the application, you can run different commands to interact with the database and perform actions related to accommodation and reservation management.

<p>A continuación, se presentan algunos ejemplos de comandos disponibles:</p>

<ul>
  <li>Create a new user:</li>
  <pre><code>(hbnb) create User</code></pre>
  
  <li>List all available accommodation:</li>
  <pre><code>(hbnb) all Place</code></pre>
  
  <li>Make a reservation for a specific accommodation:</li>
  <pre><code>(hbnb) reserve &lt;place_id&gt; &lt;user_id&gt;</code></pre>
</ul>
