# chordBOOK
This web application was designed to be used primarily by **guitarists** but also by other musicians who want to keep their songs for practice and/or performance in one place. It would serve as a replacement for a personal song book in a classic physical format. For instance musicians would be able to neatly organise their songs required for the next saturday's night gig in a local pub in case they would need a little help with the lyrics, or in case they forget which chords to play for that new number that was only added to the repertoire.

# UX
This website was intended to have three sections - two dynamic and one static.

Home page serves as the collection of all songs that user had added. Each song is shown as a card that has an image (except in mobile view) and three different functionalities - to display song's lyrics and the chords, to edit them and to delete the song all together.

Second section is where users can add their song of choice, populate it with the lyrics and chords and even be able to select a cover image for the song by simply providing a URL to the image location.

As this website is primarily aimed for guitarists, third section simply has a diagram with the chords that would be sufficient for any type of mainstream and commercial song in case a user needs a little reminder, or just wants to learn a new chord.

With the future features (like pagination, search and sort functionalities) this website could be a useful tool for any aspiring as well as accomplished musician.

## Wireframe
Initial sketch for the project design:

Sketch created with InVision: [chordBOOK](https://projects.invisionapp.com/prototype/chordBOOK-ckdni6ct400921v01smyasrfs)

# Features
## Existing Features
Create and read functionality - allows users to add their songs to the collection. User must provide name of the artist/band, name of the song and lyrics/chords. Optional feature is to provide URL for the image that would represent a song in the collection. After user presses the save button song will automatically appear on homepage in a card format. Card has three buttons Chords, Edit, Delete. 

Edit functionality - allows user to modify and update saved songs

Delete functionality - user can delete a song from the collection

## Features Left to Implement
• **Pagination** - as the user's collection will grow, the home page will become a large scrollable section which is not very economic when browsing through the content and this way user will get an experience just like the one when browsing through the actual song book in a physical format.

• **Sort** - functionality that will allow user to sort songs by alphabetic order, either by the artist's name or by the song's name

• **Search** - user will have the possibility to search for the song and access the lyrics/chords section quickly.

• **Auto-scroll** - functionality that will allow user to play along as the section with the lyrics/chords scrolls down automatically so the user won't need to do it manually and interrupt the playing.

# Technologies Used
• **Python/Flask** - The project uses Python language within Flask framework to provide different functionalities

• **HTML** - The project uses HTML as the core structure of the website 

• **CSS** - The project uses CSS for better UX 

• **Materialize** - The project uses Materialize library to simplify page layout creation 

# Testing
This website was built based on the desktop view sketch (link available in the Wireframes section of this readme file) with Materialize cards component in mind.
Every user input should manifest as a Materialize card and it should come in two cards (columns) per row.

## TESTING the Features
### Add a song section:
i. Go to the "Add A Song" page

ii. Try to click on Save button and verify that an error message appears

iii. Try to add Artist Name, Song Name and Chords and verify that it redirects you to the Home Page and the new card is created with default image

iv. Try to add Artist Name, Song Name, Chords and URL for the image and verify that it redirects you to the Home Page and the new card is created with the chosen image

### Home page section:
i. Go to the "chordBOOK" page

ii. Try to click on any card's **Chords** button and verify that a new page appears with the user defined content

iii. Try to click on **Edit** button and verify that it redirects you to the Edit section

iv. Go back to the "chordBOOK" page

v. Try to click on any card's **Delete** button and verify that a prompt appears for you to confirm the action

vi. Press Ok to confirm the action and verify that you are redirected to the home page and the song is now removed from the collection

vii. Click again on any card's Chords button and then on Delete button and verify the same as for the steps v. and vi.

### Edit functionality

i. Go to the "chordBOOK" page

ii. Try to click on any card's **Edit** button and verify that it redirects you to the Edit section

iii. Try to amend the fields but leave any of these empty: Artist Name, Song Name and Chords and verify that an error message appears

iv. Try to amend all the fields but leave the field with URL for the image empty and verify that it redirects you to the Home Page and the existing card is updated with default image

v. Try to amend all the fields along with URL for the image and verify that it redirects you to the Home Page and the existing card is updated with the chosen image

### Delete functionality

i. Go to the "chordBOOK" page

ii. Try to click on any card's **Delete** button and verify that a prompt appears for you to confirm the action

iii. Press Ok to confirm the action and verify that you are redirected to the home page and the song is now removed from the collection

iv. Click again on Chords button and then on Delete button and verify the same as for the steps ii. and iii.

### 404 page

i. Go to "chordBOOK" page and in the address bar try to change or delete last two characters and verify that the error appears and a link to the home page

# Deployment
All the code has been written in Visual Studio Code and was committed to my GitHub repository https://github.com/Lingvistik/chordBOOK

The code was deployed to Heroku and the live version of the website is available here: http://the-chord-book.herokuapp.com/songs

## Deployment process

Firstly, I needed to install the Heroku Command Line Interface (CLI) so I was able to manage Heroku app directly from the Visual Studio Code terminal.
Then I needed to connect my Visual Studio Code project with my Heroku profile by using the command - heroku login
I had to create Procfile to specify the commands that are executed by the app on startup - **web: python3 app.py**
I have also created requirements.txt file by typing command - pip3 freeze > requirements.txt in the terminal of Visual Studio Code
Once I had done all the preparation I then went to Heroku website and created a new app and use this command in the terminal - **heroku git:remote -a the-chord-book**
Next, I went to settings on my heroku app and updated Config Vars. I have set IP to 0.0.0.0 and PORT to 8080. I have also entered my environment variable and the value which is a password for my MongoDB collection.
Finally, I ran a command in the terminal - **git push heroku master**
After that command my application was deployed.

# Credits
## Content

• All the example chords and lyrics are taken from https://www.ultimate-guitar.com

Acknowledgements
• I have received inspiration for this project as a long term user of the legendary website ultimate-guitar.com
