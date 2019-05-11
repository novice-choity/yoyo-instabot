# from instagram.client import InstagramAPI as insapi
#
# access_token = "487216636.8d8290a.f431986a342d42c3ba7bfccde164d25a"
# client_secret = "e42ae8768ebe4824b3ab74c39882dbb4"
# client_id = "8d8290aff80445e9a293b8d04a652b43"
# api = insapi(access_token=access_token, client_secret=client_secret)
# print(api.user())

from InstagramAPI import InstagramAPI

api = InstagramAPI("xalien.007", "Xalien007")
bot = api.login()
# print(api.getTotalFollowers(usernameId=487216636))
# print(api.follow(userId=487216636))
# print(api.userFriendship(userId=487216636))
# print(api.getPopularFeed())
# print(api.LastJson)
print(api.getSelfUsersFollowing())
users = api.LastJson.get('users')
for user in users:
    print(user.get('username'), user.get('pk'))
    # print(len(api.getTotalFollowers(user.get('pk'))))
