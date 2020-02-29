#craigslist_scraper.py

import csv
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#Here I'm creating a dictionary with each City's Craigslist gig pages. I've hardcoded the search queries
craigslist = {
    #Lakeland
    "Lakeland - Photographer":
        "https://lakeland.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Lakeland - Photograph":
        "https://lakeland.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Lakeland - Wedding":
        "https://lakeland.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Lakeland - Photography":
        "https://lakeland.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Lakeland - Photo":
        "https://lakeland.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Lakeland - Wedding Photography":
        "https://lakeland.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Orlando
    "Orlando - Photographer":
        "https://orlando.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Orlando - Photograph":
        "https://orlando.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Orlando - Wedding":
        "https://orlando.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Orlando - Photography":
        "https://orlando.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Orlando - Photo":
        "https://orlando.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Orlando - Wedding Photography":
        "https://orlando.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Tampa
    "Tampa - Photographer":
        "https://tampa.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Tampa - Photograph":
        "https://tampa.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Tampa - Wedding":
        "https://tampa.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Tampa - Photography":
        "https://tampa.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Tampa - Photo":
        "https://tampa.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Tampa - Wedding Photography":
        "https://tampa.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Tallahassee
    "Tallahassee - Photographer":
        "https://tallahassee.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Tallahassee - Photograph":
        "https://tallahassee.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Tallahassee - Wedding":
        "https://tallahassee.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Tallahassee - Photography":
        "https://tallahassee.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Tallahassee - Photo":
        "https://tallahassee.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Tallahassee - Wedding Photography":
        "https://tallahassee.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #St. Augustine
    "St.Augustine - Photographer":
        "https://staugustine.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "St.Augustine - Photograph":
        "https://staugustine.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "St.Augustine - Wedding":
        "https://staugustine.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "St.Augustine - Photography":
        "https://staugustine.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "St.Augustine - Photo":
        "https://staugustine.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "St.Augustine - Wedding Photography":
        "https://staugustine.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Space Coast
    "Space Coast - Photographer":
        "https://spacecoast.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Space Coast - Photograph":
        "https://spacecoast.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Space Coast - Wedding":
        "https://spacecoast.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Space Coast - Photography":
        "https://spacecoast.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Space Coast - Photo":
        "https://spacecoast.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Space Coast - Wedding Photography":
        "https://spacecoast.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Miami
    "Miami - Photographer":
        "https://miami.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Miami - Photograph":
        "https://miami.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Miami - Wedding":
        "https://miami.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Miami - Photography":
        "https://miami.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Miami - Photo":
        "https://miami.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Miami - Wedding Photography":
        "https://miami.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Sarasota
    "Sarasota - Photographer":
        "https://sarasota.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Sarasota - Photograph":
        "https://sarasota.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Sarasota - Wedding":
        "https://sarasota.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Sarasota - Photography":
        "https://sarasota.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Sarasota - Photo":
        "https://sarasota.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Sarasota - Wedding Photography":
        "https://sarasota.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Panama City
    "Panama City - Photographer":
        "https://panamacity.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Panama City - Photograph":
        "https://panamacity.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Panama City - Wedding":
        "https://panamacity.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Panama City - Photography":
        "https://panamacity.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Panama City - Photo":
        "https://panamacity.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Panama City - Wedding Photography":
        "https://panamacity.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Ocala
    "Ocala - Photographer":
        "https://ocala.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Ocala - Photograph":
        "https://ocala.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Ocala - Wedding":
        "https://ocala.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Ocala - Photography":
        "https://ocala.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Ocala - Photo":
        "https://ocala.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Ocala - Wedding Photography":
        "https://ocala.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Heartland
    "Heartland - Photographer":
        "https://cfl.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Heartland - Photograph":
        "https://cfl.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Heartland - Wedding":
        "https://cfl.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Heartland - Photography":
        "https://cfl.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Heartland - Photo":
        "https://cfl.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Heartland - Wedding Photography":
        "https://cfl.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Gainesville
    "Gainesville - Photographer":
        "https://gainesville.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Gainesville - Photograph":
        "https://gainesville.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Gainesville - Wedding":
        "https://gainesville.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Gainesville - Photography":
        "https://gainesville.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Gainesville - Photo":
        "https://gainesville.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Gainesville - Wedding Photography":
        "https://gainesville.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Fort Myers
    "Fort Myers - Photographer":
        "https://fortmyers.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Fort Myers - Photograph":
        "https://fortmyers.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Fort Myers - Wedding":
        "https://fortmyers.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Fort Myers - Photography":
        "https://fortmyers.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Fort Myers - Photo":
        "https://fortmyers.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Fort Myers - Wedding Photography":
        "https://fortmyers.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
    #Daytona
    "Daytona - Photographer":
        "https://daytona.craigslist.org/search/ggg?sort=date&is_paid=all&query=photographer",
    "Daytona - Photograph":
        "https://daytona.craigslist.org/search/ggg?query=photograph&sort=date&is_paid=all",
    "Daytona - Wedding":
        "https://daytona.craigslist.org/search/ggg?query=wedding&sort=date&is_paid=all",
    "Daytona - Photography":
        "https://daytona.craigslist.org/search/ggg?query=photography&sort=date&is_paid=all",
    "Daytona - Photo":
        "https://daytona.craigslist.org/search/ggg?query=photo&sort=date&is_paid=all",
    "Daytona - Wedding Photography":
        "https://daytona.craigslist.org/search/ggg?query=Wedding+Photographer&sort=date&is_paid=all",
}

filename = "craigslist_w_dupes.csv"
f = open(filename, "w")
writer = csv.writer(f)
headers = "Title, Link, Date \n"
f.write(headers)

for city in craigslist:
    response = requests.get(craigslist[city])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    posts = html_soup.find_all('li', class_='result-row')

    for post in posts:
        #Grabs date
        post_time = html_soup.find_all('time', class_='result-date')
        post_time_text = ",".join(t.text.strip() for t in post_time)

        #Grabbing the titles
        post_title = html_soup.find('a', class_='result-title hdrlnk')
        post_title_text = post_title.text

        #Post link
        post_link = post_title['href']

        print("Post Title: " + post_title_text)
        print("Post Link: " + post_link)
        print("Post Date: " + post_time_text)

        #f.write(post_title_text + "," + post_link_fixed + "," + post_time + "\n")
        writer.writerow([post_title_text,post_link,post_time_text])

f.close()

filename_out = "craigslist_w.o_dupes.csv"
df = pd.read_csv(filename, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(filename_out)

print("\n")
print("Scrape Complete")
