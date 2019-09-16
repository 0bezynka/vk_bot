import vk_api
import time
import datetime
now = datetime.datetime.now()
vk=vk_api.VkApi(token="TOKKEN")

#Подписчики
friends_get_Followers = vk.method("users.getFollowers")
friends_get_Followers_items = (friends_get_Followers["items"])#Spisok 1

#Заявки в др
friends_get_Requests = vk.method("friends.getRequests")
list_Requests = (friends_get_Requests["items"])#Spisok 2

#обьединение списка
list_id = friends_get_Followers_items + list_Requests

log_info = ("[ Подписчиков: {}\n[ Заявок в др: {}\n[ Всего ID: {}".format(friends_get_Followers["count"],friends_get_Requests["count"],len(list_id)))
print(log_info)

# log file ===================================
log_write = ("{}\nПодписчиков: {} Заявок в др: {} Всего ID: {}\n".format(now.strftime("%d-%m-%Y %H:%M"),friends_get_Followers["count"],friends_get_Requests["count"],len(list_id)))
log_file = open("log.txt", "a", encoding='utf-8')
log_file.write(log_write)
log_file.close()

#добавление всех айди
for list_id in list_id:
    add_friend = vk.method("friends.add", {"user_id":list_id})
    print ("[+]Заявка одобрена")# .format(schet)
    time.sleep(5)#Одобряет раз в 5 секунды

print("[ Тайм-аут ]")
time.sleep(60)#Sleep 1 ========================================

#Сколько общих друзей вк
friends_get_Suggestions = vk.method("friends.getSuggestions",{"filter":"mutual","count":42})#Сколько общих друзей вк
users_list_id = (friends_get_Suggestions["items"])#получаем список айди общих друзей

for users_list_id in users_list_id:
    user_id = (users_list_id["id"])#айди пользователей

    users_first_name = (users_list_id["first_name"])#имя пользователя
    users_last_name = (users_list_id["last_name"])#фамилия пользователей

    user_id_add = vk.method("friends.add", {"user_id":user_id})#добавляем в друзья
    print("[+]Заявка отправлена: {} {}".format(users_first_name,users_last_name))

    # log file ===================================
    log_request = ("[+]Заявка отправлена: {} {}\n".format(users_first_name,users_last_name))
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_request)
    log_file.close()

    time.sleep(5)#отправляет раз в 5 секунд

print("Все выполнено!")
#time.sleep(60)


#----------------------------------------------------
# Author:      0bezynka
# Link:        https://github.com/0bezynka/vk_bot
#----------------------------------------------------
