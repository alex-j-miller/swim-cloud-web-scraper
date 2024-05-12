import SwimScraper as ss
import csv


def getRosterToCSV():
    roster = getRoster()
    with open('csv/roster.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=roster[0].keys())
        writer.writeheader()

        for player in roster:
            writer.writerow(player)

    print("CSV file created successfully.")

def getRoster():
    roster = ss.getRoster(team = '',team_ID = 55, gender = 'M', year = 2024)
    roster = roster + ss.getRoster(team = '',team_ID = 55, gender = 'F', year = 2024)
    return roster

def getRosterEvents():
    roster = getRoster()

    rosterEvents = []

    for swimmer in roster:
        rosterEvents.append({'swimmer_name': swimmer['swimmer_name'], 'events': ss.getSwimmerEvents(swimmer['swimmer_ID'])})
        print(f"{rosterEvents['swimmer_name']} : {rosterEvents['events']}")

def getMIAATeamsToCSV():
    MIAATeams = ss.getCollegeTeams(conference_names = ['MIAA'])

    with open('csv/MIAATeams.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=MIAATeams[0].keys())
        writer.writeheader()

        for team in MIAATeams:
            writer.writerow(team)

    print("CSV file created successfully.")
    return MIAATeams


# print(ss.getSwimmerTimes(750870, '', event_ID = 150))
    # times = ss.getSwimmerTimes(750870, '', event_ID = 150)

    # with open('csv/times.csv', 'w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=times[0].keys())
    #     writer.writeheader()

    #     for time in times:
    #         writer.writerow(time)

    # print("CSV file created successfully.")

def validEvent(event_name):
    return event_name in ss.events
    
def getSwimmerTimes(swimmer_ID, event_name):
    event_ID = getEventID(event_name)
    if event_ID == -1:
        return []
    return ss.getSwimmerTimes(swimmer_ID, '', event_ID)
    
# def getRosterTimes():
#     roster = getRoster()
#     csv = []
#     for i in range(len(roster)):
#         print(f"{roster[i]['swimmer_name']} : {roster[i]['swimmer_ID']}")
#         print(f"{i/len(roster)*100}%")
#         events = ss.getSwimmerEvents(roster[i]['swimmer_ID'])
#         print(events)
#         for event in events:
#             times = getSwimmerTimes(roster[i]['swimmer_ID'], event)
#             if times != []:
#                 csv.append(times)
#                 print(f"{roster[i]['swimmer_name']} : {event} : {times}")


# roster = getRoster()
# events = ss.getSwimmerEvents(roster[0]['swimmer_ID'])
# print(events)
# for event in events:
#     times = getSwimmerTimes(roster[0]['swimmer_ID'], event)
#     print(f"{roster[0]['swimmer_name']} : {event} : {times}")

def getEventCode(event_name):
    if ' Y ' in event_name:
        event_name = event_name.replace(' Y ', ' ')
        event_id = ss.getEventID(event_name)
        event_code = str(event_id) + 'Y'
    elif ' L ' in event_name:
        event_name = event_name.replace(' L ', ' ')
        event_id = ss.getEventID(event_name)
        event_code = str(event_id) + 'L'
    
    if validEvent(event_name):
        return event_code
    else:
        return -1

def getSwimmerTimesAndEvents(swimmer_id, swimmer_name):
    events = ss.getSwimmerEvents(swimmer_id)
    swimmer_times = []
    for event in events:
        event_code = getEventCode(event)
        if event_code != -1:
            times = ss.getSwimmerIDTimes(swimmer_id, event_code, swimmer_name)
            swimmer_times.append(times)
            print(f"{swimmer_name} : {event} : {times}")

    return swimmer_times

def getRosterTimes():
    swimmer_times = []
    roster = getRoster()

    for swimmer in roster:
        swimmer_times.append(getSwimmerTimesAndEvents(swimmer['swimmer_ID'], swimmer['swimmer_name']))

        with open('csv/times.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=swimmer_times[0][0].keys())
            writer.writeheader()

            for event in swimmer_times:
                for time in event:
                    writer.writerow(time)






getRosterTimes()