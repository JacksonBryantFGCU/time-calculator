# Jackson Bryant
# 04/03/2025
# Time calculator

def parse_time(time_str):
    """Parses time in 'HH:MM' format and returns (hours, minutes)."""
    hours, minutes = map(int, time_str.split(":"))
    return hours, minutes

def pad_time(value):
    """Returns a 2-digit string representation of a number."""
    return f"{value:02d}"

def convert_to_24_hour(start_time):
    """Converts a 12-hour formatted time to 24-hour format."""
    hours, minutes = parse_time(start_time[:-3])
    period = start_time[-2:].upper()

    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0

    return hours, minutes

def convert_to_12_hour(hours):
    """Converts 24-hour format to 12-hour format with AM/PM."""
    period = 'PM' if hours >= 12 else 'AM'
    hours = hours % 12 or 12  # Convert 0 to 12 for AM and adjust PM hours
    return hours, period

def add_time(start="12:00 AM", duration="00:30", day=""):
    """Adds a duration to a start time and returns the updated time with optional day tracking."""
    
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Capitalize the day correctly if provided
    day = day.capitalize() if day else ""

    start_hours, start_minutes = convert_to_24_hour(start)
    duration_hours, duration_minutes = parse_time(duration)

    # Calculate new time
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    total_hours = start_hours + duration_hours + extra_hours
    days_later = total_hours // 24
    new_hours = total_hours % 24

    # Convert back to 12-hour format
    final_hours, period = convert_to_12_hour(new_hours)

    # Determine the new day
    new_day = ""
    if day in WEEKDAYS:
        new_day = WEEKDAYS[(WEEKDAYS.index(day) + days_later) % 7]

    # Format output
    result = f"{final_hours}:{pad_time(new_minutes)} {period}"
    if new_day:
        result += f", {new_day}"
    
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result


# Tests
if __name__ == "__main__":
    print(add_time('3:30 PM', '2:12'))
    print(add_time('2:59 AM', '24:00', 'saturDay'))
    print(add_time('11:59 PM', '24:05', 'Wednesday'))
    print(add_time('8:16 PM', '466:02', 'tuesday'))
