from bs4 import BeautifulSoup


if __name__ == '__main__':
    soup = BeautifulSoup(open('wiki.ubuntu.com_Lubuntu.html'), 'html.parser')
    print(soup.prettify())
