import requests
from fake_useragent import UserAgent

ua = UserAgent()
##
##       https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/52186/statistics/overall (23/24)
##City = https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/41886/statistics/overal(22/23)
##       https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/37036/statistics/overall (21/22)
##       https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/29415/statistics/overall (20/21)
##       https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/23776/statistics/overall (19/20)
##       https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/17359/statistics/overall (18/19)
##
##Liverpool = https://api.sofascore.com/api/v1/team/44/unique-tournament/17/season/41886/statistics/overall
##

Times = {'Manchester City': 'manchester-city/17', 'Liverpool': 'liverpool/44', 'Arsenal': 'arsenal/42',
         'Tottenham': 'tottenham-hotspur/33',
         'Aston Villa': 'aston-villa/40', 'Manchester United': 'manchester-united/35',
         'Newcastle': 'newcastle-united/39',
         'Brighton': 'brighton-and-hove-albion/30', 'West Ham': 'west-ham-united/37', 'Chelsea': 'chelsea/38',
         'Brentford': 'brentford/50',
         'Wolverhampton': 'wolverhampton/3', 'Cristal Palace': 'crystal-palace/7',
         'Notthingham Forest': 'nottingham-forest/14',
         'Fulham': 'fulham/43', 'Bournemounth': 'bournemouth/60', 'Luton City': 'luton-town/72',
         'Sheffield United': 'sheffield-united/15',
         'Everton': 'everton/48', 'Burley': 'burnley/6'}

browser = {'User-Agent': ua.random}

base_api = 'https://api.sofascore.com/api/v1/team/'
end_api = '/statistics/overall'


def escolher_time(time: str):
    data_list = []
    cont_url_list = 0
    cont_data_list = 0
    serie = 17
    loc = Times.get('{}'.format(time))
    pos = loc.split("/")[1]

    url24 = base_api + pos + '/unique-tournament/17/season/52186' + end_api
    url23 = base_api + pos + '/unique-tournament/17/season/41886' + end_api
    url22 = base_api + pos + '/unique-tournament/17/season/37036' + end_api
    url21 = base_api + pos + '/unique-tournament/17/season/29415' + end_api
    url20 = base_api + pos + '/unique-tournament/17/season/23776' + end_api
    url19 = base_api + pos + '/unique-tournament/17/season/17359' + end_api

    url_list = [url19, url20, url21, url22, url23, url24]

    for url in url_list:
        api_link = requests.get(url, headers=browser).json()
        if not 'error' in api_link:
            data_list.append(api_link['statistics'])
            if url_list.index(url_list[cont_url_list]) == 0:
                data_list[cont_data_list]['ano'] = '2018/2019'
            elif url_list.index(url_list[cont_url_list]) == 1:
                data_list[cont_data_list]['ano'] = '2019/2020'
            elif url_list.index(url_list[cont_url_list]) == 2:
                data_list[cont_data_list]['ano'] = '2020/2021'
            elif url_list.index(url_list[cont_url_list]) == 3:
                data_list[cont_data_list]['ano'] = '2021/2022'
            elif url_list.index(url_list[cont_url_list]) == 4:
                data_list[cont_data_list]['ano'] = '2022/2023'
            elif url_list.index(url_list[cont_url_list]) == 5:
                data_list[cont_data_list]['ano'] = '2023/2024'
        cont_url_list += 1
    x = requests.get('https://api.sofascore.com/api/v1/team/17/unique-tournament/17/season/52186/statistics/overall', headers=browser)

    return print(data_list
                 )


escolher_time('Manchester City')
