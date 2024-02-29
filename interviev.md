1) Django design pattern?

Django follows MVC pattern (Model-View-Controller), also referred to as MTV (Model-Template-View).

Model – describes database schema
Views – Controls what user can view. It retrieves data from the table and passes it to the template which is rendered to Browser eventually.
Template – Determines how the user sees it.
Controller – controls the entire flow of models and data.

2) What are the features available in Django?

Admin Interface
Forms
Templating
The session, user management
Object-relational Mapping (ORM)

3) How Django process a request?

When a user requests a page, Django determines whether the request URL pattern is mentioned in URLs.py. Once the regex matches, Django calls the corresponding view. HttpRequest is passed as an argument to that view function and the implementation part is executed further.

4) What is CSRF?

CSRF – Cross Site Request Forgery. Csrf tokens could also be sent to a client by an attacker due to session fixation or other vulnerabilities or guessed via a brute-force attack, rendered on a malicious page that generates thousands of failed requests.

5) What is Django?

Django is a high-level Python-based, open-source web framework written in Python to develop a web application to encourage rapid development and clean, pragmatic design. Django follows the model-view-template architectural pattern and developed by a fast-moving online-new operation. Django is designed to handle intensive deadlines of a newsroom and the stringent requirements of the experienced web developers who developed it. It allows you to build a high performing web application quickly.

Django, a web application framework is a collection of modules that are grouped together to enable you to create an application or a website from an existing source. This collection of modules makes the development of web application or a website fast and easier.

A single person can design and still can include advanced functionality like authentication support, admin panel, management panel, contact forms, comment boxes, file upload, and many more. To create a website from scratch you would have to develop these components by yourself. These components are already built and you just need to configure them as per your requirement to build your site. You can focus on developing your app as Django offers a big collection of modules that can be easily used in projects and takes care of most of the hassle of web development.

Django is named after one of the best guitarists of all time Django Reinhardt, a gypsy jazz guitarist from the 1930s to early 1950s.

2.2.1 is the latest and stable version now.

6) Why Django?

Django is a free and open-source framework to develop web applications. Web development process becomes very easy and developer can focus only on designing process and boosts performance. Django follows the model-view-template architectural pattern. Django, a web application framework is a collection of modules that are grouped together to enable you to create an application or a website from an existing source. This collection of modules makes the development of web application or a website faster and easier.

Django is a quick solution for web development. It has become the right platform for a customer for business and developers due to its ability to deliver high-quality code and transparent writing.

Batteries Included – Django comes with a collection of modules also know as Batteries. A lot of out of the box stuff, you may or may not use for your application comes with Django. Instead of writing your own code, just import the package you wish to use.

Wide range of topics are spanned in Django batteries which includes –

auth package for authentication
admin package for Admin interface
Sessions package for Session management
Messages package to manage temporary or session-based messages
Sitemaps package to generate Google sitemap XML
Postgress Package for Postgress special features
Content types framework to hook into “types” of content

7) What are the disadvantages of Django?

Django is an amazing framework, still, there are a few cons. The URL specifying with regular expressions is not an easy task. Template errors fail silently by default, to know that, you may waste a lot of time to figure out what’s wrong, or you might not even know that your application has a problem. Along with the advantages, there are many disadvantages to Django mentioned below.

Template Mistakes Flop Discreetly itself – System developers do not pay attention to mistakes when they undertake a class-based viewpoint and they are extended through inheritance.

Does Not Have The Capacity To Manage Different Requests At The Same Time:

Django does not support individual procedures to deal with many requests at the same time. Developers need to investigate approaches and make singular procedures to control various requests proficiently and rapidly at once.

Django is Excessively Monolithic: Django framework directs you into a given specific pattern.

Regex To Indicate Its URL: Django uses regex to determine its URL routing models, which makes the code bigger and makes convoluted syntaxes.

While Managing Backwards Compatibility, It’s Moving Extremely Gradually: Django has a tendency to get greater and heavier after some time. Django stresses more on dev profitability and backward compatibility than the speed.

Django uses routing patterns to specify its URL.
Everything is based on Django ORM and the ORM system lacks features.
Components are tightly coupled and get deployed together
To work with Django, knowledge of the full system is required.
There are many pros and cons of Django, still, when a project with a deadline is considered, using Django for the project provides the ultimate solution.

8) Can you explain the working philosophy of Django?

The Django follows “Batteries included” philosophy which provides almost everything developers want to try “out of the box”. Everything you need to develop an application is part of the one product, and it works seamlessly together, and also follows consistent design principles.

Django’s working philosophy breaks into many components –

Models.py file: Using Python object Django web applications manage and query data and is referred to as models. It defines the structure of stored data along with field types, default values, selection list options, maximum size, label text for forms, etc. Once you select what database you want to use, you just need to write model structure and other code, Django handles all the work of communicating with the database.
Views.py file: Views are the main part of Django and the actual processing happens in view. For searching database, Django model provides simple query API. It can match the number of fields at a time using different criteria and can support complex statements.
Urls.py file: It uses a regular expression to capture URL patterns for processing. Django allows you to design URLs the way you want, with no framework limitation.
When a user sends a request on Django page:

Django runs through each URL pattern in order and stops at first one pattern that matches with, URL you have created and uses the information to retrieve the view.
The view processes the request and queries database if required.
Requested information to your template.
The template renders the data in a format you have created and displays the page.

9) What are the advantages of using Django for web development?

Django is written in Python programming language and hence it becomes easier for programmers to build web applications with clean, readable and maintainable code.
Being a matured framework, its design rules focus on reducing web application development time. According to varying business requirements, the features provided by Django enable developers to build custom web applications rapidly.
Django adopted the batteries-included approach.
Django is compatible with major operating systems and databases. By supporting major operating systems like Windows, macOS, Linux, Django enhance the accessibility of web applications.
Built-in security features provided in Django helps developers to protect the web applications from a variety of security attacks like cross-site scripting, SQL injection and cross-site request forgery.
Django enables programmers to build better and modern web applications. Django developers can easily customize, scale and extend the web framework by making changes to decoupled components.
Django provides an Auto-generated web admin to make website administration easy.
For common user tasks, pre-packaged API is also available.
Using this framework, business logic can be separated from the HTML.
Can divide the code modules into logical groups, to make it flexible for changing.
Template system provided to define the HTML template for the web page to avoid code duplication.
Django is supported by large and active community developers. The Django developers can easily speed up custom web application development by taking advantage of resources uploaded by members of the Django community.

10) What is CRUD?

The most common task in web application development is to write create, read, update and delete functionality (CRUD) for each table. It refers to the set of common operations that are used in web applications to interact with data from the database. It provides a CRUD interface that allows users to create, read, update or delete data in the application database.

Django helps us with its simplified implementation for CRUD operations using Function-Based views and class-based Views.

Function- based views are simple to implement and easy to read but they are hard to customize or extend the functionality. Code reuse is not allowed and so there is repetitiveness.
Class-based views – In no time CRUD operations can be implemented using CBVs. As the model evolves changes would be reflected automatically in CBVs. CBVs are easily extendable and allow code reuse. Django has built-in generic CBVs which makes it easy to use.

11) What is the list of backends supported by Django?

Django tried to support as many features as possible on all database backends still, not all database backends are the same, and we have to decide on which features to support and which assumption we can make safely.

Django officially supports three other popular relational databases.

Below is the list of relational databases supported by Django –

PostgreSQL
MySQL and
Oracle
Below is the list of databases to which Django supports connectivity –

SQLite – Django automatically creates an SQLite database for your project.
SAP (Sybase) SQL Anywhere
IBM DB2
Firebird
ADO- Microsoft SQL Server
ODBC – Microsoft SQL Server
Azure SQL database or other ODBC compatible database
Configuration to connect to the database is done in the settings.py file of the Django project.

ADO (ActiveX Data Objects) and ODBC (Open Database Connectivity) interfaces are standard for connecting to Microsoft SQL Server and is supported by most relational database brands.

12) Is Django a content management system (CMS)?

No, Django is not a Content Management System (CMS), rather it is a Web application framework and a programming tool that helps you to build websites.

DjangoCMS is a web publishing platform built with Django and offers out of the box support for the common features you expect from a CMS. Django CMS can be easily customized and extended by developers to create a site precise to their needs.

Django CMS is a thoroughly tested platform that supports both large and small web sites. Django CMS is robust internationalization support for creating multilingual sites. It can be configured to handle different requirements. Content editing is possible and provides rapid access to the content management interface. Django CMS supports a variety of editors with advanced text editing features. It is a flexible plugins system. Thorough documentation is available for Django CMS. Each published CMS page exists at two instances public and drat. An only draft version exists till you publish it.

13) Explain mixins in Django.

A Mixin is a special type of inheritance in Python. It is gaining a big rise in Django / Web Application Development. Mexin can be used to allow classes in Python to share methods between any class that inherits from that Mixin.

A mixin or mix-in is a class that contains methods for use by other classes without having to be the parent class of those other classes. Sometimes Mixins are described as “included” rather than “inherited”.

Django provides a number of mixins that provide more discrete functionality. Different type of mixins are –

Simple mixins are –

ContextMixin – A dictionary to include in the context and is a convenient way of specifying the simple context in as_view().
TemplateResponseMixin – Given a suitable context, TemplateResponseMixin provides a mechanism to construct a TemplateRespons and the template to use is configurable and can be further customized by a subclass.
SingleObjectMixin – SingleObjetMixin provides a mechanism for looking up an object associated with the current HTTP request.
SingleObjectTemplateMixin – SingleObjetTemplateMixin performs template base response rendering for view that operate upon a single object instance.
MutlipleObjectMixin – MultipleObjectMixin used to display list of objects

14) What is Django? Elaborate some technical features of Django.

Django is a high-level web application framework based on Python.

This framework is one of the best in the industry for rapid development, pragmatic design without compromising on features.

Some of the technical features of Django include:

Admin Interface
Code Reusability
CDN Integration
Security Features
ORM
A huge number of third-party applications
There are many features which Django community has been developing over the years and therefore it’s called “Batteries-Included” framework, as it has lots of features built-in which otherwise would be time-consuming and expensive to make.

15) What is Django Admin Interface?

Django Admin is the preloaded interface made to fulfill the need of web developers as they won’t need to make another admin panel which is time-consuming and expensive.

Django Admin is application imported from django.contrib packages.

It is meant to be operated by the organization itself and therefore doesn’t need the extensive frontend.

Django’s Admin interface has its own user authentication and most of the general features.

It also offers lots of advanced features like authorization access, managing different models, CMS (Content Management System), etc.

16) How is Django’s code reusability feature different from other frameworks?

Django framework offers more code-reusability than other frameworks out there.

As Django Project is a collection of different applications like login application, signup application.

These applications can be just copied from one directory to another with some tweaks to settings.py file and you won’t need to write new signup application from scratch.

That’s why Django is a rapid development framework and this level of code reusability is not there in other frameworks.

17) Django is an MVC based framework, how this framework implements MVC?

Django is based on MTV architecture which is a variant of MVC architecture.

MVC is an acronym for Model, View, and Controller.

There are different parts of a website so that they can develop and execute in different machines to achieve faster and more responsive websites.

Django implements MTV architecture by having 3 different components and they are all handled by Django itself.

Models are the part which is models.py file in a Django application, which defines the data structure of the particular application.

View are the mediators between models and templates, they receive the data from the Model and make it a dictionary and return the same as a response to a request to the Template.

The Template is the component with which user interacts, and it generates both statically and dynamically in the Django server.

That’s how the Django implements 3 components and work in coordination with each other.

18) What happens when a typical Django website gets a request? Explain.

When a user enters a URL in the browser the same request is received by the Django Server.

The server then looks for the match of the requested URL in its URL-config and if the URL matches, it returns the corresponding view function.

It will then request the data from the Model of that application, if any data is required and pass it to the corresponding template which is then rendered in the browser, otherwise, a 404 error is returned.

19) What is the Controller in the MVC framework of Django?

Ans. As Django implements in MTV framework, these three components communicate with each other via the controller and that controller is actually Django framework.

Django framework does the controlling part itself.

20) Is Django’s Admin Interface customizable? If yes, then How?

Django’s Admin is just one of the applications and very customizable, also you can download a different third-party application and install it for a totally different view.

You can make your own Admin Application if you want complete control over your Admin.

Although you can customize the Django Admin site like changing the properties of admin.site object.

We can also make some changes in particular models and apply them in our Django Admin for particular apps like we can add a search bar for particular applications.

The Django Admin Interface is fully customizable to the lowest level, but instead of customizing that much, we can rather create a new Admin Interface.

So those who don’t like Django Admin Interface, prefer making a new one from scratch then editing the previous one.

21) Why is Django called a loosely coupled framework?

Django is called a loosely coupled framework because of the MTV architecture it’s based on.

Django’s architecture is a variant of MVC architecture and MTV is useful because it completely separates server code from the client’s machine.

Django’s Models and Views are present on the client machine and only templates return to the client, which are essentially HTML, CSS code and contains the required data from the models.

These components are totally different from each other and therefore, front-end developers and backend developers can work simultaneously on the project as these two parts changing will have little to no effect on each other when changed.

Therefore, Django is a loosely coupled framework.

22) What is Django Rest Framework (DRF)?

Django REST is a framework which lets you create RESTful APIs rapidly.

This framework has got funding by many big organizations and is popular because of its features over Django frameworks like Serialisation, Authentication policies and Web-browsable API.

RESTful APIs are perfect for web applications since they use low bandwidth and are designed such that they work well with communications over the Internet like GET, POST, PUT, etc.

23) What is Django?

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source..

24) What does Django mean?

Django is named after Django Reinhardt, a gypsy jazz guitarist from the 1930s to early 1950s who is known as one of the best guitarists of all time.

25) Which architectural pattern does Django Follow?

Django follows Model-View Template (MVT) architectural pattern.

26) Explain the architecture of Django?

Django is based on MVT architecture. It contains the following layers:

Models: It describes the database schema and data structure.

Views: The view layer is a user interface. It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template.

Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page.

Controller: Controller is the heart of the system. It handles requests and responses, setting up database connections and loading add-ons. It specifies the Django framework and URL parsing.

27) Which foundation manages Django web framework?

Django web framework is managed and maintained by an independent and non-profit organization named Django Software Foundation (DSF).

28) Is Django stable?

Yes, Django is quite stable. Many companies like Disqus, Instagram, Pinterest, and Mozilla have been using Django for many years.

29) What are the features available in Django web framework?

Features available in Django web framework are:

Admin Interface (CRUD)
Templating
Form handling
Internationalization
Session, user management, role-based permissions
Object-relational mapping (ORM)
Testing Framework
Fantastic Documentation

30) What are the advantages of using Django for web development?

It facilitates you to divide code modules into logical groups to make it flexible to change.
It provides auto-generated web admin to make website administration easy.
It provides pre-packaged API for common user tasks.
It provides template system to define HTML template for your web page to avoid code duplication.
It enables you to define what URL is for a given function.
It enables you to separate business logic from the HTML.

31) How to create a project in Django?

To start a project in Django, use the command $django-admin.py and then use the following command:

Project

init.py

manage.py

settings.py

urls.py

32) What are the inheritance styles in Django?

There are three possible inheritance styles in Django:

Abstract base classes: This style is used when you only want parent?s class to hold information that you don’t want to type out for each child model.
Multi-table Inheritance: This style is used if you are sub-classing an existing model and need each model to have its own database table.
Proxy models: This style is used, if you only want to modify the Python level behavior of the model, without changing the model’s fields.
33) How can you set up the database in Djanago?

To set up a database in Django, you can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.

By default, Django uses SQLite database. It is easy for Django users because it doesn’t require any other type of installation. In the case of other database you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.

Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on

Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.

Note: You have to add setting likes setting like Password, Host, User, etc. in your database, if you are not choosing SQLite as your database.

34) What does the Django templates contain?

A template is a simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the template is evaluated and tags (%tag%) that controls the logic of the template.

35) Is Django a content management system (CMS)?

No, Django is not a CMS. Instead, it is a Web framework and a programming tool that makes you able to build websites.

36) What is the use of session framework in Django?

The session framework facilitates you to store and retrieve arbitrary data on a per-site visitor basis. It stores data on the server side and abstracts the receiving and sending of cookies. Session can be implemented through a piece of middleware.

37) How can you set up static files in Django?

There are three main things required to set up static files in Django:

Set STATIC_ROOT in settings.py

run manage.py collectsatic

set up a Static Files entry on the PythonAnywhere web tab

38) How to use file based sessions?

You have to set the SESSION_ENGINE settings to “django.contrib.sessions.backends.file” to use file based session.

39) What is some typical usage of middlewares in Django?

Some usage of middlewares in Django is:

Session management,
Use authentication
Cross-site request forgery protection
Content Gzipping, etc.

40) What does of Django field class types do?

The Django field class types specify:

The database column type.
The default HTML widget to avail while rendering a form field.
The minimal validation requirements used in Django admin.
Automatic generated forms.

41) Explain how you can create a project in Django?

To start a project in Django, you use command $ django-admin.py and then use the command
Project
init.py
manage.py
settings.py
urls.py

42) Explain how you can set up the Database in Django?

You can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.
Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings

Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on
Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.
If you are not choosing SQLite as your database then setting like Password, Host, User, etc. must be added.

43) What is the difference between a project and an app in Django?

In Django, a project is the entire application and an app is a module inside the project that deals with one specific requirement. E.g., if the entire project is an ecommerce site, then inside the project we will have several apps, such as the retail site app, the buyer site app, the shipment site app, etc.

44) What is Django Admin Interface?

Django comes with a fully customizable in-built admin interface, which lets us see and make changes to all the data in the database of registered apps and models. To use a database table with the admin interface, we need to register the model in the admin.py file.

45) Explain Django’s Request/Response Cycle.

In the Request/Response Cycle, first, a request is received by the Django server. Then, the server looks for a matching URL in the urlpatterns defined for the project. If no matching URL is found, then a response with 404 status code is returned. If a URL matches, then the corresponding code in the view file associated with the URL is executed to build and send a response.

46) What is a model in Django?


A model is a Python class in Django that is derived from the django.db.models.Model class. A model is used in Django to represent a table in a database. It is used to interact with and get results from the database tables of our application.

47) What are migrations in Django?

A migration in Django is a Python file that contains changes we make to our models so that they can be converted into a database schema in our DBMS. So, instead of manually making changes to our database schema by writing queries in our DBMS shell, we can just make changes to our models. Then, we can use Django to generate migrations from those model changes and run those migrations to make changes to our database schema.

48) What are views in Django?

A view in Django is a class and/or a function that receives a request and returns a response. A view is usually associated with urlpatterns, and the logic encapsulated in a view is run when a request to the URL associated with it is run. A view, among other things, gets data from the database using models, passes that data to the templates, and sends back the rendered template to the user as an HttpResponse.

49) What is the use of the include function in the urls.py file in Django?

As in Django there can be many apps, each app may have some URLs that it responds to. Rather than registering all URLs for all apps in a single urls.py file, each app maintains its own urls.py file, and in the project’s urls.py file we use each individual urls.py file of each app by using the include function.

50) Why is Django called a loosely coupled framework?

Django is called a loosely coupled framework because of its MVT architecture, which is a variant of the MVC architecture. It helps in separating the server code from the client-related code. Django’s models and views take care of the code that needs to be run on the server like getting records from database, etc., and the templates are mostly HTML and CSS that just need data from models passed in by the views to render them. Since these components are independent of each other, Django is called a loosely coupled framework.

51) Mention the architecture of Django architecture?

Django architecture consists of

Models: It describes your database schema and your data structure
Views: It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template
Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page
Controller: The Django framework and URL parsing

52) Why Django should be used for web-development?

It allows you to divide code modules into logical groups to make it flexible to change
To ease the website administration, it provides auto-generated web admin
It provides pre-packaged API for common user tasks
It gives you template system to define HTML template for your web page to avoid code duplication
It enables you to define what URL be for a given function
It enables you to separate business logic from the HTML
Everything is in python

53) Give an example how you can write a VIEW in Django?

Views are Django functions that take a request and return a response. To write a view in Django we take a simple example of “Guru99_home” which uses the template Guru99_home.html and uses the date-time module to tell us what the time is whenever the page is refreshed. The file we required to edit is called view.py, and it will be inside mysite/myapp/

Copy the below code into it and save the file
from datatime import datetime
from django.shortcuts import render
def home (request):
return render(request, ‘Guru99_home.html’, {‘right_now’: datetime.utcnow()})
Once you have determined the VIEW, you can uncomment this line in urls.py

url ( r ‘^$’ , ‘mysite.myapp.views.home’ , name ‘Guru99’),

The last step will reload your web app so that the changes are noticed by the web server.

54) Explain how you can setup static files in Django?

There are three main things required to set up static files in Django

Set STATIC_ROOT in settings.py
run manage.py collectsatic
set up a Static Files entry on the PythonAnywhere web tab

55) Mention what does the Django templates consists of?

The template is a simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the template is evaluated and tags (% tag %) that controls the logic of the template.

56) Explain the use of session framework in Django?

In Django, the session framework enables you to store and retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the receiving and sending of cookies. Session can be implemented through a piece of middleware.

57) Explain how you can use file based sessions?

To use file based session you have to set the SESSION_ENGINE settings to “django.contrib.sessions.backends.file”

58) Explain the migration in Django and how you can do in SQL?

Migration in Django is to make changes to your models like deleting a model, adding a field, etc. into your database schema. There are several commands you use to interact with migrations.

Migrate
Makemigrations
Sqlmigrate
To do the migration in SQL, you have to print the SQL statement for resetting sequences for a given app name.
django-admin.py sqlsequencreset
Use this command to generate SQL that will fix cases where a sequence is out sync with its automatically incremented field data.

59) Mention what command line can be used to load data into Django?

To load data into Django you have to use the command line Django-admin.py loaddata. The command line will searches the data and loads the contents of the named fixtures into the database.

60) Explain what does django-admin.py makemessages command is used for?

This command line executes over the entire source tree of the current directory and abstracts all the strings marked for translation. It makes a message file in the locale directory.

61) List out the inheritance styles in Django?

In Django, there is three possible inheritance styles

Abstract base classes: This style is used when you only wants parent’s class to hold information that you don’t want to type out for each child model
Multi-table Inheritance: This style is used If you are sub-classing an existing model and need each model to have its own database table
Proxy models: You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields

62) Mention what does the Django field class types?

Field class types determines

The database column type
The default HTML widget to avail while rendering a form field
The minimal validation requirements used in Django admin and in automatically generated forms