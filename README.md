# AddressAPI_sqlite_swaggerdocrdoc


THIS IS A REST API USING FASIAPI 


to run  the  api : 
cmd : - [  python -m uvicorn main:app --reload]


to check the api in swaggerdoc :
http://127.0.0.1:8000/docs

libraries used :

 command : pip install fastapi uvicorn aiosqlite databases pydantic requets SQLAlchemy
 
- fastapi
- uvicorn
- aiosqlite
- databases
- pydantic
- requests
- SQLAlchemy

  op of [ pip freeze > requiremt.txt ]

aiosqlite==0.20.0
annotated-types==0.6.0
anyio==4.3.0
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
databases==0.8.0
fastapi==0.109.2
greenlet==3.0.3
h11==0.14.0
idna==3.6
pydantic==2.6.1
pydantic_core==2.16.2
requests==2.31.0
sniffio==1.3.0
SQLAlchemy==1.4.51
starlette==0.36.3
typing_extensions==4.9.0
urllib3==2.2.1
uvicorn==0.27.1


you can also make a virtual env for this project
cmd : - [ python -m venv denv  ] 
to activate : .\denv\Scripts\activate   

you can test in postman also:
http://127.0.0.1:8000/addressdetails/

[
    {
        "id": 1,
        "name": "string",
        "country": "string",
        "phone": 0
    },
    {
        "id": 2,
        "name": "Debishree Nayak",
        "country": "India",
        "phone": 90786543125
    },
    {
        "id": 3,
        "name": "Krisha Sundar",
        "country": "India",
        "phone": 9912345231
    },
    {
        "id": 4,
        "name": "Krisha Sundar",
        "country": "India",
        "phone": 9912345231
    },
    {
        "id": 5,
        "name": "Radhika Mohanan",
        "country": "India",
        "phone": 7876031234
    }



happy coding


   

  
