# Testing  
This document details how the Movie2Archive application was tested to ensure that complience and good user experiance were achieved and to make the application as accessible to all its users.  
Tests were carried out throughout development in an intergrated way, the tests were carried oyt at each main application development or new feature addition to ensure PEP8 complence within Python was aintained and when developng fromtend elements, HTML, CSS and JS complience was maintained.

## Intergrated testing stages
- #1 - Construct and render flask application to browser:  
PEP8 complience - Python, flask structure files - PASS
- #2 - Database tables User, MediaType and Location models created, postgres database initialised and tables created sucessfully.
PEP8 complience - models.py - PASS
- #3 - Database tables Edition and Movielookup added to database.
PEP8 complience - models.py, routes.py - PASS

## Development bugs
- #1 - MovieLookup table renamed to Movielookup as second capital causes an _ to appear in postgresql database tables view - Fixed
