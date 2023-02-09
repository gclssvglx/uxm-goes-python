from datetime import datetime, timedelta

sessions = {
    1: ["4:18", "3:10", "2:58", "2:50", "3:29", "6:00", "3:04", "2:28"], 
    2: ["4:41", "4:29", "4:09", "3:49", "5:51", "6:01", "7:22"], 
    3: ["8:41", "12:54", "3:58", "4:53"], 
    4: ["5:03", "5:57", "8:22", "4:09", "5:25"], 
    5: ["11:27", "4:02", "5:30", "3:05"], 
    6: ["10:09", "7:48", "6:32", "4:41"], 
    7: ["10:12", "5:56", "11:03"], 
    8: ["10:13", "10:49"], 
    9: ["10:46", "8:03", "9:37"], 
    10: ["6:20", "8:43", "2:19", "5:03"],
    11: ["3:25", "10:31", "7:05", "4:30"], 
    12: ["4:03", "11:56", "7:17"], 
    13: ["9:57", "11:04"], 
    14: ["10:53", "4:41", "4:33", "7:15"], 
    15: ["7:55", "6:59", "2:19", "2:04"], 
    16: ["12:31", "13:42", "1:15"],
}

def calc_total_time(sessions):
    for durations in sessions.values():
        start_datetime = datetime(year=2023, month=2, day=10)
        end_datetime = datetime(year=2023, month=2, day=10)

        for duration in durations:
            minutes_and_seconds = duration.split(":")
            minutes = int(minutes_and_seconds[0])
            seconds = int(minutes_and_seconds[1])
            end_datetime = end_datetime + \
                timedelta(minutes=minutes, seconds=seconds)

        print("Duration: ", end_datetime - start_datetime)


calc_total_time(sessions)
