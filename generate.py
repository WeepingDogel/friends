import os
import toml
'''
Generation Process.
By WeepingDogel
'''
class KnowingFriends():
    def LoadFriends(self,filename):
        # The information of friends will be stored in a toml file.
        # So this function is the first step.
        # The file will be loaded and formatted as toml.
        friendsList = toml.load(filename)
        return friendsList
class Process():
    def InitializeHTML(self):
        # Let's initialize!
        if os.path.exists('public') == False:
            os.system('mkdir public')
        os.system('cp resources/style.css public/style.css')
        f = open('public/index.html','w')
        f.write('''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="style.css">
<title>Friends</title>
</head>
<body>
''')
        print("HTML Initialization Done!")
    def GenerateTop(self,friends):
        f = open('public/index.html','a')
        f.write('<div class="top">\n')
        f.write('<h1>Friends</h1>\n')
        f.write('<a href="' + friends['Main']['backurl'] + '">Back</a>')
        f.write('</div>\n')
    def WriteCards(self,friends,numbers):
        f = open('public/index.html','a')
        for i in range(1,numbers + 1):
            title = friends['friends'][str(i)]['Title']
            bio = friends['friends'][str(i)]['Bio']
            url = friends['friends'][str(i)]['URL']
            avatar = friends['friends'][str(i)]['Avatar']
            f.write('<div class="friend">\n')
            f.write('<img src="' + avatar + '">')
            f.write('<h1>' + title + '</h1>\n')
            f.write('<p>' + bio + '</p>\n')
            f.write('<a href="'+ url + '">传送</a>\n')
            f.write('</div>\n')
            print("Writing[" + str(i) + "]: " + title + '|' + bio + '|' + url)
        f = open('public/index.html','a')
        f.write('</body>\n</html>')
def Main():
    # Main Channel of all.
    # All the things will be started here.
    KF = KnowingFriends()
    P = Process()
    friends = KF.LoadFriends("friends.toml")
    numbers = friends['friends']['number']
    P.InitializeHTML()
    P.GenerateTop(friends)
    P.WriteCards(friends,numbers)
Main()
