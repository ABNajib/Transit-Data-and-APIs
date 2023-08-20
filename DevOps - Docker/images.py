import os
import sys
import pymysql
from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers

# delete containers
def delete(image):
    cmd = f'docker image rm {image}'
    result = os.system(cmd)
    if (result == 0):
        print(f'Removed {image}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('mysqlimg')
    delete('mongoimg')
    delete('debeziumimg')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker build -t mysqlimg -f Dockerfiles/MySQLDB/Dockerfile .', 'mysqlimg')
    create('docker build -t mongoimg -f Dockerfiles/MongoDB/Dockerfile .', 'mongoimg')
    create('docker build -t debeziumimg -f Dockerfiles/DebeziumCDC/Dockerfile .', 'debeziumimg')
    sys.exit()

