#!/bin/bash
# Clean up user expense data in csv format
# Usage: ./cleanup.sh -u <user_number>
# If user number is not provided, all user data will be cleaned up
#
# *Should be executed as scheduled system job after all data is stored into RDS.

USER_NUMBER=""
while getopts ":u:" opt; do
    case $opt in
        u)
            USER_NUMBER=$OPTARG
        ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
        ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
        ;;
    esac
done

if [ -z "$USER_NUMBER" ]; then
    FILE_PATTERN="./data/user/user_*.csv"
    echo "No user number provided. Clearing data for all users."
else
    FILE_PATTERN="./data/user/user_${USER_NUMBER}*.csv"
    echo "Clearing data for user $USER_NUMBER."
fi

if ls $FILE_PATTERN 1> /dev/null 2>&1; then
    echo "Cleaning up files: $FILE_PATTERN"
    rm -f $FILE_PATTERN
    echo "Cleanup completed."
else
    echo "No files found matching the pattern: $FILE_PATTERN"
fi
