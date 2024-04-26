import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^(.+)(https?://)(www\.)?(youtube\.com/embed/[a-zA-Z0-9]+)(.+)$", s):
        if "www." in s:
            link = match.group(2) + match.group(3) + match.group(4)
        else:
            link = match.group(2) + match.group(4)

        return re.sub(r"https?://(www\.)?youtube\.com/embed/", r"https://youtu.be/", link)

    else:
        return None







if __name__ == "__main__":
    main()

