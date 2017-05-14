from bs4 import BeautifulSoup
import wikipedia

def printlist(l1):
    for l in l1:
        print(l)

def find_section(page, title):
    res = page.section(title)
    if res is None:
        res = page.section(title + 'Edit')
    return res

def filmlist(year):
    bw= wikipedia.page("List of Bollywood films of "+year)
    
    soup= BeautifulSoup(bw.html(),"lxml")

    tables = soup.find_all("table", { "class" : "wikitable" })
    #Change 'wikitable' to 'wikitable sortable' for post 2011 films    
    links=[]
    titles=[]

    for table in tables:
        i_val=table.find_all("i")
        for i in i_val:
            try:
                url=(i.find('a',href=True)['href'])
                if url[:3]!='/w/':
                    links.append("https://en.wikipedia.org"+url)
                    titles.append(i.find('a',href=True)['title'])
                    #print("https://en.wikipedia.org"+url)
            except:
                pass

    printlist(titles)
    return titles

def filmwikipages(titles):
    pages=[]

    for title in titles:
        try:
            pages.append(wikipedia.page(title))
            print("Pagified "+title)
        except:
            print("Failed "+title)
    return pages

def writeplot(pages):
    f=open('plots2006.txt', 'w') #Change file name as needed

    for page in pages:
        if "Plot" in page.sections:
            ttl=str(page.title)
            print("Plot exists for "+ttl)
            plt=find_section(page,"Plot")
            if plt!=None :
                print("Plotted "+ttl)
                f.write(plt)
                f.write("\n-----------------------------------------------------------\n")
            
    f.close()
    
pages=filmwikipages(filmlist("2006"))
writeplot(pages)
