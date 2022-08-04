# Testing  
This document details how the Movie2Archive web application was tested to ensure that complience, a good user experiance was achieved and to make the application as accessible to all its users.  
Tests were carried out throughout development in an intergrated way, the tests were carried out at each main application development stage or when a new feature addition was being developed to ensure PEP8 complence within Python code was maintained and ensure when developng fromtend elements that, HTML, CSS and JS complience was maintained also.

## Table of contents
 
1. [User stories testing from the UX section](#user-stories-testing-from-the-ux-section)  
    2.1 [First time user](#first-time-user)  
    2.2 [Returning user](#returning-user)  
    2.3 [Site owner](#site-owner)  

## User stories testing from the UX section  
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

### Returning user  
- __As a returning user, I want to be able to easily navigate to the login page.__  
Located across all pages on the main navigation bar will be a link to the login page when a user is not authenticate on the site.  
![User stories - Returning user q1](/docs/testing/user_stories_teting_images/q1_user_stories_returning_user.png)  

- __As a returning user, I want to be able to edit a movie entry I have in my collection.__  
When a user selects view my collection within their profile or my collection from the main navigation bar, they are taken to their collection page, under every item is an edit button to edit that entry.  
A user can edit every part of their original entry including media type, edition and location.  
![User stories - Returning user q2](/docs/testing/user_stories_teting_images/q2_user_stories_returning_user.png)  

- __As a returning user, I want to be able to see how many movies are in my collection.__  
Located within their profile the main banner above the fold section displays clearly how many items are within a users total collection.  
![User stories - Returning user q3](/docs/testing/user_stories_teting_images/q3_user_stories_returning_user.png)  

- __As a returning user, I want to be able to change my password.__  
Located within a user’s profile page under section edit your user account details is a link to update the users password if they feel it may have been compromised.  
![User stories - Returning user q4](/docs/testing/user_stories_teting_images/q4_user_stories_returning_user.png)  

- __As a returning user, I want to be able to move my collection to another room location.__  
Located within my collection the user can select edit to edit the movie entry they have added.  
The user can edit any movie within their collection individually, bulk moving location is not present at this time as this would not be the case for an average user.  
![User stories - Returning user q5](/docs/testing/user_stories_teting_images/q5_user_stories_returning_user.png)  

- __As a returning user, I want to be able to update my account login details.__  
Located within the profile page under update my account details is a link to update user details, this information includes username and email address.  
![User stories - Returning user q6](/docs/testing/user_stories_teting_images/q6_user_stories_returning_user.png)  

### Site Owner  
- __As the site owner, I want visitors to find Movie2archive approachable and know its purpose from the outset.__  
Located on the homepage are examples of what Movie2archive does and how to use the application.  

- __As the site owner, I want visitors to gain more information and learn new facts about the movies they own.__  
Located on the about page, a brief explanation of what inspired the creation of Movie2archive and its plans moving into the future.  

- __As the site owner, I want visitors to be able to easily add their movies.__  
A user is able once logged in to reach the add a movie page from either their profile or through the main navigation in 3 or less clicks, leaning on the set out target when developing the application.  

- __As the site owner, I want the site visitors to be able to see what they own and see their collection by media type.__  
When a user visits their collection, they are able to filter their collection by media type uch as DVD, Blue Ray or VHS.  

- __As a site owner, I want to encourage recycling to the applications users.__  
Located on the homepage, will be a third party integration in the future, until such time a random recycling provider baed in the UK is used in this case a informative piece about Zapper the merchants who are able to recycle physical media.  


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
