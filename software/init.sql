DROP DATABASE IF EXISTS IMPACT;
CREATE DATABASE IMPACT;
USE IMPACT;

DROP TABLE IF EXISTS `sensor_raw_one`;
CREATE TABLE IF NOT EXISTS `sensor_raw_one` (
    id INT(16) AUTO_INCREMENT,
    x_accel_one VARCHAR(75),
    y_accel_one VARCHAR(75),
    z_accel_one VARCHAR(75),
    x_gyro VARCHAR(75),
    y_gyro VARCHAR(75),
    z_gyro VARCHAR(75),
    temperature VARCHAR(75),
    x_accel_two VARCHAR(75),
    y_accel_two VARCHAR(75),
    z_accel_two VARCHAR(75),
    timestamp VARCHAR(75),
    x_angular_accel VARCHAR(75),
    y_angular_accel VARCHAR(75),
    z_angular_accel VARCHAR(75),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE INDEX sensor_raw_one_timestamp ON `sensor_raw_one` (timestamp);

DROP TABLE IF EXISTS `sensor_raw_two`;
CREATE TABLE IF NOT EXISTS `sensor_raw_two` (
    id INT(16) AUTO_INCREMENT,
    x_accel_one VARCHAR(75),
    y_accel_one VARCHAR(75),
    z_accel_one VARCHAR(75),
    x_gyro VARCHAR(75),
    y_gyro VARCHAR(75),
    z_gyro VARCHAR(75),
    temperature VARCHAR(75),
    x_accel_two VARCHAR(75),
    y_accel_two VARCHAR(75),
    z_accel_two VARCHAR(75),
    timestamp VARCHAR(75),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE INDEX sensor_raw_two_timestamp ON `sensor_raw_two` (timestamp);

DROP TABLE IF EXISTS `sensor_raw_three`;
CREATE TABLE IF NOT EXISTS `sensor_raw_three` (
    id INT(16) AUTO_INCREMENT,
    x_accel_one VARCHAR(75),
    y_accel_one VARCHAR(75),
    z_accel_one VARCHAR(75),
    x_gyro VARCHAR(75),
    y_gyro VARCHAR(75),
    z_gyro VARCHAR(75),
    temperature VARCHAR(75),
    x_accel_two VARCHAR(75),
    y_accel_two VARCHAR(75),
    z_accel_two VARCHAR(75),
    timestamp VARCHAR(75),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE INDEX sensor_raw_three_timestamp ON `sensor_raw_three` (timestamp);

