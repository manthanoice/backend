# Codemonk Backend Developer Intern Project

This is the backend project I built as a part of the Codemonk internship program.

### Installation

To run this project on your local machine, you need to follow these steps:

- Open the command line in your PC.
- Navigate to the project directory.
- Run the following command to start the Docker containers:

    ```
    docker-compose up
    ```

    This command will start the Django server, the PostgreSQL database.

- Once the containers are up and running, you can access the API using the following URL:

    ```
    http://127.0.0.1:8000/
    ```

    You can also access the Django admin panel using the following URL:

    ```
    http://127.0.0.1:8000/admin/
    ```

### API Documentation

The API documentation is available in the [Postman](https://www.postman.com/) collection. You can access it using the following link:

[https://documenter.getpostman.com/view/21242095/2s93eWzsu9](https://documenter.getpostman.com/view/21242095/2s93eWzsu9)

### User Authentication

The project comes with a predefined superuser account, which you can use for testing purposes. You can access the Django admin panel using the following credentials:

- Username: `admin@example.com`
- Password: `password123`

If you want to create a new superuser, you can use the following command:

    
    python manage.py createsuperuser
    
    
### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).