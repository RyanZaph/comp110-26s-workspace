from lessons.profiles import Profile
user1: Profile = Profile("110 rules")

#Create a new variable user1 that  is reference to a profle objwct with the username 110_rulez
user1.private = False
print(user1.private)

user1.tweet("OOP is cool!")