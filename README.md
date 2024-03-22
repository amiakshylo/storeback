<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">STOREBACK</h1>
</p>
<p align="center">
    <em>Empowering seamless app deployments and network readiness.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/amiakshylo/storeback?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/amiakshylo/storeback?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/amiakshylo/storeback?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/amiakshylo/storeback?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The Storeback project is an open-source e-commerce platform with robust features for product management, user authentication, and order processing. It integrates Django REST framework, Celery for task management, and Redis for caching, enhancing scalability and performance. Core functionalities include CRUD operations, custom permissions, and serializers for entities like products, customers, and orders. With a modular design and clean architecture, Storeback streamlines development and deployment processes, making it a valuable solution for building efficient online stores.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Dockerized architecture using Docker Compose for services like PostgreSQL, Redis, and Celery. Clear separation of concerns with serializers, views, and models. Follows Django best practices. Supports async tasks with Celery. |
| 🔩 | **Code Quality**  | Good code quality maintained with PEP8 standards. Comprehensive test coverage ensuring reliability and maintainability. Consistent code style and structure promoting readability and collaboration. |
| 📄 | **Documentation** | Well-documented codebase with clear explanations for serializers, views, models, and tasks. README, comments, and docstrings provide guidance for setup, usage, and contribution. API documentation for endpoints and permissions. |
| 🔌 | **Integrations**  | Integrates with Django REST framework, Celery for async tasks, JWT authentication with djoser, and Redis for caching. Seamless communication across services like MySQL and SMTP4Dev. |
| 🧩 | **Modularity**    | Highly modular codebase with separate modules for core functionality, likes, tags, and playground. Reusable components like serializers, views, models, and tasks promote scalability and maintainability. |
| 🧪 | **Testing**       | Utilizes pytest-django for testing models and views. Implements Locust for load testing. Ensures core functionality validation and performance assessment. |
| ⚡️  | **Performance**   | Efficient resource usage and speed demonstrated with pagination settings, caching with Redis, and asynchronous task management using Celery. Optimized database queries and API responses for improved performance. |
| 🛡️ | **Security**      | Secure data access control with custom permissions and JWT authentication. Ensures protection against CSRF, SQL injection, and unauthorized access. Follows Django security best practices. |
| 📦 | **Dependencies**  | Key dependencies include Django, djangorestframework, Celery, and djoser. Additional libraries like pillow for image handling and psycopg2 for PostgreSQL support. |
| 🚀 | **Scalability**   | Scalable architecture supporting increased traffic with async task processing, database optimization, and modular design. Easily configurable for horizontal scaling and performance enhancement. |

---

##  Repository Structure

```sh
└── storeback/
    ├── Dockerfile
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── build.sh
    ├── core
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializers.py
    │   ├── signals
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── docker-compose.yml
    ├── docker-entrypoint.sh
    ├── likes
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── locustfiles
    │   └── browse_product.py
    ├── manage.py
    ├── playground
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── static
    │   ├── tasks.py
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── pytest.ini
    ├── store
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── filters.py
    │   ├── management
    │   ├── migrations
    │   ├── models.py
    │   ├── pagination.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── signals
    │   ├── static
    │   ├── tests
    │   ├── tests.py
    │   ├── urls.py
    │   ├── validators.py
    │   └── views.py
    ├── storefront
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── celery.py
    │   ├── settings
    │   ├── urls.py
    │   └── wsgi.py
    ├── tags
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── wait-for-it.sh
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                      |
| ---                                                                                              | ---                                                                                                                                                                                                                                                          |
| [docker-compose.yml](https://github.com/amiakshylo/storeback/blob/master/docker-compose.yml)     | Defines services, dependencies, and configurations for local development environment with Docker Compose. Orchestrates PostgreSQL, Redis, Celery, and SMTP4Dev services, enabling seamless communication and resource allocation across containers.          |
| [wait-for-it.sh](https://github.com/amiakshylo/storeback/blob/master/wait-for-it.sh)             | Enables testing TCP host/port availability. Parses command-line arguments for host, port, timeout, and a subcommand to execute post-test. Handles timeouts and strict mode for subprocess execution. Helpful for ensuring network service readiness.         |
| [manage.py](https://github.com/amiakshylo/storeback/blob/master/manage.py)                       | Executes administrative tasks for Django, setting up the environment for the storefront app. Handles imports and launches Django command-line operations.                                                                                                    |
| [build.sh](https://github.com/amiakshylo/storeback/blob/master/build.sh)                         | Installs dependencies, collects static files, and applies migrations for the Storeback Django project during build process.                                                                                                                                  |
| [Pipfile](https://github.com/amiakshylo/storeback/blob/master/Pipfile)                           | Specifies Python dependencies using the Pipfile to manage packages like Django, Django REST framework, Celery, and more for the project. Essential for maintaining a robust and functional web application.                                                  |
| [docker-entrypoint.sh](https://github.com/amiakshylo/storeback/blob/master/docker-entrypoint.sh) | Executes database migrations and launches the server on a specified address and port for the Storeback repository, facilitating seamless application updates and service provision.                                                                          |
| [Dockerfile](https://github.com/amiakshylo/storeback/blob/master/Dockerfile)                     | Sets up Python environment with dependencies and MySQL client library. Prepares app directory, installs pipenv, and copies app files. Exposes port 8000 in the Docker container. Contributing to a streamlined setup and deployment for the main repository. |

</details>

<details closed><summary>store</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                    |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                        |
| [serializers.py](https://github.com/amiakshylo/storeback/blob/master/store/serializers.py) | Serializers for products, collections, reviews, carts, addresses, customers, and orders. Manages validation, creation, and updates. Converts data between complex types for API interaction within the e-commerce system.                                                                  |
| [pagination.py](https://github.com/amiakshylo/storeback/blob/master/store/pagination.py)   | Implements default pagination settings using PageNumberPagination from rest_framework.                                                                                                                                                                                                     |
| [permissions.py](https://github.com/amiakshylo/storeback/blob/master/store/permissions.py) | Implements custom permissions for admin access and read-only views, extends DjangoModelPermissions, and provides a permission check for canceling orders within the store application.                                                                                                     |
| [urls.py](https://github.com/amiakshylo/storeback/blob/master/store/urls.py)               | Defines nested routers for products, collections, customers, carts, images, and addresses, efficiently managing viewsets and URL patterns for each category in the Django-based storefront API.                                                                                            |
| [validators.py](https://github.com/amiakshylo/storeback/blob/master/store/validators.py)   | Imposes validation for file sizes within the store module, ensuring file size adherence to a predefined limit.                                                                                                                                                                             |
| [views.py](https://github.com/amiakshylo/storeback/blob/master/store/views.py)             | Defines view sets for various models including products, carts, addresses, customers, reviews, collections, and orders in the REST API. Manages CRUD operations, permissions, filters, and serializers for each model based on user roles and context.                                     |
| [tests.py](https://github.com/amiakshylo/storeback/blob/master/store/tests.py)             | Tests models and views of store app. Validates core functionality ensuring proper data handling. Key component in maintaining code quality and reliability within larger project architecture.                                                                                             |
| [admin.py](https://github.com/amiakshylo/storeback/blob/master/store/admin.py)             | Defines custom Django admin interfaces for Orders, Products, Collections, and Customers. Enhances usability by providing inline editing, filtering, actions, and display customizations for efficient management of store-related entities. Supports visual styling through CSS inclusion. |
| [filters.py](https://github.com/amiakshylo/storeback/blob/master/store/filters.py)         | Enables filtering of Product and Review models using specific fields, maintaining modular and reusable filter logic for the store repositorys Django application.                                                                                                                          |
| [models.py](https://github.com/amiakshylo/storeback/blob/master/store/models.py)           | Defines models for products, orders, customers, reviews, cart items, and addresses. Includes fields for product details, promotions, orders, and customer information. Establishes relationships among entities for an e-commerce platform.                                                |
| [apps.py](https://github.com/amiakshylo/storeback/blob/master/store/apps.py)               | Registers signals handlers upon app initialization in the StoreConfig class within the store/apps.py file, enhancing the repositorys Django architecture by managing app configuration and signal events.                                                                                  |

</details>

<details closed><summary>store.management.commands</summary>

| File                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                            |
| [seed.sql](https://github.com/amiakshylo/storeback/blob/master/store/management/commands/seed.sql)                                                 | This code file within the `core` module of the repository is responsible for defining the essential data models and their corresponding serializers. By encapsulating this core functionality, the code file plays a crucial role in structuring and managing the data layer of the application. It ensures that data can be efficiently stored, retrieved, and manipulated within the system. |
| [createsuperuser_if_not_exists.py](https://github.com/amiakshylo/storeback/blob/master/store/management/commands/createsuperuser_if_not_exists.py) | Ensures superuser creation if absent in Django app. Uses `get_user_model` to check, then creates if needed, displaying success or existing status. Handles IntegrityError gracefully.                                                                                                                                                                                                          |
| [seed_db.py](https://github.com/amiakshylo/storeback/blob/master/store/management/commands/seed_db.py)                                             | Populates database with collections and products via executing SQL script.                                                                                                                                                                                                                                                                                                                     |

</details>

<details closed><summary>store.signals</summary>

| File                                                                                         | Summary                                                                                                                                                                                    |
| ---                                                                                          | ---                                                                                                                                                                                        |
| [handlers.py](https://github.com/amiakshylo/storeback/blob/master/store/signals/handlers.py) | Defines a signal handler creating a Customer instance for a new user upon post_save event. Uses the AUTH_USER_MODEL from the settings and connects to the Customer model in the store app. |

</details>

<details closed><summary>likes</summary>

| File                                                                             | Summary                                                                                                                                                                                                     |
| ---                                                                              | ---                                                                                                                                                                                                         |
| [views.py](https://github.com/amiakshylo/storeback/blob/master/likes/views.py)   | Implements view functions for managing user likes within the Django web framework. Facilitates rendering of web pages and handling user interactions related to liking specific content in the application. |
| [tests.py](https://github.com/amiakshylo/storeback/blob/master/likes/tests.py)   | Tests product liking functionality ensuring proper implementation and behavior within the storeback system.                                                                                                 |
| [admin.py](https://github.com/amiakshylo/storeback/blob/master/likes/admin.py)   | Registers models with the Django admin panel.                                                                                                                                                               |
| [models.py](https://github.com/amiakshylo/storeback/blob/master/likes/models.py) | Defines models for user likes with dynamic relationships using Django ORM.Allows any object to be liked with a generic relationship to content type.                                                        |
| [apps.py](https://github.com/amiakshylo/storeback/blob/master/likes/apps.py)     | Defines the configuration for the likes app, specifying default database field and app name within the Django project structure.                                                                            |

</details>

<details closed><summary>storefront</summary>

| File                                                                                  | Summary                                                                                                                                                                                                         |
| ---                                                                                   | ---                                                                                                                                                                                                             |
| [wsgi.py](https://github.com/amiakshylo/storeback/blob/master/storefront/wsgi.py)     | Sets Django settings and initializes the WSGI application for the storefront.                                                                                                                                   |
| [urls.py](https://github.com/amiakshylo/storeback/blob/master/storefront/urls.py)     | Defines URL patterns for admin, playground, store, and core modules. Integrates debug_toolbar, djoser for authentication, and silk for profiling in debug mode. Handles serving media files during development. |
| [celery.py](https://github.com/amiakshylo/storeback/blob/master/storefront/celery.py) | Defines and configures Celery for task management in the storefront Django application. Automatically discovers and imports tasks using Django settings, enhancing scalability and asynchronous capabilities.   |
| [asgi.py](https://github.com/amiakshylo/storeback/blob/master/storefront/asgi.py)     | Initializes Django ASGI application with the specified settings module for the storefront within the repository architecture.                                                                                   |

</details>

<details closed><summary>storefront.settings</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                           |
| ---                                                                                            | ---                                                                                                                                                                                                                                               |
| [dev.py](https://github.com/amiakshylo/storeback/blob/master/storefront/settings/dev.py)       | Defines development settings for the storefront, specifying database and cache configurations, along with settings for Celery and email functionality. Sets debug mode to true and defines allowed hosts for the Django application.              |
| [prod.py](https://github.com/amiakshylo/storeback/blob/master/storefront/settings/prod.py)     | Manages production settings, imports common settings, sets SECRET_KEY, and disables DEBUG mode.-Configures the default database using dj_database_url with specified connection details.                                                          |
| [common.py](https://github.com/amiakshylo/storeback/blob/master/storefront/settings/common.py) | Defines Django settings for the storefront application. Configures middleware, authentication, templates, and logging. Specifies root URLs and paths for static and media files. Integrates REST framework, JWT authentication, and Celery tasks. |

</details>

<details closed><summary>locustfiles</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                    |
| ---                                                                                                    | ---                                                                                                                                                                                                                                        |
| [browse_product.py](https://github.com/amiakshylo/storeback/blob/master/locustfiles/browse_product.py) | Implements Locust load testing tasks for browsing products, viewing product details, and adding items to the cart in the e-commerce store. Includes simulated user interactions with different endpoints to assess performance under load. |

</details>

<details closed><summary>core</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                   |
| ---                                                                                       | ---                                                                                                                                                                                                                                       |
| [serializers.py](https://github.com/amiakshylo/storeback/blob/master/core/serializers.py) | Enhances user and authentication data serialization in the `core` module using extended fields for user creation and information display, leveraging `djoser` integrations for efficient user management.                                 |
| [urls.py](https://github.com/amiakshylo/storeback/blob/master/core/urls.py)               | Defines URL configuration for core app, directing to the index HTML template using Djangos path function and TemplateView class.                                                                                                          |
| [views.py](https://github.com/amiakshylo/storeback/blob/master/core/views.py)             | Defines core views for rendering in the Django framework.                                                                                                                                                                                 |
| [tests.py](https://github.com/amiakshylo/storeback/blob/master/core/tests.py)             | Verifies core functionalities through test cases in Django, ensuring proper system behavior.                                                                                                                                              |
| [admin.py](https://github.com/amiakshylo/storeback/blob/master/core/admin.py)             | Enhances User and Product administration interfaces by customizing fieldsets and inlines to improve user and product management. Maintains app independence through custom_store and generic relations for child editing in Django admin. |
| [models.py](https://github.com/amiakshylo/storeback/blob/master/core/models.py)           | Defines a custom User model in the core module, extending Djangos AbstractUser for the parent repository. Enforces unique email field constraint.                                                                                         |
| [apps.py](https://github.com/amiakshylo/storeback/blob/master/core/apps.py)               | Registers signals handlers with Django AppConfig in the core module for event-driven operations.                                                                                                                                          |

</details>

<details closed><summary>core.templates.core</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                          |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                              |
| [index.html](https://github.com/amiakshylo/storeback/blob/master/core/templates/core/index.html) | Presents a visually appealing website layout for showcasing portfolio items with professional descriptions. Incorporates parallax effects and contact form for engagement. Designed to promote user interaction and provide information about the owners professional expertise. |

</details>

<details closed><summary>core.signals</summary>

| File                                                                                        | Summary                                                                                                                                      |
| ---                                                                                         | ---                                                                                                                                          |
| [hendlers.py](https://github.com/amiakshylo/storeback/blob/master/core/signals/hendlers.py) | Notifies on order creation by printing order information. Handled through signal receiver importing order_created signal from store.signals. |

</details>

<details closed><summary>tags</summary>

| File                                                                            | Summary                                                                                                                                                                                                                                       |
| ---                                                                             | ---                                                                                                                                                                                                                                           |
| [views.py](https://github.com/amiakshylo/storeback/blob/master/tags/views.py)   | Implements views for rendering web pages using Djangos render function in the tags' app.                                                                                                                                                      |
| [tests.py](https://github.com/amiakshylo/storeback/blob/master/tags/tests.py)   | Verifies tag functionalities. Tests ensure reliable tag creation, modification, and deletion within the stores ecosystem, enhancing product categorization and organization.                                                                  |
| [admin.py](https://github.com/amiakshylo/storeback/blob/master/tags/admin.py)   | Defines TagAdmin class for Django admin panel with search functionality based on the label field for Tag model.                                                                                                                               |
| [models.py](https://github.com/amiakshylo/storeback/blob/master/tags/models.py) | Defines a tagging system with models for storing tags and associating them with content objects. Provides a manager for retrieving tags for a specific object type and ID. Allows for generic foreign key relationships with content objects. |
| [apps.py](https://github.com/amiakshylo/storeback/blob/master/tags/apps.py)     | Defines configuration for tags app, specifying default database field.                                                                                                                                                                        |

</details>

<details closed><summary>playground</summary>

| File                                                                                | Summary                                                                                                                                                                                                       |
| ---                                                                                 | ---                                                                                                                                                                                                           |
| [urls.py](https://github.com/amiakshylo/storeback/blob/master/playground/urls.py)   | Defines URL patterns for the Hello endpoint in the playground app, connecting the endpoint to the corresponding view.                                                                                         |
| [views.py](https://github.com/amiakshylo/storeback/blob/master/playground/views.py) | Implements APIView to fetch data from httpbin.org and logs the process.                                                                                                                                       |
| [tasks.py](https://github.com/amiakshylo/storeback/blob/master/playground/tasks.py) | Enables asynchronous email notifications to customers. Sends 10k emails with a custom message, ensuring successful delivery. Supports the repositorys architecture by enhancing customer engagement features. |
| [tests.py](https://github.com/amiakshylo/storeback/blob/master/playground/tests.py) | Verifies functionality of Django application components.                                                                                                                                                      |
| [apps.py](https://github.com/amiakshylo/storeback/blob/master/playground/apps.py)   | Defines the configuration for the playground app in the Django project, specifying the default database field and app name.                                                                                   |

</details>

<details closed><summary>playground.templates</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                |
| ---                                                                                               | ---                                                                                                                                                                                                                    |
| [hello.html](https://github.com/amiakshylo/storeback/blob/master/playground/templates/hello.html) | Renders dynamic content based on user input, displaying a greeting with a customizable message. Supports iteration through a list of customers, enhancing user experience in the playground section of the repository. |

</details>

<details closed><summary>playground.templates.emails</summary>

| File                                                                                                     | Summary                                                                                                   |
| ---                                                                                                      | ---                                                                                                       |
| [hello.html](https://github.com/amiakshylo/storeback/blob/master/playground/templates/emails/hello.html) | Defines email template blocks for subject and body customization, facilitating dynamic content insertion. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.10.12`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the storeback repository:
>
> ```console
> $ git clone https://github.com/amiakshylo/storeback
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd storeback
> ```
>
> 3. Install the dependencies:
> ```console
> $ pipenv install
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run storeback using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```






