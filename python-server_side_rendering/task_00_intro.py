#!/usr/bin/python3
"""Generate text invitations from a template for given attendees."""


def generate_invitations(template, attendees):
    """Create invitation files for each attendee from a template."""

    placeholders = ["name", "event_title", "event_date", "event_location"]

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendee must be a dictionary.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        data = {}

        for key in placeholders:
            value = attendee.get(key)
            data[key] = value if value else "N/A"

        output = template.format(**data)

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output)
