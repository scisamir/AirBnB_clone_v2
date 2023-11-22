# AirBnB Clone
	0x00. AirBnB clone - The console
 ## This project aims to create a clone of the AirBnB website

 ## First Step:

 ### Objects (classes), serialization and deserialization, file storage, and unittests:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### Command Intepreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Usage

### starting the command intepreter
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

### create
```
(hbnb) create BaseModel
6f4de530-9179-470b-8ea8-fa2e121800d5
(hbnb) create User
20061fa2-e05b-449d-9b3a-0929dce66afc
(hbnb)
```

### show
```
(hbnb) show User 20061fa2-e05b-449d-9b3a-0929dce66afc
[User] (20061fa2-e05b-449d-9b3a-0929dce66afc) {'id': '20061fa2-e05b-449d-9b3a-0929dce66afc', 'created_at': datetime.datetime(2023, 10, 17, 7, 12, 59, 639440), 'updated_at': datetime.datetime(2023, 10, 17, 7, 12, 59, 643343)}
(hbnb)
```

### destroy
```
(hbnb) destroy User 20061fa2-e05b-449d-9b3a-0929dce66afc
(hbnb) show User 20061fa2-e05b-449d-9b3a-0929dce66afc
** no instance found **
(hbnb)
```

### all
```
(hbnb) create BaseModel
56792a12-6173-4b4f-b178-f52b9a9e413e
(hbnb) all
["[BaseModel] (56792a12-6173-4b4f-b178-f52b9a9e413e) {'id': '56792a12-6173-4b4f-b178-f52b9a9e413e', 'created_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 124398), 'updated_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 126686)}"]
(hbnb) create User
949e96ae-d3e9-4716-aba5-49094f8b6377
(hbnb) all
["[BaseModel] (56792a12-6173-4b4f-b178-f52b9a9e413e) {'id': '56792a12-6173-4b4f-b178-f52b9a9e413e', 'created_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 124398), 'updated_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 126686)}", "[User] (949e96ae-d3e9-4716-aba5-49094f8b6377) {'id': '949e96ae-d3e9-4716-aba5-49094f8b6377', 'created_at': datetime.datetime(2023, 10, 17, 7, 18, 34, 946231), 'updated_at': datetime.datetime(2023, 10, 17, 7, 18, 34, 948960)}"]
(hbnb)
```

### update
```
(hbnb) show BaseModel 56792a12-6173-4b4f-b178-f52b9a9e413e
[BaseModel] (56792a12-6173-4b4f-b178-f52b9a9e413e) {'id': '56792a12-6173-4b4f-b178-f52b9a9e413e', 'created_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 124398), 'updated_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 126686)}
(hbnb) update BaseModel 56792a12-6173-4b4f-b178-f52b9a9e413e first_name "My name"
(hbnb) show BaseModel 56792a12-6173-4b4f-b178-f52b9a9e413e
[BaseModel] (56792a12-6173-4b4f-b178-f52b9a9e413e) {'id': '56792a12-6173-4b4f-b178-f52b9a9e413e', 'created_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 124398), 'updated_at': datetime.datetime(2023, 10, 17, 7, 18, 26, 126686), 'first_name': 'My name'}
(hbnb)
```

### quit
```
(hbnb)
(hbnb) quit
$
```

## Other variants of the commands above are:
- `<class name>.all()` - to retrieve all instances of a class
- `<class name>.count()` - to retrieve the number of instances of a class
- `<class name>.show(<id>)` - to retrieve an instance based on its ID
- `<class name>.destroy(<id>)` - to destroy an instance based on his ID
- `<class name>.update(<id>, <attribute name>, <attribute value>)` - to update an instance based on his ID


### AUTHORS
* [Samir Idris](https://linktr.ee/scisamir)
* [Louis Agbedor](louisdzidzor22@gmail.com)
