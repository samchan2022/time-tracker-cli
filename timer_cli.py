import sqlite3
import os
import argparse
import sys
from datetime import datetime, timedelta
from timer import timer as timer_module
from config import config


def main():
    con = sqlite3.connect(config.DATABASE)
    con.row_factory = sqlite3.Row

    timer = timer_module.Timer(con)
    timer.init_timer()

    # create parser object
    parser = argparse.ArgumentParser(description = "a simple time tracker CLI in Python 3, with an Sqlite3 database")

    # defining arguments for parser object

    parser.add_argument("-n", "--name", type = str, 
                        metavar = "timer_name", default = None,
                        help = "Name of the timer")

    parser.add_argument("-s", "--start", action="store_true",
                        help = "Start the timer, use together with --name timer_name")

    parser.add_argument("-p", "--stop", action="store_true",
                        help = "Stop the timer, use together with --name timer_name")

    parser.add_argument("-a", "--all", action="store_true",
                        help = "Get all the timers")

    parser.add_argument("-m", "--message", type = str, metavar = "message", default = None,
                        help = "Update the timer message, with --name timer name --message message")

    parser.add_argument("-d", "--delete", action="store_true",
                        help = "Delete the timer, use together with --name timer_name")

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.all == True:
        timer.get_all_timers()
    elif args.start == True:
        if args.name != None:
            timer.start_timer(args.name, args.message)
        else:
            parser.print_help()
    elif args.stop == True:
        if args.name != None:
            timer.stop_timer(args.name)
        else:
            parser.print_help()
    elif args.delete == True:
        if args.name != None:
            timer.delete_timer(args.name)
        else:
            parser.print_help()
    elif args.message != None:
        if args.name != None:
            timer.update_msg( args.name, args.message )
        else:
            parser.print_help()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()


if __name__ == "__main__":
    # calling the main function
    main()
