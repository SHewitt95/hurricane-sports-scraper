from bs4 import BeautifulSoup as soup
import urllib

def main():
    # Give scraper the URL
    get_url()
    # Scrape page for student-athlete info. Put in list of dictionaries
    scrape()
    # Convert list of dictionaries into csv
    list_to_csv()

def get_url():
    '''
    Given a URL, this method creates the object needed for soup.
    '''
    print("Got the URL!")

def scrape():
    '''
    Given the object, soup will find the student-athlete info.
    A list of dictionaries will be created. Each dictionary represents
    a student-athlete.
    '''
    print("Scraped!")

def list_to_csv():
    '''
    Given the list of dictionaries, this method will convert the list
    into a csv file. The file will be stored in a folder within the
    same directory.
    '''
    print("Converted list into a csv!")


if (__name__ == '__main__'):
    main()
