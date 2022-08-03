# Testing  
This document details how the Movie2Archive web application was tested to ensure that complience, a good user experiance was achieved and to make the application as accessible to all its users.  
Tests were carried out throughout development in an intergrated way, the tests were carried out at each main application development stage or when a new feature addition was being developed to ensure PEP8 complence within Python code was maintained and ensure when developng fromtend elements that, HTML, CSS and JS complience was maintained also.

## Table of contents
 
1. [User stories testing from the UX section](#user-stories-testing-from-the-ux-section)  
    2.1 [First time user](#first-time-user)  
    2.2 [Returning user](#returning-user)  
    2.3 [Site owner](#site-owner)  

## User stories testing from UX section  
### First time User
- __As a first-time user, I want to understand what the applications purpose is so that I can decide if it meets my needs.__  
Located on the homepage, above the fold banner Image describes Movie2archive’s purpose and the function of the application.  
![User stories - First time user q1](/docs/testing/user_stories_teting_images/q1_user_stories_first_time_user.png)  

- __As a first-time user, I want to be able to easily navigate to the registration page.__  
Located at the top of every page is the main navigation bar, when a user is not logged in Login and Register will be available to the user on all pages until they authenticate by logging into Movie2archive.  
![User stories - First time user q2](/docs/testing/user_stories_teting_images/q2_user_stories_first_time_user.png)  

- __As a first-time user, I want to find out how to add a movie to my collection.__  
Located on the homepage are 3 simple steps outlining how to  get started using Movie2archive, the user can use these directions to add a item to their collection or select add a movie within their profile page.  
![User stories - First time user q3](/docs/testing/user_stories_teting_images/q3_user_stories_first_time_user.png)  

- __As a first-time user, I want to view my collection.__  
When a user has logged in, they will be directed to their profile page, within this page under section what would you like to do I a direct link to view a collection, alternatively a user can select my collection located on the main navigation bar.  
![User stories - First time user q4](/docs/testing/user_stories_teting_images/q4_user_stories_first_time_user.png)  

- __As a first-time user, I want to find out more information about a movie I have added.__  
When a user is logged in, they can visit my collection page, located next to every movie list item is a button which reads view, selecting this will take the user to a movie details page, alternatively the user can select the title of the movie to be taken to the same page.  
![User stories - First time user q5](/docs/testing/user_stories_teting_images/q5_user_stories_first_time_user.png)  

- __As a first-time user, I want to find out how to remove a movie in case I make a mistake.__  
Located within the profile page within the section what would you like to do are instructions on how to remove a movie from a collection.  
![User stories - First time user q6](/docs/testing/user_stories_teting_images/q6_user_stories_first_time_user.png)  

- __As a first-time user, I want to know how to log out of Movie2archive.__  
Located on the main navigation bar when a user is logged in will be a Logout link which when activated will end their aession and return them to the homepage as a non logged in user.  
![User stories - First time user q7](/docs/testing/user_stories_teting_images/q7_user_stories_first_time_user.png)  


## Intergrated testing stages
- Construct and render flask application to browser:  
PEP8 complience - Python, flask structure files - PASS  
- Database tables User, MediaType and Location models created, postgres database initialised and tables created sucessfully.  
PEP8 complience - models.py - PASS  
- Database tables Edition and Movielookup added to database.  
PEP8 complience - models.py, routes.py - PASS  
- Database mediaArchive setup and deployed in MongoDB Atlas.  
PEP8 complience - routes.py used to connect and test insert, read and delete fnction - PASS  
- Test oage created movies-mdbtest.html to render retrieved data from MongoDB - retrieved sucessfully.  
- route.py, class movie_test created to test api call and print json data, new page movietest.html was used to test display output - retrievedand read sucessfully.  


## Development bugs
- MovieLookup table renamed to Movielookup as second capital causes an _ to appear in postgresql database tables view - Fixed
