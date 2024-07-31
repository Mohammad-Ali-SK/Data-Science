from pymongo import MongoClient
import requests

def data(city):
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=de0146d4145585515d2bba51679e6bc5").json()
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    presure = data['main']['pressure']
    print(f"City : {city}\n Weather : {weather} \n Temp : {temp} \n Pressure : {presure}")

# Monogo Part-1
client = MongoClient("mongodb+srv://ytmanager:ytmanager@machinelearning.hbo9rte.mongodb.net/")
db = client['Yt_Manager']
collection  = db['yt_manager']


def add_data(roll,name,class_no):
    pass

def show_data():
    pass


def update_data(roll,name,class_no):
    pass

def delete_data(rool):
    pass


def main():
    while True:
        print("\n Student Data || Chose your Option.")
        print("\n1. Add student.")
        print("\n2. Show all Student.")
        print("\n4. Update Student data.")
        print("\n5. Delete Student data.")
        
        choice = int(input("Enter your choice : "))
        
        match choice:
            case 1:
                add_data()
            case 2:
                show_data()