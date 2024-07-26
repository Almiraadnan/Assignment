f = open('user.txt','w')

text = f.write("""Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
""")

f.close()