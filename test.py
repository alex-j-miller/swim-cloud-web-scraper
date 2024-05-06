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

def getEventID(event_name):
    if ' Y ' in event_name:
        event_name = event_name.replace(' Y ', ' ')
    elif ' L ' in event_name:
        event_name = event_name.replace(' L ', ' ')
    return ss.getEventID(event_name)

roster = getRoster()
csv = []
for i in range(len(roster)):
    print(f"{roster[i]['swimmer_name']} : {roster[i]['swimmer_ID']}")
    print(f"{i/len(roster)*100}%")
    events = ss.getSwimmerEvents(roster[i]['swimmer_ID'])
    print(events)
    for event in events:
        times = ss.getSwimmerTimes(roster[i]['swimmer_ID'], '', event_ID=getEventID(event))
        csv.append(times)
        print(f"{roster[i]['swimmer_name']} : {event} : {times}")