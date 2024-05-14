import re

def change_ics_entries_to_delete(input_file, output_file):
    with open(input_file, 'r') as file:
        ics_content = file.read()

    updated_ics_content = re.sub(r'BEGIN:VEVENT.*?END:VEVENT', replace_with_delete, ics_content, flags=re.DOTALL)

    with open(output_file, 'w') as file:
        file.write(updated_ics_content)

def replace_with_delete(match):
    event = match.group(0)
    uid_match = re.search(r'UID:.*', event)
    if uid_match:
        uid = uid_match.group(0)
        cancel_event = re.sub(r'STATUS:.*\n', '', event) 
        cancel_event = re.sub(r'METHOD:.*\n', '', cancel_event) 
        cancel_event = cancel_event.replace('BEGIN:VEVENT', 'BEGIN:VEVENT\nMETHOD:CANCEL\nSTATUS:CANCELLED')
        return cancel_event
    return event

input_file = 'calendar.ics'
output_file = 'calendar_deleted.ics'
change_ics_entries_to_delete(input_file, output_file)
print(f"Updated calendar saved to {output_file}")
