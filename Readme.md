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



Test
===================================================

Test cases

1. Start the timer, w and  w/o an optional description/message
2. Stop the timer 
3. Update the message
4. Delete the timer
5. List all timers



Test Case 1 - start the timer
___________________________________________________


1.First start a timer 

    python3 timer_cli.py --name test1 --start



2.Check the timer

    python3 timer_cli.py --all


Result

    Number of timers: 1
    test1: 0day 0hour 0min 3sec


3.Check again to see if the timer is running. If the time is increased, then it should be working.

    python3 timer_cli.py --all


Result

    Number of timers: 1
    test1: 0day 0hour 2min 13sec



Test Case2 - stop the timer
___________________________________________________


1.Stop the timer 


    python3 timer_cli.py --name test1 --stop


2.Check the timer

    python3 timer_cli.py --all


Result

    Number of timers: 1
    test1: 0day 0hour 15min 57sec


3.Check again to see if the timer has stopped. If the time remains the same, then the timer has stopped

    python3 timer_cli.py --all


Result

    Number of timers: 1
    test1: 0day 0hour 15min 57sec




Test Case3 - Update the message
___________________________________________________

1.Update the message


    python3 timer_cli.py --name test1 --message "My new message"


2.Check the timer

    python3 timer_cli.py --all


Result

    Number of timers: 1
    test1: 0day 0hour 15min 57sec My new message



Test Case4 - Delete the timer
___________________________________________________

1.Delete the timer 

    python3 timer_cli.py --name test1 --delete


2.Check the timer

    python3 timer_cli.py --all


Result

    Number of timers: 0


Test Case5 - List all timers
___________________________________________________


1.Create multiple timers



    python3 timer_cli.py --name test1 --start --message "My first message"
    python3 timer_cli.py --name test2 --start --message "My second message"
    python3 timer_cli.py --name test3 --start --message "My third message"


2.Check the timer

    python3 timer_cli.py --all


Result

    Number of timers: 3
    test1: 0day 0hour 0min 22sec My first message
    test2: 0day 0hour 0min 14sec My second message
    test3: 0day 0hour 0min 9sec My third message


