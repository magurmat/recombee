This is the solution for the homework assignment given by Recombee to Matus Magur.

To successfully run tests, DATABASE_URL in .env must be changed. "postgres" must be replaced with "localhost" and then
run command pytest test.py

In requests.txt are exported curl example requests for the created API.
In Insomnia_2024-03-17.json are exported Insomnia requests for the created API.

To run the application you need these commands:

1.  docker volume create --name=test_data
2.  docker-compose build
3.  docker-compose up

This should run server on port 5000