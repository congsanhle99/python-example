import webbrowser as wb
from var import WEB_URLS


# def workAuto():
#     Edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
#     url = input("Enter name of the website:# ")
#     wb.get(Edge_path).open(url)


# workAuto()


def workAuto():
    Edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    URLs = WEB_URLS
    for url in URLs:
        wb.get(Edge_path).open(url)


workAuto()
