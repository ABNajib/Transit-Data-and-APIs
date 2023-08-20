import os
import sys
import pymysql
from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql, mongodb does not need it

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

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
    delete('some-mysql')
    delete('some-mongo')
    # Add code to delete "some-redis" for Redis database container for Activity 13.4
    delete('some-redis')
    # Add code to delete "some-cassandra" for Cassandra database container for Activity 13.5
    delete('some-cassandra')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker network create MBTANetwork', 'MBTANetwork')
    create('docker run -p 3300:3306 --name mysqlserver --network MBTANetwork -dti mysqlimg', 'mysqlserver')
    create('docker run -p 27017:27017 --name some-mongo --network MBTANetwork -dti mongoimg', 'some-mongo')
    create('docker run --name debeziumserver --network MBTANetwork -dti debeziumimg', 'debeziumserver')
    sys.exit()

# if -init, init mysql, mongodb does not need it
if(argument == '-init'):
    #init_mysql()
    # Add call to init_cassandra() to initialize the Cassandra database container. Activity 13.5.
    #init_cassandra()
    sys.exit()