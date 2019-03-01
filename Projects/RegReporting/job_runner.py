'''
Job runner script for Reg Reporting webapp 
'''

import sys

# High Level Requirements
# 1. read  data_flow_job table in RegReporting database (ms sql server)
#       for each data flow job:
#           a) pull data based on return -> report_data
#           b) initiate data flow tasks based on return-report and job definition definition
#
# 2. data is stored in 3 columns i.e. element_id, element_value, additional_attributes (json object)
#    create a csv output file from above and send it out to its destination 
#
# 3. supported data destinations
#    a) windows share drive e.g. \\server\\folder\\ 
#    b) sftp e.g. host (pre setup required e.g. key exchange )
#    c) sql server e.g. connection string (pre setup required e.g. permissions)


def main(argv):
    try:
        pass
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)
