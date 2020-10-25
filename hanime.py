'''

                ██████╗  █████╗ ██████╗ ████████╗██╗  ██╗ ██████╗ ███████╗██╗   ██╗
                ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗██╔════╝██║   ██║
    Made by     ██████╔╝███████║██████╔╝   ██║   ███████║██║   ██║█████╗  ██║   ██║
                ██╔══██╗██╔══██║██╔══██╗   ██║   ██╔══██║██║   ██║██╔══╝  ██║   ██║
                ██████╔╝██║  ██║██║  ██║   ██║   ██║  ██║╚██████╔╝██║     ╚██████╔╝
                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ 
                                                                   
github: https://github.com/barthofu
personal website: https://barthofu.me
'''


from src import scraperClass #import the sweet class that will make all the work for us ;P

config = {
    
    "targetPath": './hanime_images/', #path to the directory where the images will be downloaded (can be either relative or absolute)
    "driverPath": "./chromedriver.exe", #path to the Chrome's driver, leave it as it is
    
    "showLinks": False, #print every link when they are scraped
    
    #you can enable or disable (True/False) filter tags here :)
    "tags": { #DON'T TOUCH THE 'divIndex's!
        "SFW": { "enabled": False, "divIndex": 1 },
        "NSFW": { "enabled": True, "divIndex": 2 },
        "Furry": { "enabled": False, "divIndex": 3 },
        "Futa": { "enabled": False, "divIndex": 4 },
        "Yaoi": { "enabled": False, "divIndex": 5 },
        "Yuri": { "enabled": True, "divIndex": 6 },
        "Trap": { "enabled": False, "divIndex": 7 },
        "3D": { "enabled": False, "divIndex": 8 },
    }
    
}


#let's fucking go 
scraper = scraperClass.Scraper(config).run()






