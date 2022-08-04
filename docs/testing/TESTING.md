# Testing  
This document details how the Movie2Archive web application was tested to ensure that complience, a good user experiance was achieved and to make the application as accessible to all its users.  
Tests were carried out throughout development in an intergrated way, the tests were carried out at each main application development stage or when a new feature addition was being developed to ensure PEP8 complence within Python code was maintained and ensure when developng fromtend elements that, HTML, CSS and JS complience was maintained also.

## Table of contents
 
1. [User stories](#user-stories)  
    1.1[First time user](#first-time-user)  
    1.2 [Returning user](#returning-user)  
    1.3 [Site owner](#site-owner)  
2. [Testing overview](#testing-overview)  
3. [Test results overview](#test-results-overview)  
4. [Validation Testing](#validation-testing)  
    4.1 [HTML validation](#html-validation)  
    4.2 [CSS validation](#css-validation)  
    4.3 [JS validation](#js-validation)  
5. [Database testing stages](#database-testing-stages)  
    5.1 [Database bug/fixes](#database-bugsfixes)  
6. [Manual tests](#manual-tests)  
    6.1 [Rendering in browser & Reflow test](#rendering-in-browser--reflow-test)  

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

## Testing Overview  
__Automated testing__
All automated tests were carried out using incognito mode to eliminate extension conflicts or false positives or errors due to the extension requests.  

__Manual testing__  
All manual testing was carried out in standard mode to simulate a standard users experience of the web application.

__Libraries__  
As the project technologies used the Bootatrap framework and Font Awesome for icons there is a possible effect on performance audit scored.  
CDN's were used to provide a minified cached version of both frameworks but this can still be a larger file when page loads.
CSS preloader tags were used to illiminate render blocking script flag within Lighthouse and defering of scripts where necessairy was used on Javascript libraries and scripts.    

__Performance__  
Due to experiance and the restrictions of the shared environment of Heroku for compiling and serving the application on the frontend, certain performance metrcs are affected as the shared hoting will sleep to conserve resources and wake when needed, a payed plan providing always on connection and more higher performance may yield faster performance.    

__PEP8 complience__  
PEP8 complience has been followed throughout the project, the project was developed using GitPod and the full template provided by Code Institute which includes Python linting to eansure complience.  

__Accessibility extensions__  
All results from accessibility extensions were verified using manual tests and where relevant were validated using real Screen Reader software using a human tester.  

__Screen Reader software__  
NVDA and JAWS were used in some tests, this is software which I own and was run in real time and not simulated through an extension or virtual environment.  

## Test results overview  
Below is a table which represents an overview of the various tests undertaken duuring and through development, results of these tests and issues were collected and stored in an Excel document for functionality and accessibility reasons, the excel document contains 3 sheets of tests.  
Please find the [movie2archive test records.xlsx](movie2archive_test_records.xlsx) file on the GitHub repository.  
 
| Test             | Logged out user | logged in user | Admin user |
|------------------|----------|-------------------|------|
| Database connections  | PASS     | Pass              | PASS | 
| HTML Validation  | PASS     | Pass              | PASS | 
| CSS Validation   | PASS     | PASS               | PASS | 
| JShint           | PASS     | PASS              | PASS | 
| Links            | PASS     | PASS              | PASS | 
| Landmark Regions | PASS     | PASS              | PASS |
| Screen reader    | PASS     | PASS              | PASS |
| Lighthoise - <br>Performance,<br>Accessibility,<br>Best practice,<br>SEO | PASS         | PASS         | PASS          |

## Validation testing  
### HTML validation  
-  Homepage - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_homepage.png)  

-  About - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_about_page.png) 

-  Login - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_login_page.png) 

-  Register - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_register_page.png) 

-  My collection - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_collection_page.png) 

-  Profile - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_profile_page.png) 

-  Dashboard - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_dahboard_page.png) 

__Add and Edit pages__  
As the only thing that changes on these pages only 1 is needed to be validated as the content is filtered intoo a template file and the form is inserted.  

-  Add/Edit - media type/location type/edition type - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_add_media_page.png) 

-  Add/Edit - movie - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_add_movie_page.png) 

-  Add/Edit - User details/Password - PASS  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_update_user_details_page.png) 

### CSS validation  
As the site uses one CSS style sheet, the stylesheet wa validated by pasing in the raw code to the validator.  

-  CSS stylesheet - PASS  
![W3C CSS Validator result](/docs/testing/validator_testing_images/test_css_validator.png)  

### JS validation  
![JShint Validator result](/docs/testing/validator_testing_images/test_jshint_validator.png)  
Jhint was used and no errors were detected.  

## Database testing stages
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

## Database bugs/fixes  
- MovieLookup table renamed to Movielookup as second capital causes an _ to appear in postgresql database tables view - Fixed  

## Manual testing  
### Rendering in browser & Reflow test  
Devices used: Windows 10 PC, Mac Studio, iPad Air 2, iPhone X  
Desktops  
-  Chrome, EDGE, Firefox on PC - PASS  
-  Safari, Chrome on Mac - PASS  
Tablet and mobile
-  Safari - PASS  
I found that the web application and application reflowed and displayed correctly and as expected on different screen sizes and systems.  

### Link testing  
All links within the web application were tested to ensure that internal links behaved correctly, and external facing links such as social media links, third party links opened in a new tab.  
A screen reader was used during these tests on PC and MAC to ensure that the Sr-Only CSS help text classes which have been applied were announced correctly by the screen reader software.  
an example of the code is shown below:  
```
<li class="ms-3">
        <a target="_blank" href="https://twitter.com/" rel="noopener">
          <i class="fab fa-twitter" aria-hidden="true"></i>
            <span class="sr-only">Find us on Twitter (opens in a new window)
            </span>
          </a>
      </li>
```  
All pages were tested, and no issues were found.  

