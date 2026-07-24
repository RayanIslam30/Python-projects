# Code that takes HTML output from youtube, and gives back just a sharable url to go to that video on youtube
import re

def main():
    print(
        parse(input("HTML: "))
    )  # Ask for HTML output, and call our function to read it


def parse(html):
    # Same check for short and long input
    if html := re.search(
        r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', html
    ):  # Check if html formatted right, get the link embed and ignore everything else
        return f"https://youtu.be/{html.group(1)}"
    else:  # Otherwise, not valid
        return "None"


if __name__ == "__main__":  # Only run if called directly
    main()
