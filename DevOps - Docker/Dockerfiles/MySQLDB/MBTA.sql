CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,

    occupancy_status varchar(255),
    current_status varchar(255),
    current_stop_sequence INT default null,
    bearing INT,
    direction_id INT not null,
    route_id INT not null,
    stop_id INT not null,
    trip_id INT not null,
    updated_at TIMESTAMP
);

