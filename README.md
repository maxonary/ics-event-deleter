# iCalendar Event Deleter

## Overview

Has it ever happened to you that you falsely imported a calendar to you personal accoutn? Do you need to delete a large number of events now from your calendar? Manually deleting each event is be time-consuming...

A Python script designed to mark all events in an `.ics` calendar file as canceled. This script reads an existing `.ics` file, modifies the events to indicate cancellation, and writes the updated content to a new `.ics` file. This can be useful for bulk-deleting events from a calendar.

## Features

- Reads all events from an input `.ics` file.
- Marks each event as canceled by adding `METHOD:CANCEL` and `STATUS:CANCELLED` properties.
- Writes the modified events to a new output `.ics` file.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Place your input `.ics` file in the same directory as the script, or provide the full path to the file.
2. Run the script with the input and output file names as arguments.
3. Import the output `.ics` file into your calendar application to remove prior added events.

### Example

```sh
python main.py input_calendar.ics output_calendar.ics
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

By using this script, you agree to take full responsibility for any modifications made to your calendar files. Always ensure you have backups of your data before running the script.