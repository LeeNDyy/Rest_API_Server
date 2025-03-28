# Rest_API_server
![Static Badge](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Static Badge](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Static Badge](https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=for-the-badge)

# Description
Hello, my name is Vasilkov Arseniy, in this project a Rest API server is being implemented. 
Rest API server written in Python using uvicorn and Fastapi. 
The project was developed as a laboratory work on the subject "Microservice architecture" by a 2nd year student of the specialty 09.02.01 "Computer systems and complexes".

# Launch instructions
Launch using Docker
Rebuild and launch containers using the command:
```
docker compose up --build
```
This command allows you to collect all containers and immediately launch them for further work

After that you will have 4 containers, 3 with the same application and nginx, to check the work
you need to follow the website link that will appear in the terminal after starting the project: 

Open one of the /app/routers/contact.py or /app/routers/group.py files. At the very end of the code, there will be a long request text. You can remove the comments and watch the changes on the page or in the VS Code console.

# Postman
You can also chek the work in postman:
In this project there are two objects: contect, group and for each of them queries are written: POST, GET, PUT, DELETE
To check the work, go to postman and write request. Example: http://0.0.0.0.6081/api/v1/contact/, it's post request for contact.
