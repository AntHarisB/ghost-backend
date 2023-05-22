USE Project;

SELECT * FROM auth_user;
SELECT * FROM performancetab_projectinformation WHERE year=2023;
SELECT * FROM performancetab_projectinformation_members;

DELETE FROM performancetab_projectinformation;

INSERT INTO performancetab_projectinformation (id, project_name, project_value, team_size, velocity, weeks_over_ddl, hourly_price, year, lead_closing, project_creation, type_of_project, hours_available, hours_billed, costs_actual, costs_planned, project_value_planned)
VALUES 
('1', 'Projekat 1', '152128.49', '4', '5', '17', '72', '2022', '14.08', 'preporuka', 'fixed', '672', '945', '140580.00', '120000.22', '170180.13'),
('2', 'Projekat 2', '262867.34', '9', '9', '10', '47', '2019', '17.32', 'prodaja', 'on-going', '635', '532', '2502300.00', '281000.04', '267700.20'),
('3', 'Projekat 3', '371771.85', '10', '3', '3', '55', '2021', '16.23', 'partnerstvo', 'fixed', '735', '934', '361200.11', '401500.20', '381600.44'),
('4', 'Projekat 4', '934414.41', '5', '6', '7', '16', '2022', '19.44', 'preporuka', 'on-going', '611', '294', '900770.66', '801200.30', '927700.05'),
('5', 'Projekat 5', '680129.91', '1', '4', '10', '52', '2023', '12.76', 'preporuka', 'fixed', '694', '319', '670120.13', '691500.11', '650152.85'),
('6', 'Projekat 6', '205986.97', '2', '7', '28', '69', '2019', '6.12', 'preporuka', 'fixed', '667', '605', '200300.00', '221800.00', '190210.10'),
('7', 'Projekat 7', '314216.45', '8', '2', '19', '49', '2020', '8.68', 'preporuka', 'on-going', '286', '632', '320170.00', '304450.05', '315670.10'),
('8', 'Projekat 8', '768675.15', '4', '4', '10', '28', '2021', '8.11', 'prodaja', 'fixed', '587', '527', '751100.11', '766700.02', '780340.90'),
('9', 'Projekat 9', '722658.63', '3', '3', '7', '11', '2020', '11.26', 'preporuka', 'fixed', '229', '58', '700011.10', '710960.00', '720870.04'),
('10', 'Projekat 10', '410089.76', '6', '8', '26', '89', '2022', '15.21', 'partnerstvo', 'on-going', '226', '744', '400220.10', '410020.06', '425500.02'),
('11', 'Projekat 11', '353126.91', '5', '7', '16', '33', '2019', '12.31', 'preporuka', 'on-going', '192', '76', '351100.02', '370350.60', '360660.09'),
('12', 'Projekat 12', '688529.11', '4', '3', '10', '60', '2021', '15.76', 'preporuka', 'on-going', '383', '400', '689700.07', '700770.10', '690025.10'),
('13', 'Projekat 13', '287090.71', '8', '10', '9', '44', '2020', '8.65', 'prodaja', 'on-going', '310', '465', '300120.00', '280300.40', '320000.00'),
('14', 'Projekat 14', '904936.12', '2', '5', '13', '71', '2023', '14.59', 'partnerstvo', 'on-going', '402', '418', '900170.20', '920180.40', '911900.05'),
('15', 'Projekat 15', '35090.71', '4', '6', '6', '21', '2020', '8.65', 'prodaja', 'on-going', '211', '417', '32220.50', '35220.40', '33020.40');

INSERT INTO performancetab_projectinformation (id, project_name, project_value, team_size, velocity, weeks_over_ddl, hourly_price, year, lead_closing, project_creation, type_of_project, hours_available, hours_billed, costs_actual, costs_planned, project_value_planned)
VALUES 
('16', 'Projekat 16', '235090.81', '6', '3', '5', '21', '2019', '8.85', 'prodaja', 'on-going', '211', '417', '232220.50', '135220.40', '133020.40'),
('17', 'Projekat 17', '135090.71', '4', '6', '4', '21', '2019', '6.65', 'partnerstvo', 'fixed', '159', '306', '232220.50', '135220.40', '133020.40'),
('18', 'Projekat 18', '205986.97', '8', '3', '5', '21', '2020', '8.85', 'preporuka', 'fixed', '211', '417', '1405800.00', '135220.40', '133020.40'),
('19', 'Projekat 19', '215986.97', '4', '6', '8', '21', '2020', '6.65', 'partnerstvo', 'on-going', '112', '208', '1485800.00', '175220.40', '253020.40'),
('20', 'Projekat 20', '135090.71', '5', '7', '4', '21', '2021', '6.65', 'partnerstvo', 'fixed', '159', '306', '232220.50', '135220.40', '133020.40'),
('21', 'Projekat 21', '215986.97', '4', '6', '4', '21', '2021', '6.65', 'preporuka', 'on-going', '175', '306', '1485800.00', '175220.40', '253020.40'),
('22', 'Projekat 22', '205090.71', '8', '6', '8', '21', '2022', '6.65', 'prodaja', 'on-going', '159', '217', '199220.50', '215220.50', '203020.40'),
('23', 'Projekat 23', '335090.71', '4', '5', '4', '21', '2022', '6.65', 'preporuka', 'fixed', '166', '311', '332720.50', '335220.40', '337020.40'),
('24', 'Projekat 24', '185090.71', '7', '6', '5', '21', '2023', '6.65', 'preporuka', 'on-going', '141', '306', '182220.50', '185220.40', '183020.40'),
('25', 'Projekat 25', '215090.71', '4', '9', '4', '21', '2023', '6.65', 'partnerstvo', 'fixed', '159', '309', '212220.50', '215220.40', '213020.40'),
('26', 'Projekat 26', '165090.71', '3', '6', '2', '21', '2023', '6.65', 'prodaja', 'on-going', '133', '306', '182220.50', '165220.40', '183020.40');

UPDATE performancetab_projectinformation SET date_start = '2019-01-01' WHERE id = 2;
UPDATE performancetab_projectinformation SET date_start = '2019-05-01' WHERE id = 6;
UPDATE performancetab_projectinformation SET date_start = '2019-10-01' WHERE id = 11;
UPDATE performancetab_projectinformation SET date_end = '2019-04-20' WHERE id = 2;
UPDATE performancetab_projectinformation SET date_end = '2019-09-01' WHERE id = 6;
UPDATE performancetab_projectinformation SET date_end = '2019-12-20' WHERE id = 11;


UPDATE performancetab_projectinformation SET date_start = '2020-02-01' WHERE id = 7;
UPDATE performancetab_projectinformation SET date_start = '2020-05-01' WHERE id = 9;
UPDATE performancetab_projectinformation SET date_start = '2020-08-01' WHERE id = 13;
UPDATE performancetab_projectinformation SET date_start = '2020-11-01' WHERE id = 15;
UPDATE performancetab_projectinformation SET date_end = '2020-04-11' WHERE id = 7;
UPDATE performancetab_projectinformation SET date_end = '2020-07-23' WHERE id = 9;
UPDATE performancetab_projectinformation SET date_end = '2020-10-10' WHERE id = 13;
UPDATE performancetab_projectinformation SET date_end = '2020-12-18' WHERE id = 15;


UPDATE performancetab_projectinformation SET date_start = '2021-03-01' WHERE id = 3;
UPDATE performancetab_projectinformation SET date_start = '2021-06-01' WHERE id = 8;
UPDATE performancetab_projectinformation SET date_start = '2021-10-01' WHERE id = 12;
UPDATE performancetab_projectinformation SET date_end = '2021-05-21' WHERE id = 3;
UPDATE performancetab_projectinformation SET date_end = '2021-09-09' WHERE id = 8;
UPDATE performancetab_projectinformation SET date_end = '2021-11-30' WHERE id = 12;


UPDATE performancetab_projectinformation SET date_start = '2022-02-01' WHERE id = 1;
UPDATE performancetab_projectinformation SET date_start = '2022-06-01' WHERE id = 4;
UPDATE performancetab_projectinformation SET date_start = '2022-09-01' WHERE id = 10;
UPDATE performancetab_projectinformation SET date_end = '2022-05-11' WHERE id = 1;
UPDATE performancetab_projectinformation SET date_end = '2022-08-26' WHERE id = 4;
UPDATE performancetab_projectinformation SET date_end = '2022-11-29' WHERE id = 10;


UPDATE performancetab_projectinformation SET date_start = '2023-01-01' WHERE id = 5;
UPDATE performancetab_projectinformation SET date_start = '2023-02-01' WHERE id = 14;
UPDATE performancetab_projectinformation SET date_end = '2023-03-21' WHERE id = 5;
UPDATE performancetab_projectinformation SET date_end = '2023-05-11' WHERE id = 14;

UPDATE performancetab_projectinformation SET date_start = '2019-04-01' WHERE id = 16;
UPDATE performancetab_projectinformation SET date_start = '2019-06-01' WHERE id = 17;
UPDATE performancetab_projectinformation SET date_end = '2019-06-02' WHERE id = 16;
UPDATE performancetab_projectinformation SET date_end = '2019-08-21' WHERE id = 17;

UPDATE performancetab_projectinformation SET date_start = '2020-04-01' WHERE id = 18;
UPDATE performancetab_projectinformation SET date_start = '2020-06-05' WHERE id = 19;
UPDATE performancetab_projectinformation SET date_end = '2020-06-22' WHERE id = 18;
UPDATE performancetab_projectinformation SET date_end = '2020-08-11' WHERE id = 19;

UPDATE performancetab_projectinformation SET date_start = '2021-04-01' WHERE id = 20;
UPDATE performancetab_projectinformation SET date_start = '2021-05-05' WHERE id = 21;
UPDATE performancetab_projectinformation SET date_end = '2021-06-21' WHERE id = 20;
UPDATE performancetab_projectinformation SET date_end = '2021-07-18' WHERE id = 21;

UPDATE performancetab_projectinformation SET date_start = '2022-04-07' WHERE id = 22;
UPDATE performancetab_projectinformation SET date_start = '2022-05-02' WHERE id = 23;
UPDATE performancetab_projectinformation SET date_end = '2022-06-18' WHERE id = 22;
UPDATE performancetab_projectinformation SET date_end = '2022-07-11' WHERE id = 23;

UPDATE performancetab_projectinformation SET date_start = '2023-04-07' WHERE id = 24;
UPDATE performancetab_projectinformation SET date_start = '2023-05-08' WHERE id = 25;
UPDATE performancetab_projectinformation SET date_start = '2023-06-09' WHERE id = 26;
UPDATE performancetab_projectinformation SET date_end = '2023-06-10' WHERE id = 24;
UPDATE performancetab_projectinformation SET date_end = NULL WHERE id = 25;
UPDATE performancetab_projectinformation SET date_end = NULL WHERE id = 26;

UPDATE performancetab_projectinformation
SET development = '1300000.00',
    design = '2150500.00',
    other = '31000000.00',
    total_revenue = '1900000.00',
    direct = '3900000.00',
    indirect = '1755600.00',
    marketing = '7480200.00',
    HRcost = '287050.00',
    officeCost = '211100.00',
    salesCosts = '99850.00',
    otherCosts = '648.00'
WHERE id = 5;

UPDATE performancetab_projectinformation
SET development = '1300000.00',
    design = '2150500.00',
    other = '31000000.00',
    total_revenue = '1900000.00',
    direct = '3900000.00',
    indirect = '1755600.00',
    marketing = '7480200.00',
    HRcost = '287050.00',
    officeCost = '211100.00',
    salesCosts = '99850.00',
    otherCosts = '648.00'
WHERE id = 5;

UPDATE performancetab_projectinformation
SET development = CASE
        WHEN id = 14 THEN '1300000.00'
        WHEN id = 24 THEN '1500000.00'
        WHEN id = 25 THEN '1400000.00'
        WHEN id = 26 THEN '1600000.00'
        ELSE development
    END,
    design = CASE
        WHEN id = 14 THEN '2150500.00'
        WHEN id = 24 THEN '2200000.00'
        WHEN id = 25 THEN '2100000.00'
        WHEN id = 26 THEN '2300000.00'
        ELSE design
    END,
    other = CASE
        WHEN id = 14 THEN '31000000.00'
        WHEN id = 24 THEN '32000000.00'
        WHEN id = 25 THEN '30000000.00'
        WHEN id = 26 THEN '33000000.00'
        ELSE other
    END,
    total_revenue = CASE
        WHEN id = 14 THEN '1900000.00'
        WHEN id = 24 THEN '2000000.00'
        WHEN id = 25 THEN '1800000.00'
        WHEN id = 26 THEN '2100000.00'
        ELSE total_revenue
    END,
    direct = CASE
        WHEN id = 14 THEN '3650000.00'
        WHEN id = 24 THEN '4100100.00'
        WHEN id = 25 THEN '4000500.00'
        WHEN id = 26 THEN '3960300.00'
        ELSE other
    END,
    indirect = CASE
        WHEN id = 14 THEN '1650000.00'
        WHEN id = 24 THEN '1730605.00'
        WHEN id = 25 THEN '1420300.00'
        WHEN id = 26 THEN '1690900.00'
        ELSE other
    END,
    marketing = CASE
        WHEN id = 14 THEN '7960000.00'
        WHEN id = 24 THEN '8350000.00'
        WHEN id = 25 THEN '8102200.00'
        WHEN id = 26 THEN '7900800.00'
        ELSE other
    END,
    HRcost = CASE
        WHEN id = 14 THEN '460800.00'
        WHEN id = 24 THEN '450200.00'
        WHEN id = 25 THEN '510050.00'
        WHEN id = 26 THEN '500200.00'
        ELSE other
    END,
    officeCost = CASE
        WHEN id = 14 THEN '98600.00'
        WHEN id = 24 THEN '101200.00'
        WHEN id = 25 THEN '100500.00'
        WHEN id = 26 THEN '97050.00'
        ELSE other
    END,
    salesCosts = CASE
        WHEN id = 14 THEN '53000.00'
        WHEN id = 24 THEN '51200.00'
        WHEN id = 25 THEN '52630.00'
        WHEN id = 26 THEN '49800.00'
        ELSE other
    END,
    otherCosts = CASE
        WHEN id = 14 THEN '750.00'
        WHEN id = 24 THEN '610.00'
        WHEN id = 25 THEN '930.00'
        WHEN id = 26 THEN '775.00'
        ELSE other
    END
WHERE id IN (14, 24, 25, 26);

