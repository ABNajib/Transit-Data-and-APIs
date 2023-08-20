import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']
            busDict['current_status'] = bus['attributes']['current_status']
            busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
            busDict['bearing'] = bus['attributes']['bearing']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['route_id'] = int(bus['relationships']['route']['data']['id'])
            busDict['stop_id'] = int(bus['relationships']['stop']['data']['id'])
            busDict['trip_id'] = int(bus['relationships']['trip']['data']['id'])
            busDict['updated_at'] = bus['attributes']['updated_at']
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  