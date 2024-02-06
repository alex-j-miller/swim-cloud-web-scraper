import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page(event, gender, team_id = "55", year = "2024"):
    return requests.get(f'https://www.swimcloud.com/team/{team_id}/times/?dont_group=false&event={event}&event_course=Y&gender={gender}&page=1&region&season_id=27&tag_id&team_id={team_id}&year={year}')

def get_data_frame(page):
    soup = BeautifulSoup(page.text, features="html.parser")
    table = soup.find('table', attrs={'class':'c-table-clean table table-hover'})

    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)

    data_frame = pd.DataFrame(columns = headers)
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(data_frame)
        data_frame.loc[length] = row

    return data_frame

eventName_to_eventID = {"50 Free" : "150",
                        "100 Free" : "1100",
                        "200 Free" : "1200",
                        "500 Free" : "1500",
                        "1000 Free" : "11000",
                        "1650 Free" : "11650",
                        "50 Back" : "250",
                        "100 Back" : "2100",
                        "200 Back" : "2200",
                        "50 Breast" : "350",
                        "100 Breast" : "3100",
                        "200 Breast" : "3200",
                        "50 Fly" : "450",
                        "100 Fly" : "4100",
                        "200 Fly" : "4200",
                        "100 IM" : "5100",
                        "200 IM" : "5200",
                        "400 IM" : "5400",
                        "200 Free Relay" : "1200",
                        "400 Free Relay" : "1400"
                        }

eventID_to_eventName = {"150" : "50 Free",
                        "1100" : "100 Free",
                        "1200" : "200 Free",
                        "1500" : "500 Free",
                        "11000" : "1000 Free",
                        "11650" : "1650 Free",
                        "250" : "50 Back",
                        "2100" : "100 Back",
                        "2200" : "200 Back",
                        "350" : "50 Breast",
                        "3100" : "100 Breast",
                        "3200" : "200 Breast",
                        "450" : "50 Fly",
                        "4100" : "100 Fly",
                        "4200" : "200 Fly",
                        "5100" : "100 IM",
                        "5200" : "200 IM",
                        "5400" : "400 IM",
                        "1200" : "200 Free Relay",
                        "1400" : "400 Free Relay"
                        }

events = ["150",
        "1100",
        "1200",
        "1500",
        "11000",
        "11650",
        "250",
        "2100",
        "2200",
        "350",
        "3100",
        "3200",
        "450",
        "4100",
        "4200",
        "5100",
        "5200",
        "5400",
        ]

genders = ["M", "F"]
team_id = "55" # 55 is the team id for the Calvin University
year = "2024" # 2024 is the year of the season

page = get_page("150", "M")
data_frame = get_data_frame(page)
data_frame.to_csv('swim_data.csv', index=False)

# pages = []
# for event in events:
#     for gender in genders:
#         url = f'https://www.swimcloud.com/team/{team_id}/times/?dont_group=false&event={event}&event_course=Y&gender={gender}&page=1&region&season_id=27&tag_id&team_id={team_id}&year={year}'
#         pages.append(requests.get(url))

# data_frames = []

# for page in pages:
#     soup = BeautifulSoup(page.text, features="lxml")
#     table = soup.find('table', attrs={'class':'c-table-clean table table-hover'})
#     print(table)


#     headers = []
#     for i in table.find_all('th'):
#         title = i.text
#         headers.append(title)
#     data_frame = pd.DataFrame(columns = headers)
#     data_frames.append(data_frame)

# for data_frame in data_frames:
#     # Get the data of the table
#     for j in table.find_all('tr')[1:]:
#         row_data = j.find_all('td')
#         row = [i.text for i in row_data]
#         length = len(mydata)
#         mydata.loc[length] = row

# df.to_csv('swim_times.csv', index=False, encoding='utf-8')