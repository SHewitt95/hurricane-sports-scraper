from bs4 import BeautifulSoup as soup
import urllib
import csv

def main():
    url = ""

    # Give scraper the URL
    url_html = get_url(url)

    # Scrape page for student-athlete info. Put in list of dictionaries
    list_of_dict = scrape(url_html)

    # Convert list of dictionaries into csv
    csv_file = list_to_csv(list_of_dict)

def get_url(url):
    '''
    Given a URL, this method creates the object needed for soup.
    '''
    print("Got the URL!")

def scrape(url_html):
    '''
    Given the object, soup will find the student-athlete info.
    A list of dictionaries will be created. Each dictionary represents
    a student-athlete.
    '''
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
