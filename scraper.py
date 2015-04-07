from bs4 import BeautifulSoup as soup
import urllib
import csv

# List of an entire team. Will exclude unicode syntax.
student_athletes = []

# List of table row headers without HTML syntax.
clean_row_labels = []

def main():
    global soup

    url = "http://www.hurricanesports.com/SportSelect.dbml?&DB_OEM_ID=28700&SPID=103764&SPSID=658379" # Soccer

    # Give scraper the URL. Makes soup.
    get_html(url)

    # Scrape page for student-athlete info. Put in list of lists.
    scrape(soup)

    # Converts heights to inches.
    # Google Spreadsheets does annoying thing where it converts
    #   heights to dates, so converting to inches in order to
    #   avoid issue.
    height_to_inches()

    # Convert list of lists into csv
    list_to_csv()

def get_html(url):
    '''
    Given a URL, this method creates the object needed for soup.
    '''
    global soup

    # Open url
    html = urllib.urlopen(url)

    # Give html to BeautifulSoup
    soup = soup(html)

def scrape(soup):
    '''
    Given the object, soup will find the student-athlete info.
    A list of dictionaries will be created. Each dictionary represents
    a student-athlete.
    '''
    global clean_row_labels

    # Look for td with class "subhdr."
    # This is where the table's headers are.
    header_html = soup.find_all("td", {"class" : "subhdr", "align" : ""})

    # Fills clean_row_labels with HTML-less text.
    for item in header_html:
        # Encode converts unicode values to ASCII.
        # If unable, the unicode value is ignored.
        clean_row_labels.append(item.get_text(strip=True).encode('ascii', 'ignore'))

    # Appends "Hometown" because HTML for "Hometown" is different from rest of row labels.
    clean_row_labels.append("Hometown (Prev School)")

    # Look for td with classes "even" and "odd."
    # This is where each player is in table.
    odd_players = soup.find_all("td", {"class" : "odd"})
    even_players = soup.find_all("td", {"class" : "even"})
    team = odd_players + even_players

    # Cleans up data scraped from website by removing HTML syntax.
    get_team_info(team)

def get_team_info(team):
    '''
    Gets players' information from lists of html tags.
    '''
    global student_athletes
    global clean_row_labels
    player = []
    counter = 0

    # Makes list of lists. Each list item is a player's full info.
    for item in team:
        # Encode converts unicode values to ASCII.
        # If unable, the unicode value is ignored.
        player.append(item.get_text(strip=True).encode('ascii', 'ignore'))
        counter = counter + 1

        # Once all of a single player's info is added, append player list to student_athletes list.
        # Then, make new list for next player and reset counter.
        if (counter % len(clean_row_labels) == 0):
            student_athletes.append(player)
            player = []
            counter = 0

    #print(clean_row_labels)
    #print(student_athletes)

def height_to_inches():
    global student_athletes
    global clean_row_labels

    # Gets index of height column. HEAVILY assumes that a height column exists
    #   in the "Ht." format.
    height_index = clean_row_labels.index("Ht.")


    # For loop visits each player list in student_athletes
    for player in student_athletes:
        feet, inches = get_num_from_string(player[height_index])
        pass

def get_num_from_string(height_string):
    feet = 0
    inches = 0

    return feet, inches

def list_to_csv():
    '''
    Given the list of dictionaries, this method will convert the list
    into a csv file. The file will be stored in a folder within the
    same directory.
    '''
    global clean_row_labels
    global student_athletes

    myfile = open("csv-files/soccer.csv", 'wb')
    writer = csv.writer(myfile)
    writer.writerow(clean_row_labels)
    writer.writerows(student_athletes)


if (__name__ == '__main__'):
    main()
