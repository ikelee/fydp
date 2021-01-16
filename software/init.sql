DROP DATABASE IF EXISTS IMPACT;
CREATE DATABASE IMPACT;
USE IMPACT;

DROP TABLE IF EXISTS `sensor_raw`;
CREATE TABLE IF NOT EXISTS `sensor_raw` (
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
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- CREATE INDEX user_credential_username ON `sensor_raw` (username);
