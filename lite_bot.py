import vk_api
import time

vk=vk_api.VkApi(token="TOKKEN")

friends_getOnline_my = vk.method("friends.getOnline",{"count":10, "order":"random"})#1 Список друзей онлайн
print("[ Список друзей получил")

for list_get_online in friends_getOnline_my:
    friends_getOnline_list = vk.method("friends.getOnline",{"user_id":list_get_online,"count":4})#2 Получаем друзей из списка
    print("[ Онлайн получил")

    for lists in friends_getOnline_list:
        add_friends = vk.method("friends.add",{"user_id":lists})#3 Отправляет заявку в друзья

        users_get = vk.method("users.get",{"user_ids":lists})#4 Узнает кому отправил заявку
        print("[+] Заявка отправлена: {} {}".format(users_get[0]["first_name"],users_get[0]["last_name"]))
        time.sleep(5)

print("Все выполнено!")


#----------------------------------------------------
# Author:      0bezynka
# Link:        https://github.com/0bezynka/vk_bot
#----------------------------------------------------