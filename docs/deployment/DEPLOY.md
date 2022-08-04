# Deploying a Project to Heroku

Video tutorial from Code Institute:
[https://youtu.be/Mb9\_EkN5Sqk](https://youtu.be/Mb9_EkN5Sqk)

## Local IDE/CDE (Gitpod)

In the terminal window enter:

1. Pip3 list to list dependences for the application in the terminal
2. Pip3 freeze –-local > requirements.txt //generates a requirements.txt file for Heroku

If any new packages are added, this file must be updated and added to Heroku.

1. echo web: python run.py \&gt; Procfile generates a Proc file for Heroku

Note: Using echo may cause the Proc file to add an extra line at end of the file, delete the extra line to avoid problems.

1. Push to GitHub

## Go to Heroku and login

Note: Heroku allows 5 apps without verifying adding details and 100 if details are added

1. Navigate to the dashboard once logged in and at the top right select &quot;New&quot; then create new app
2. Give your app a unique name in the text field
3. Select your region &quot;Europe&quot; and select Create app

Will be redirected to the deploy screen.

Do not upload our local database, create a new one in Heroku instead to avoid personal data breaches, covered further on.

1. Select the Resources tab then under add-ons search for Heroku Postgres and when found select.
2. A Popup will ask for the account type, select hobby dev – free and then Submit order

Heroku will then attach postgresql to the app.

1. The add-on heroku-postgresql has been installed will be displayed when done.

Check out the documentation in its [Dev Center](https://devcenter.heroku.com/articles/heroku-postgresql) article to get started, if you want to learn more.

1. Click settings and go to config vars and then select reveal config vars
2. Enter into the fields the details from the env.py file

Important: do not add Development or DB\_URL keys and values

Key and Value eg. IP (Key) 0.0.0.0 (Value)

1. Once a key and value have been entered, select add to generate another field to enter another key and value.
2. SECRET\_KEY – the value field of this key can be anything you choose
3. Set debug to True when building, but must set to False when submitting a project for assessment.

## Go back to your IDE

At the moment, the app.config lines are pointing to the SECRET\_KEY and DB\_URL

Because Heroku is using a different Database, we need to add a conditional statement to check if we are accessing a local DB or the one on Heroku.

1. pen the \_\_init\_\_.py file

Example app.config call:

app.config[&quot;SQLALCHEMY\_DATABASE\_URI&quot;] = os.environ.get(&quot;DB\_URL&quot;)

1. Add a conditional statement:

if os.environ.get(&quot;DEVELOPMENT&quot;) == &quot;True&quot;:

app.config[&quot;SQLALCHEMY\_DATABASE\_URI&quot;] = os.environ.get(&quot;DB\_URL&quot;) # This is the local DB

else:

app.config[&quot;SQLALCHEMY\_DATABASE\_URI&quot;] = os.environ.get(&quot;DATABASE\_URL&quot;) # This is the Heroku DB

1. Save the file and push changes to the GitHub repo
2. Then go back to Heroku

## Heroku dashboard

1. Select the Deploy tab on to left top menu:

There are 3 options to choose, Heroku CLI, GitHub or Container registry

1. Select GitHub (connect to GitHub)
 Will use the repo to build the app and update changes.
2. Just below, next to connect to GitHub there will be a search for a repository to connect to field.

Make sure it is your name and then enter the repo name in the search field and select search.

1. The repo should show bellow and if all looks good, select the Connect button.
2. Just below next to Automatic deploys make sure main branch is in the dropdown field.
 Then select Enable Automatic Deploys button.

Note: The reason for doing this is so when we push to GitHub it then gets pushed to Heroku and the Heroku app rebuilds and displays the changes we have made.

Please be aware: Do not push to GitHub from your machine if the app you are working on does not load or has errors e.g. Jinja errors, as if you do the Heroku app will not be able to build and will cause errors in the Heroku dashboard.

1. Finally select the Deploy Branch button at the bottom of the page.

This may take a few minutes while it builds, when it is done, there will be a message saying:

Your app was successfully deployed with a view button.
 (Do not click)

1. Go to Settings top left, and then select reveal config vars as we did before, you should see that data has been auto populated.

The area to take note of is the DATABASE\_URL value field:

If it says postgres:// Then further steps are needed

If it says postgresql:// - Ignore the below steps.

## Steps:

1. Open the \_\_INIT\_\_.py file in your IDE.

And add the following code:

1. Import re (at the top of the file just below import os)
2. Within the else statement that was added in previous steps, amend the code to as follows:
 We are adding a uri variable which will string replace one url for another.


if os.environ.get(&quot;DEVELOPMENT&quot;) == &quot;True&quot;:

app.config[&quot;SQLALCHEMY\_DATABASE\_URI&quot;] = os.environ.get(&quot;DB\_URL&quot;)

else:

uri = os.environ.get(&quot;DATABASE\_URL&quot;)

if uri.startswith(&quot;postgres://&quot;):

uri = uri.replace(&quot;postgres://&quot;, &quot;postgresql://&quot;, 1)

app.config[&quot;SQLALCHEMY\_DATABASE\_URI&quot;] = uri # Heroku

1. Save and push to GitHub

Wait a few minutes to allow Heroku to rebuild the app

## Go back to Heroku

1. Select the Activity tab, top left of the screen, then select the more button at the top right and choose Run console
2. Console will open.
3. Enter: python3
 in the field, select run or hit enter
4. Then in the console window enter:

from <database name> import db Press enter

Note: (<database name> is the name of the database in this case but will be whatever your db is called)

1. Then enter:

db.create\_all() Press enter

When a new line shows \&gt;\&gt;\&gt;\&gt;\&gt;

1. enter: exit() Press enter and then use the &quot;X&quot; to the right to close the console window.
2. With everything setup:
 Select the Open app button at the top right of the screen and your app should be displayed in all its glory.

Note: the database is empty, so new data will need to be entered etc.

[Back to Repository](https://github.com/JHodgkins/MSP3-Movie2Archive)  