from urllib.request import urlopen
import json

token = "YOU TOKEN"
group_id = "ID"

def count_user():
    url = "https://api.vk.com/method/groups.getById.json?group_ids=" + group_id + "&fields=members_count&access_token=" + token + "&v=5.52"
    response = urlopen(url)
    data = response.read()
    jsn = json.loads(data)
    count_group = jsn["response"][0]["members_count"]
    return count_group

def pagination():
    tmpus = count_user()
    url_page = set()
    filter = "blacklisted"
    for x in range(0, tmpus, 999):
        url_page.add("https://api.vk.com/method/groups.getMembers.json?group_id=" + group_id + "&fields="+filter+"&access_token=" + token + "&offset=" + str(x) + "&v=5.52")
    return url_page

def get_user_id():
    id = set()
    for url_pag in pagination():
        respag = urlopen(url_pag, timeout=40)
        data_pag = respag.read()
        jsn_pag = json.loads(data_pag)
        for id_t in jsn_pag["response"]["items"]:
            if "deactivated" in id_t:
                zaglushka=0
            else:
                id.add(id_t["id"])
    return id

print (len(get_user_id()))
