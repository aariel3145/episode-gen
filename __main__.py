"""
File: __main__.py

Project: Episode-Gen

Description:    Takes a csv file of episodes of a show, puts them into a dict, picks a random episode
                Currently only works for Discovery Plus shows: Mythbusters, Dirty Jobs, Battlebots

Programmer: Amy Ariel

"""

# Imports
import sys
import csv
import random
import webbrowser

# variables
browser = "chrome_pc"
discovery_plus = ["mythbusters", "dirty jobs", "battlebots"]
replace_punc = "!?,'-()/"
chrome_pc_path = "C://Program Files//Google//Chrome//Application//Chrome.exe"
episodes = []

if __name__ == "__main__":
    # get name of show from command line
    show = ""
    for i in range(1, len(sys.argv)):
        if i > 1:
            show += " "
        show += sys.argv[i]

    # open show csv, if possible
    try:
        infile = open(show + ".csv", mode = 'r')
    except:
        print(f"Error: show '{show}' is not in database")
        sys.exit(1)

    # read episodes csv into list, each as a dict
    reader = csv.DictReader(infile)
    for rows in reader:
        episodes.append(rows)

    # pick random episode to watch
    watch = random.choice(episodes)
    print(f'You should watch {show.title()} Season {watch["season"]}, Episode {watch["episode"]}, {watch["title"]}.')

    # generate URL for show
    watch_show = show.lower().replace(" ", "-")
    watch_title =  watch["title"].lower()
    for char in watch_title:
        if char in replace_punc:
            watch_title = watch_title.replace(char,"")
    watch_title = watch_title.replace("  ", "-")
    watch_title = watch_title.replace(" ", "-")

    # determine which streaming service to open / what URL scheme to use
    if watch_show in discovery_plus:
        url = "discoveryplus.com/video/" + watch_show + "/" + watch_title

    # determine which browser to use
    if browser == "chrome_pc":
        path = locals()[browser + "_path"]

    # open episode in browser
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(path))
    webbrowser.get(browser).open_new_tab(url)