# Project Overview
This is the online portal for the coffee shop. The purpose of this porject is to provide information related to shop online to all the customers to make it easy for them to access the variety of products available in shop. In addition to that, customers can order online for their purchase.

Users can create profile to keep their information avalilabe in shop's database. After that, they just need to login and can order quickly as need not to repeat stored information while ordering.

In this project Django, HTML and CSS are used.

# Project Objectives
Main objectives concluded for this project are following:
- To create a simple, informative and user friendly website
- To provide possibility for user to create a profile and order with that and also to be able to order without login
- To create a functioning website having information about all the available items in store


# Features

## Navigation Bar

Navigation bar has links for different pages on this site to which customer are supposed to navigate through in order to access related information/activity.

![Navigation_Bar](media/header1.png)


## Home Page

This is the page where customer will land as soon as he/she will go to web url.

![Home_Page](media/homepage1.png)


## Products Page

This page has the list of all the products available for customer. Products are as well categorize further for easier navigation for cutomers.

![Product_page](media/products.png)


## Hot Coffee Page

All avaiable type are added in this page.

![hot_coffee_view](media/hotcoffee.png)


## Cold Coffee Page

All avaiable type are added in this page.

![cold_coffee_view](media/coldcoffee.png)

## Smoothies

All avaiable type are added in this page.

![smoothies](media/smoothies.png)

## Summer-special-drink

All avaiable type are added in this page.

![Summer-special-drink](media/summerspecial.png)

## Swedish-fika

All avaiable type are added in this page.

![Swedish-fika](media/fika.png)


## Special offers(combo pack)

All avaiable type are added in this page.

![special_offer_page_view](media/combopack.png)

## Facebook page 

![facebook_page_view](media/facebook.png)

# Testing

Various test cases were executed through out the development process to make sure that design is in line with project objective and website is fully functional. Majorly test cases can be categrized in 2 categories as GUI and functional testing.

## GUI Testing

Not all the GUI test cases were passed due to inconsistancy in platform connections. Still there are a lot of falied cases but unfortunately can't proceed with solving those at the moment.

## Functional Testing

All functional test case are passed.

## Lighthouse Results

![lighthouse_view](media/lighthouse.png)

## Defects

Few of still outstanding defects are:
1. Home page is not visible correctly when url is entered (random occurance)
2. All products are not visible with respective image
3. Payment option is not correctly visible to the customer

# Technologies used

Tool/Language Used
- HTML
- CSS
- JavaScript
- Python
- Django

Django Package
- Gunicorn as the server for Heroku
- Dj_database_url to parse the database URL from the environment variables in Heroku
- Psycopg2 as an adaptor for Python and PostgreSQL databases
- Allauth for authentication, registration and account management
- Stripe for processing all online and credit card purchases on the website
- Crispy Forms to style the forms
- Pillow to process and save all the images downloaded through the database


# Deployment

- Create Pipfile

- In the terminal enter the command pip3 freeze > requirements.txt, and a file with all the requirements will be created.

- Setting up Heroku
    - Go to Heroku website
    - Login to Heroku and choose Create App
    - Click New and Create a new app
    - Choose a name and select your location
    - Go to the Resources tab
    - From the Resources list select Heroku Postgres
    - Navigate to the Deploy tab
    - Click on Connect to Github and search for your repository
    - Navigate to the Settings tab
    - Reveal Config Vars and add your AWS, Database URL (from Heroku-Postgres) and Secret key.

- Deployment on Heroku
    - Go to the Deploy tab.
    - Choose the main branch for deploying and enable automatic deployment
    - Select manual deploy for building the App
    - Wait until build is complete
    - Click on Open App button
    - Website launched now
