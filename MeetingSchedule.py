time_stamp =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


time_stamp = sorted(time_stamp)

merged = [time_stamp[0]]

for current_meeting_start, current_meeting_end in time_stamp[1:]:
    last_meeting_start, last_meeting_end = merged[-1]

    if current_meeting_start <= last_meeting_end:
        merged[-1] = (last_meeting_start, max(last_meeting_end, current_meeting_end))
    else:
        merged.append((current_meeting_start, current_meeting_end))

print(merged)