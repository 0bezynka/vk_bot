import vk_api
import time
vk=vk_api.VkApi(token="TOKKEN")

# Подписчики
friends_get_Followers = vk.method("users.getFollowers")
friends_get_Followers_items = (friends_get_Followers["items"])# Spisok 1

# Заявки в др
friends_get_Requests = vk.method("friends.getRequests")
list_Requests = (friends_get_Requests["items"])# Spisok 2

# Обьединение списка
list_id = friends_get_Followers_items + list_Requests

info = ("[ Подписчиков: {}\n[ Заявок в др: {}\n[ Всего ID: {}".format(friends_get_Followers["count"],friends_get_Requests["count"],len(list_id)))
print(info)

#добавление всех айди
for add_id in list_id:
    add_friend = vk.method("friends.add", {"user_id":add_id})
    print ("[+]Заявка одобрена")
    time.sleep(5)#Одобряет раз в 5 секунды

print("[ Тайм-аут ]")
time.sleep(60)# Sleep 1

#Сколько общих друзей вк
friends_get_Suggestions = vk.method("friends.getSuggestions",{"filter":"mutual","count":42})#Сколько общих друзей вк
users_list_id = (friends_get_Suggestions["items"])#получаем список айди общих друзей

for users_list_id in users_list_id:
    user_id = (users_list_id["id"])#айди пользователей

    users_first_name = (users_list_id["first_name"])#имя пользователя
    users_last_name = (users_list_id["last_name"])#фамилия пользователей

    user_id_add = vk.method("friends.add", {"user_id":user_id})# Добавляем в друзья
    print("[+]Заявка отправлена: {} {}".format(users_first_name,users_last_name))

    time.sleep(5)# Отправляет раз в 5 секунд

print("Все выполнено!")

#----------------------------------------------------
# Author:      0bezynka
# Link:        https://github.com/0bezynka/vk_bot
#----------------------------------------------------
