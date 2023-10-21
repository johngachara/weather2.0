from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):
    if 'location' in request.POST:
        location = request.POST['location']
    else:
        location = 'Nairobi'
    today = datetime.date.today()
    current_datetime = datetime.datetime.now()
    day = current_datetime.day
    URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
    key = 'FQUQ9VQWFS6QJWJ9RYG6NGKJC'
    params = {"location": location ,"key":key,"date": today,"period":"next4days","unitGroup":"metric","include":['days','events','current']}
    response = requests.get(URL,params).json()
    addr = response['resolvedAddress']
    precip = response['days'][0]['precipprob']
    wind = response['days'][0]['windspeed']
    humidity = response['days'][0]['humidity']
    temperature = response['days'][0]['temp']
    future = response['days'][1]['temp']
    future_two = response['days'][2]['temp']
    future_three = response['days'][3]['temp']
    future_four = response['days'][4]['temp']
    descr = response['days'][0]['description']
    return render(request,'home.html',{"wind":wind,"humidity":humidity,"temp":temperature,"response":response,"address":addr,"today":today,"day": day,"description":descr,"day1":future,"day2":future_two,"day3":future_three,"day4":future_four,"precipitation":precip})