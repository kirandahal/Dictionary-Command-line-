import json
from difflib import get_close_matches
data=json.load(open("data.json"))
i=1
while(i>0):
    def app(user):
        user = user.lower()
        if user in data:
            return data[user]
        elif user.title() in data:
            return data[user.title()]
        elif user.upper() in data:
            return data[user.upper()]
        elif len(get_close_matches(user,data.keys()))>0:
            print("did you mean %s instead" %get_close_matches(user,data.keys())[0])
            a=input("enter Y For Yes and N for No")
            if "Y"  in a or "y" in a:
                return data[get_close_matches(user,data.keys())[0]]
            elif "N" in a or "n" in a:
                return("eneter again the word properly")

            else:
                return"only y and n is needed.write word again"
        else:
            return "words not found .please try again another word."
    user= input("enter the required word :")
    fo=app(user)
    if type(fo) == list:
        for item in fo:
            fo=item
            print(fo)
    else:
        print(fo)


