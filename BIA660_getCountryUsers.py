"""
This script retrieves the urls that correspond to user profiles on freelancer.com
Here is an example url:
    https://www.freelancer.com/u/zhj11651.html
    
On the website, freelancers are viewed in pages (10 per page). For example, 
page 1 is https://www.freelancer.com/freelancers/skills/all/1
page 2 is https://www.freelancer.com/freelancers/skills/all/2
etc.

Open a web browser (e.g. chrome) and go to page 1: https://www.freelancer.com/freelancers/skills/all/1.
Right click on the username of the 1st freelancer and click 'Copy Link Address'. If you do this for username 'calciustech',
the link https://www.freelancer.com/u/calciustech.html is copied. This is the link to the person's full profile. We want to get
all this link of multiple freelancers and store them in a file.

Our scipct will browse page by page, and retrieve the links of the 10 freelancers in each page.
"""

#import the two libraries we will be using in this script
import urllib2,re


#make a new browser, this will download pages from the web for us. This is done by calling the 
#build_opener() method from the urllib2 library
browser=urllib2.build_opener()

#desguise the browser, so that websites think it is an actual browser running on a computer
browser.addheaders=[('User-agent', 'Mozilla/5.0')]


#number of pages you want to retrieve (remember: 10 freelancers per page)
pagesToGet=100


#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
fileWriter=open('CountryOfLastfm.txt','w')


#for every number in the range from 1 to pageNum+1  
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page
    
    #make the full page url by appending the page num to the end of the standard prefix
    #we use the str() function because we cannot concatenate strings with numbers. We need
    #to convert the number to a string first.
    url='http://www.last.fm/music/+tag/country?page='+str(page)
    #use the browser to get the url.
    response=browser.open(url)
    
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()
    segments =re.findall('<a href="/music/(.*?)"     class="name"',myHTML)
    #segments=myHTML.split('<strong class="name">') # split


    #for all the segments except the 1st and last one
    #for j in range(1,len(segments)-1,1): # the len(myList) function returns the length (number of elements) in the given list
    for i in segments:    
        #get the segment in the j-th position

        #find the position of the first double quote character "  in the segment
        
        #get the part (sub-string) of the segment from position 0 all the way to (but excluding) position index
        link= i
        
        #write the link to the freelancer's profile to the file. We want one link per line, so we add '\n' character to change lines.
        fileWriter.write('http://www.last.fm/music/'+link+'\n')
    

#close the file. File that are opened must always be closed to make sure everything is actually written and finalized.
fileWriter.close()


