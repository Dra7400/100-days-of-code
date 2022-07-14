class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        user.following += 1
        # print("new user being created...")

user_1 = User("001", "Dave")
print (user_1.username)
user_2 = User("002", "Laura")
# print (user_2.followers)

user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_1.followers)
print(user_2.followers)
