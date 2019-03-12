'''
Data flow job execution script for Regulatory Reporting (Manual Adjustments) application
The script is ran daily, it reads the content of 'data flows' table and executes data transfers as per definition. 
'''

import sys

# High Level Requirements

# 1. read  data_flow_job table in RegReporting database (ms sql server)
#       for each data flow job:
#           a) pull data based on return -> report_data (data shape is part of report definition)
#           b) initiate data flow tasks based on data destination definition definition for the flow
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
    except:
        print('Unhandled error in main()')


if __name__ == "__main__":
    main(sys.argv)

