
Introduction
---------------------------------------------------
This project is a simple time tracker CLI in Python 3, with an Sqlite3 database.


Requisation
---------------------------------------------------
- python3
- sqlite3


Usage (python)
===================================================


Start a timer
---------------------------------------------------

    python3 timer_cli.py --name my_timer --start



start with message

    python3 timer_cli.py --name my_timer --start --message message



Stop a timer
---------------------------------------------------

    python3 timer_cli.py --name my_timer --stop



Update a timer message
---------------------------------------------------

    python3 timer_cli.py --name my_timer --message "my new message"


Delete a timer
---------------------------------------------------

    python3 timer_cli.py --name my_timer


List all timers
---------------------------------------------------

    python3 timer_cli.py --all


Usage (Linux)
===================================================


Start a timer
---------------------------------------------------

    ./timer_cli.sh --name my_timer --start



start with message

    ./timer_cli.sh --name my_timer --start --message message



Stop a timer
---------------------------------------------------

    ./timer_cli.sh --name my_timer --stop



Update a timer message
---------------------------------------------------

    ./timer_cli.sh --name my_timer --message "my new message"


Delete a timer message
---------------------------------------------------

    ./timer_cli.sh --name my_timer --message "my new message"


List all the timers
---------------------------------------------------

    ./timer_cli.sh --all


