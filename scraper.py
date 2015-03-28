from bs4 import BeautifulSoup as soup
import urllib
import csv

def main():
    global soup

    url = "http://www.hurricanesports.com/SportSelect.dbml?&DB_OEM_ID=28700&SPID=103777&SPSID=658436" # Men's basketball

    # Give scraper the URL
    get_html(url)

    # Scrape page for student-athlete info. Put in list of dictionaries
    list_of_dict = scrape(soup)

    # Convert list of dictionaries into csv
    csv_file = list_to_csv(list_of_dict)

def get_html(url):
    '''
    Given a URL, this method creates the object needed for soup.
    '''
    global soup

    # Open url
    html = urllib.urlopen(url)

    # Give html to BeautifulSoup
    soup = soup(html)

    print("Got the HTML!")

def scrape(soup):
    '''
    Given the object, soup will find the student-athlete info.
    A list of dictionaries will be created. Each dictionary represents
    a student-athlete.
    '''
    student_athletes = []

    # Look for td with class "subhdr."
    # This is where the table's headers are.
    #messy_list = soup.find_all("td", {"class" : "subhdr", "align" : ""})


    # Look for td with classes "even" and "odd."
    # This is where each player is in table.
    print(soup.find_all("td", {"class" : "odd"}))
    print(soup.find_all("td", {"class" : "even"}))

    print("Scraped!")

def list_to_csv(list_of_dict):
    '''
    Given the list of dictionaries, this method will convert the list
    into a csv file. The file will be stored in a folder within the
    same directory.
    '''
    print("Converted list into a csv!")


if (__name__ == '__main__'):
    main()
