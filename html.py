#Code that takes HTML output from youtube, and gives back just a sharable url to go to that video on youtube
import re 
import sys


def main():
    print(parse(input("HTML: "))) #Ask for HTML output, and call our function to read it


def parse(html):
    #Check if we have long or short output
    if short := re.search(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', html): #Check if our string meets all requirements for short html
        return f"https://youtu.be/{short.group(1)}"

if __name__ == "__main__": #Only run if called directly
    main()

