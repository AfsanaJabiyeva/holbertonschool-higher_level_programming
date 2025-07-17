#!/usr/bin/python3
def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template should be string")
        return None

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be list of dictionaries")
        return None

    if not template.strip():
        print("Template is empty, no output files generated.")
        return None

    if not attendees:
        print("No data provided, no output files generated.")
        return None

    for index, attendee in enumerate(attendees, start=1):
        filled_temp = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is not None:
                value = str(value)
            else:
                value = "N/A"

            filled_temp = filled_temp.replace(f"{{{key}}}", value)

        output_file = f"output_{index}.txt"
        try:
            with open(output_file, 'w', encoding="utf-8") as o_f:
                o_f.write(filled_temp)
        except Exception as e:
            print(f"Error: {e}")
