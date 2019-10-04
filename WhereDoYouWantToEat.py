#The goal of this program is to randomly select a place to eat or hang out
#Ultimately want to expand to take into account number of people, location, family/friends, cuisine
#Would be nice to eventually output a Yelp link and be based off of your location
#Include to-go options?
#Yelp API tutorial: https://python.gotrained.com/yelp-fusion-api-tutorial/

#Import libraries to use for this program
import random
import requests
import json

#Yelp API
api_key = 'YUKgPwxqs5mnCzcqhCJ530soX7QuT5ch_Qe0d5Qp1w2qyzMOz3E4Io6mfxvsvj0Mlgby35-NJJ8qAVpyMDZLd9UwU99haXLbDANa4TCrIG5MY8B0jSlB1aKQ5OeWXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'

meal = ""
while  meal.upper() != 'Q': 
    meal = input("Please input whether you want: \n L - lunch\n D - dinner\n B - boba\n E - dessert\n Q - Quit\n\n I want to eat: ") #User selects option
    location = input("Please input what city you are in:")
    upperMeal = meal.upper() #Make input uppercase so that when using if and elif, easy to identify
    lunchDict = {"Uroko Cafe", "The Marketplace", "Aloha Hawaiian BBQ", "University Town Center"} #Lunch places
    dinnerDict = {"Cava Grill", "Panini Kebab Grill", "Souplantation"} #Dinner places
    bobaDict = {"7 Leaves", "Tastea", "Omomo", "HNTea"} #Boba places
    dessertDict = {"Yogurtland", "Saffron and Rose", "Fill Bakeshop and Creamery" }

    if (upperMeal == "LUNCH" or upperMeal == "L"):
        lunch = (random.choice(list(lunchDict))) #Randomly selects from the lunchDict
        params = {'term':lunch,'location':location} #Sets parameters to randomly selected business and searches based off location
    elif (upperMeal == "DINNER" or upperMeal == "D"):
        dinner = (random.choice(list(dinnerDict))) #Randomly selects from the dinnerDict
        params = {'term':dinner,'location':location}
    elif (upperMeal == "BOBA" or upperMeal == "B"):
        boba = (random.choice(list(bobaDict))) #Randomly selects from the bobaDict
        params = {'term':boba,'location':location}
    elif (upperMeal == "DESSERT" or upperMeal == "E"):
        dessert = (random.choice(list(dessertDict))) #Randomly selects from the dessertDict
        params = {'term':dessert,'location':location}
    elif (upperMeal == "QUIT" or upperMeal == "Q"):
        break
    else:
        print("Please Enter a Valid Option")
        break
    
    req=requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]
    print(businesses[0]["name"]) #Name of first business on Yelp search
    print(businesses[0]["url"]) #URL of first business on Yelp search


