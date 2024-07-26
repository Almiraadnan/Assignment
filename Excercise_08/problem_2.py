f = open('user.txt','r')
content = """Hi *user*!
We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""
text = f.read()
f.close()
s = open('user_email.txt','a')
updated_text = text.replace("*user*","Mahnoor").replace("*title*", "you").replace("*here*", "Almira is here")

update = s.write(updated_text)