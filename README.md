# Crypto Currency Information Microservice
API used for data : Coincap 

Documentation explaining JSON file structure : https://docs.coincap.io/#ee30bea9-bb6b-469d-958a-d3e35d442d7a

## How To REQUEST Data
First, start up the server by running the python file. It should start up on 'http://localhost:3000'.
To request data make a simple HTTP GET request to the server. In the following example I use the *requests* python library.
```
requests.get('http://localhost:3000')
```
## How To RECEIVE Data
Store the response and use the json() method to create a JSON object from it. The json() method will also throw an error if it detects a JSON was not received.
```
response = requests.get('http://localhost:3000')
crypto_data = response.json()
```
Navigate and parse the data as you would a regular JSON file in python.
```
print(f'Name: {crypto_data["data"][0]["id"]}, Price USD: ${crypto_data["data"][0]["priceUsd"]}')
```
> Name: bitcoin, Price USD: $29519.1654108398628332

## UML Sequence Diagram
![image](https://user-images.githubusercontent.com/89743706/236617331-d45f06b1-3d46-4a7f-98e5-feddb7333bfd.png)
