import requests
import datetime
import constants


def get_auth_token(url, school_ihfo):
    response = requests.get(
        f"{url}/auth?login={school_ihfo['login']}&password={school_ihfo['password']}&devkey={school_ihfo['devkey']}&vendor={school_ihfo['vendor']}").json()
    school_ihfo['token'] = response['response']['result']['token']
    school_ihfo['expires'] = response['response']['result']['expires']
    return school_ihfo


def get_shedule_all(url, school_ihfo):
    classes = {'8А': '8А', '9А': '9А', '9Б': '9Б',
               '10А': '10А', '10Б': '10Б', '10В': '10В', '10Г': '10Г', '10Д': '10Д', '10О': '10О',
               '11А': '11А', '11Б': '11Б', '11В': '11В', '11Г': '11Г', '11Д': '11Д', '11О': '11О'}
    for item in classes:
        shedule_response = requests.get(
            f'{url}/getschedule?student=&days={datetime.datetime.now().strftime("%Y%m%d")}&class={item}&rings=no&vendor={school_ihfo["vendor"]}&devkey={school_ihfo["devkey"]}&login={school_ihfo["login"]}&password={school_ihfo["password"]}').json()
        classes[item] = shedule_response['response']['result']['days'][datetime.datetime.now().strftime("%Y%m%d")][
            'items']
    return classes


def get_classrooms_shedule(url, school_ihfo):
    shedule = get_shedule_all(url, school_ihfo)
    classrooms = {'22': [], '23': [], '24_25': [], '26': [], '31': [], '32': [], '33': [], '34': [], '35': [], '41': [],
                  '42': [], '43': [], '44': [], '45': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': [],
                  '61': [], '62': [], '63': [], '64': [], '65': [], '79а': [], '78': []}

    for item in shedule:
        for lesson in range(len(shedule[item])):
            for room in classrooms:
                if room in shedule[item][lesson]['room']:
                    classrooms[room].append(shedule[item][lesson])
    return classrooms


url = "https://lyceum-fa.eljur.ru/api"
school_ihfo = {'login': "ShoolClasTab",
               'password': "846nfasdg65s4d",
               'vendor': "lyceum-fa",
               'devkey': "d7d706aa96e3fa15df1657d86e81cb10",
               'token': '',
               'expires': '', }

classrooms = constants.classrooms
