-- Create catalog & schema
CREATE CATALOG IF NOT EXISTS inceptez_catalog;
CREATE SCHEMA IF NOT EXISTS inceptez_catalog.insurancedb;

USE CATALOG inceptez_catalog;
USE SCHEMA insurancedb;

-----------------------------
-- CUSTOMERS TABLE (Delta)
-----------------------------
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    name STRING,
    email STRING,
    phone STRING,
    address STRING
)
USING DELTA;

-----------------------------
-- POLICIES TABLE
-----------------------------
DROP TABLE IF EXISTS policies;

CREATE TABLE policies (
    policy_id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    customer_id INT,
    policy_type STRING,
    premium DECIMAL(10,2),
    start_date DATE,
    end_date DATE
)
USING DELTA;

-----------------------------
-- CLAIMS TABLE
-----------------------------
DROP TABLE IF EXISTS claims;

CREATE TABLE claims (
    claim_id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    policy_id INT,
    claim_amount DECIMAL(10,2),
    claim_date DATE,
    status STRING
)
USING DELTA;

-----------------------------
-- PAYMENTS TABLE
-----------------------------
DROP TABLE IF EXISTS payments;

CREATE TABLE payments (
    payment_id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    policy_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    method STRING
)
USING DELTA;

-----------------------------
-- ETL OFFSETS TABLE
-----------------------------
DROP TABLE IF EXISTS etl_offsets;

CREATE TABLE etl_offsets (
    table_name STRING,
    last_offset BIGINT,
    inserted_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
USING DELTA
TBLPROPERTIES('delta.feature.allowColumnDefaults' = 'supported');

-----------------------------
-- INSURANCE METRICS (Empty Table)
-----------------------------
DROP TABLE IF EXISTS insurance_metrics;

CREATE TABLE insurance_metrics
USING DELTA
AS SELECT * FROM (
  SELECT
    NULL AS metric_name,
    NULL AS metric_value,
    NULL AS created_ts
)
WHERE 1=0;

-----------------------------------------------------
-- INSERT records into delta tables
-----------------------------------------------------

INSERT INTO customers(name,email,phone,address) VALUES ('Customer1','customer1@mail.com','900001001','Address 1');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer2','customer2@mail.com','900001002','Address 2');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer3','customer3@mail.com','900001003','Address 3');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer4','customer4@mail.com','900001004','Address 4');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer5','customer5@mail.com','900001005','Address 5');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer6','customer6@mail.com','900001006','Address 6');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer7','customer7@mail.com','900001007','Address 7');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer8','customer8@mail.com','900001008','Address 8');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer9','customer9@mail.com','900001009','Address 9');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer10','customer10@mail.com','900001010','Address 10');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer11','customer11@mail.com','900001011','Address 11');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer12','customer12@mail.com','900001012','Address 12');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer13','customer13@mail.com','900001013','Address 13');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer14','customer14@mail.com','900001014','Address 14');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer15','customer15@mail.com','900001015','Address 15');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer16','customer16@mail.com','900001016','Address 16');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer17','customer17@mail.com','900001017','Address 17');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer18','customer18@mail.com','900001018','Address 18');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer19','customer19@mail.com','900001019','Address 19');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer20','customer20@mail.com','900001020','Address 20');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer21','customer21@mail.com','900001021','Address 21');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer22','customer22@mail.com','900001022','Address 22');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer23','customer23@mail.com','900001023','Address 23');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer24','customer24@mail.com','900001024','Address 24');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer25','customer25@mail.com','900001025','Address 25');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer26','customer26@mail.com','900001026','Address 26');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer27','customer27@mail.com','900001027','Address 27');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer28','customer28@mail.com','900001028','Address 28');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer29','customer29@mail.com','900001029','Address 29');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer30','customer30@mail.com','900001030','Address 30');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer31','customer31@mail.com','900001031','Address 31');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer32','customer32@mail.com','900001032','Address 32');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer33','customer33@mail.com','900001033','Address 33');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer34','customer34@mail.com','900001034','Address 34');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer35','customer35@mail.com','900001035','Address 35');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer36','customer36@mail.com','900001036','Address 36');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer37','customer37@mail.com','900001037','Address 37');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer38','customer38@mail.com','900001038','Address 38');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer39','customer39@mail.com','900001039','Address 39');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer40','customer40@mail.com','900001040','Address 40');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer41','customer41@mail.com','900001041','Address 41');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer42','customer42@mail.com','900001042','Address 42');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer43','customer43@mail.com','900001043','Address 43');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer44','customer44@mail.com','900001044','Address 44');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer45','customer45@mail.com','900001045','Address 45');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer46','customer46@mail.com','900001046','Address 46');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer47','customer47@mail.com','900001047','Address 47');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer48','customer48@mail.com','900001048','Address 48');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer49','customer49@mail.com','900001049','Address 49');
INSERT INTO customers(name,email,phone,address) VALUES ('Customer50','customer50@mail.com','900001050','Address 50');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (1,'Health',3035.38,'2023-06-29','2024-06-28');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (2,'Health',4119.79,'2023-09-21','2024-09-20');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (3,'Life',4675.42,'2023-03-24','2024-03-23');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (4,'Health',1299.47,'2023-08-20','2024-08-19');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (5,'Health',1424.22,'2023-09-01','2024-08-31');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (6,'Home',1063.6,'2023-01-25','2024-01-25');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (7,'Life',1700.75,'2023-02-19','2024-02-19');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (8,'Life',1841.89,'2023-09-26','2024-09-25');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (9,'Home',1132.71,'2023-03-25','2024-03-24');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (10,'Home',4654.0,'2023-07-16','2024-07-15');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (11,'Auto',1275.69,'2023-04-28','2024-04-27');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (12,'Health',1717.38,'2023-07-24','2024-07-23');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (13,'Life',4508.63,'2023-10-27','2024-10-26');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (14,'Auto',3566.43,'2023-06-30','2024-06-29');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (15,'Health',4176.72,'2023-01-12','2024-01-12');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (16,'Health',4890.01,'2023-05-24','2024-05-23');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (17,'Home',4213.04,'2023-02-24','2024-02-24');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (18,'Health',2320.36,'2023-08-09','2024-08-08');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (19,'Health',1217.7,'2023-06-13','2024-06-12');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (20,'Life',4428.35,'2023-04-02','2024-04-01');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (21,'Auto',3951.74,'2023-01-14','2024-01-14');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (22,'Life',1609.5,'2023-05-03','2024-05-02');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (23,'Auto',3754.52,'2023-02-21','2024-02-21');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (24,'Home',4002.73,'2023-01-11','2024-01-11');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (25,'Auto',2417.69,'2023-04-04','2024-04-03');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (26,'Life',2693.85,'2023-09-06','2024-09-05');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (27,'Home',3707.24,'2023-06-12','2024-06-11');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (28,'Home',3315.52,'2023-04-28','2024-04-27');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (29,'Home',1108.32,'2023-04-01','2024-03-31');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (30,'Home',4320.06,'2023-02-09','2024-02-09');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (31,'Auto',4297.39,'2023-06-12','2024-06-11');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (32,'Home',3686.79,'2023-08-03','2024-08-02');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (33,'Life',1006.7,'2023-02-27','2024-02-27');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (34,'Home',4565.38,'2023-06-26','2024-06-25');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (35,'Auto',1307.73,'2023-01-05','2024-01-05');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (36,'Home',4513.67,'2023-03-10','2024-03-09');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (37,'Health',3947.9,'2023-06-05','2024-06-04');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (38,'Life',3933.89,'2023-06-09','2024-06-08');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (39,'Life',2403.34,'2023-07-14','2024-07-13');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (40,'Home',1510.05,'2023-09-25','2024-09-24');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (41,'Home',1838.24,'2023-06-23','2024-06-22');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (42,'Life',3974.82,'2023-01-23','2024-01-23');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (43,'Life',1380.11,'2023-05-08','2024-05-07');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (44,'Life',3527.89,'2023-06-30','2024-06-29');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (45,'Health',4919.4,'2023-01-28','2024-01-28');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (46,'Auto',2702.27,'2023-04-21','2024-04-20');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (47,'Auto',1176.27,'2023-07-28','2024-07-27');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (48,'Auto',4293.13,'2023-08-02','2024-08-01');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (49,'Home',4864.42,'2023-01-25','2024-01-25');
INSERT INTO policies(customer_id,policy_type,premium,start_date,end_date) VALUES (50,'Health',2550.31,'2023-03-16','2024-03-15');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (10,2329.39,'2023-10-19','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (4,8336.84,'2023-03-13','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (19,4745.93,'2023-06-06','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (19,2891.71,'2023-05-24','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (44,1220.67,'2023-01-03','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (8,6608.48,'2023-01-01','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (41,1666.64,'2023-01-05','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (42,1005.63,'2023-08-25','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (7,7580.9,'2023-07-04','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (9,5385.22,'2023-08-21','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (35,5152.28,'2023-01-25','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (39,6383.09,'2023-07-17','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (20,9069.12,'2023-07-04','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (43,7039.79,'2023-05-04','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (14,7769.25,'2023-07-09','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (17,5539.5,'2023-04-27','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (4,5656.64,'2023-10-11','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (4,8103.19,'2023-01-01','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (13,4999.76,'2023-06-07','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (48,9100.94,'2023-06-14','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (47,4128.89,'2023-04-10','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (4,7350.55,'2023-05-12','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (2,1613.5,'2023-03-03','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (43,5539.15,'2023-10-11','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (49,6146.9,'2023-02-24','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (32,6467.29,'2023-07-12','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (37,8356.18,'2023-07-22','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (50,3192.37,'2023-11-25','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (2,2761.38,'2023-05-19','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (28,8337.9,'2023-11-15','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (14,3951.02,'2023-07-29','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (20,5872.5,'2023-08-06','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (37,2919.56,'2023-06-27','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (3,7678.07,'2023-09-15','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (36,2078.95,'2023-07-08','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (22,1855.78,'2023-01-31','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (2,5097.7,'2023-07-23','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (40,7094.59,'2023-06-23','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (48,8131.41,'2023-01-01','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (12,8073.55,'2023-01-17','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (31,6150.84,'2023-03-04','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (14,1599.37,'2023-06-28','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (4,4954.54,'2023-03-11','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (46,7313.74,'2023-10-20','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (3,5796.43,'2023-04-23','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (48,4140.69,'2023-11-12','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (28,6390.36,'2023-08-17','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (12,9136.46,'2023-04-18','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (37,1029.11,'2023-07-21','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (41,7399.32,'2023-04-10','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (8,9509.84,'2023-02-23','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (18,3558.2,'2023-07-11','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (35,8059.61,'2023-06-17','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (2,770.95,'2023-04-26','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (22,6341.67,'2023-04-30','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (24,9071.02,'2023-11-02','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (49,7753.69,'2023-07-06','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (16,2335.72,'2023-07-11','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (26,7495.64,'2023-08-02','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (28,4734.71,'2023-09-29','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (36,5122.52,'2023-05-05','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (25,547.6,'2023-02-10','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (43,5566.73,'2023-08-24','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (20,6032.44,'2023-09-28','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (28,3536.39,'2023-05-05','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (27,4667.17,'2023-08-04','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (25,5300.27,'2023-09-15','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (44,9315.81,'2023-02-15','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (45,3693.54,'2023-03-24','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (45,6996.82,'2023-10-01','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (26,6282.53,'2023-02-03','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (25,1497.21,'2023-05-09','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (25,2232.73,'2023-08-29','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (18,3253.4,'2023-11-16','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (16,9034.08,'2023-06-15','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (6,3270.05,'2023-11-13','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (17,4581.01,'2023-06-29','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (41,7892.75,'2023-06-08','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (29,8072.88,'2023-01-17','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (39,7239.32,'2023-01-15','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (29,5196.48,'2023-07-02','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (44,514.83,'2023-07-25','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (10,1114.47,'2023-09-06','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (17,1979.08,'2023-11-22','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (17,2265.68,'2023-05-23','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (31,9068.96,'2023-06-06','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (1,1306.69,'2023-03-31','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (32,4989.94,'2023-01-09','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (27,8329.48,'2023-07-10','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (18,8404.85,'2023-02-22','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (32,3835.35,'2023-01-15','Approved');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (7,3964.02,'2023-08-25','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (42,5408.43,'2023-04-01','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (16,3863.6,'2023-04-28','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (15,6938.29,'2023-11-06','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (26,5418.21,'2023-10-27','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (23,8872.81,'2023-03-01','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (43,9336.44,'2023-09-09','Rejected');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (16,2961.18,'2023-08-13','Pending');
INSERT INTO claims(policy_id,claim_amount,claim_date,status) VALUES (43,6924.61,'2023-05-01','Rejected');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (1,4480.22,'2023-06-24','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (2,4352.87,'2023-07-13','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (3,3151.3,'2023-05-02','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (4,4853.76,'2023-07-18','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (5,3631.0,'2023-04-04','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (6,3278.43,'2023-09-06','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (7,2544.27,'2023-08-14','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (8,2794.79,'2023-05-31','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (9,2981.43,'2023-10-26','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (10,4006.7,'2023-05-03','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (11,2403.51,'2023-05-14','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (12,1287.85,'2023-10-22','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (13,3347.39,'2023-07-03','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (14,1713.31,'2023-08-05','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (15,3991.38,'2023-05-06','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (16,4137.3,'2023-09-28','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (17,4493.55,'2023-07-13','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (18,748.34,'2023-04-04','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (19,696.09,'2023-06-14','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (20,3628.06,'2023-02-19','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (21,4411.46,'2023-09-09','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (22,4205.58,'2023-06-28','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (23,2252.45,'2023-10-28','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (24,2427.24,'2023-10-25','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (25,1974.02,'2023-10-29','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (26,2786.83,'2023-06-16','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (27,555.77,'2023-06-17','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (28,1949.36,'2023-09-06','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (29,3040.99,'2023-07-08','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (30,3332.91,'2023-09-16','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (31,1097.48,'2023-08-16','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (32,1073.53,'2023-11-19','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (33,4201.92,'2023-03-01','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (34,2537.65,'2023-03-06','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (35,3216.54,'2023-04-30','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (36,2813.76,'2023-03-03','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (37,1959.47,'2023-10-17','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (38,2115.06,'2023-07-23','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (39,2521.33,'2023-05-21','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (40,2385.93,'2023-09-08','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (41,1316.43,'2023-11-15','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (42,815.79,'2023-03-05','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (43,2187.11,'2023-04-23','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (44,3317.74,'2023-08-25','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (45,915.66,'2023-04-02','Card');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (46,1703.92,'2023-06-15','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (47,4524.69,'2023-05-01','NetBanking');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (48,3811.5,'2023-07-16','UPI');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (49,2618.3,'2023-01-14','Cash');
INSERT INTO payments(policy_id,amount,payment_date,method) VALUES (50,2139.88,'2023-06-10','Cash');


