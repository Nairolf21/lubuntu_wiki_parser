if __name__ == '__main__':
    try:
        f = open('wiki.ubuntu.com_Lubuntu.html', 'rb')
        html_doc = f.read()
        print(html_doc)
    except Exception, e:
        print("error", e)
