USE Project;

SELECT * FROM performancetab_projectinformation;

INSERT INTO performancetab_projectinformation (id, project_name, project_value, team_size, velocity, weeks_over_ddl, hourly_price, year, lead_closing, project_creation, type_of_project, hours_available, hours_billed)
VALUES 
('1', 'Projekat 1', '152128.49', '4', '5', '17', '72', '2022', '14.08', 'preporuka', 'fixed', '672', '945', '2022-05-11', '2022-02-01'),
('2', 'Projekat 2', '262867.34', '9', '9', '10', '47', '2019', '17.32', 'prodaja', 'on-going', '635', '532', '2019-04-20', '2019-01-01'),
('3', 'Projekat 3', '371771.85', '10', '3', '3', '55', '2021', '16.23', 'partnerstvo', 'fixed', '735', '934', '2021-05-21', '2021-03-01'),
('4', 'Projekat 4', '934414.41', '5', '6', '7', '16', '2022', '19.44', 'preporuka', 'on-going', '611', '294', '2022-08-26', '2022-06-01'),
('5', 'Projekat 5', '680129.91', '1', '4', '10', '52', '2023', '12.76', 'preporuka', 'fixed', '694', '319', '2023-03-21', '2023-01-01'),
('6', 'Projekat 6', '205986.97', '2', '7', '28', '69', '2019', '6.12', 'preporuka', 'fixed', '667', '605', '2019-09-01', '2019-05-01'),
('7', 'Projekat 7', '314216.45', '8', '2', '19', '49', '2020', '8.68', 'preporuka', 'on-going', '286', '632', '2020-04-11', '2020-02-01'),
('8', 'Projekat 8', '768675.15', '4', '4', '10', '28', '2021', '8.11', 'prodaja', 'fixed', '587', '527', '2021-09-09', '2021-06-01'),
('9', 'Projekat 9', '722658.63', '3', '3', '7', '11', '2020', '11.26', 'preporuka', 'fixed', '229', '58', '2020-07-23', '2020-05-01'),
('10', 'Projekat 10', '410089.76', '6', '8', '26', '89', '2022', '15.21', 'partnerstvo', 'on-going', '226', '744', '2022-11-29', '2022-09-01'),
('11', 'Projekat 11', '353126.91', '5', '7', '16', '33', '2019', '12.31', 'preporuka', 'on-going', '192', '76', '2019-12-20', '2019-10-01'),
('12', 'Projekat 12', '688529.11', '4', '3', '10', '60', '2021', '15.76', 'preporuka', 'on-going', '383', '400', '2021-11-30', '2021-10-01'),
('13', 'Projekat 13', '287090.71', '8', '10', '9', '44', '2020', '8.65', 'prodaja', 'on-going', '310', '465', '2020-10-10', '2020-08-01'),
('14', 'Projekat 14', '904936.12', '2', '5', '13', '71', '2023', '14.59', 'partnerstvo', 'on-going', '402', '418', NULL, '2023-04-01'),
('15', 'Projekat 15', '35090.71', '4', '6', '6', '21', '2020', '8.65', 'prodaja', 'on-going', '211', '417', '2020-12-18', '2020-11-01');

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
UPDATE performancetab_projectinformation SET date_start = '2023-04-01' WHERE id = 14;
UPDATE performancetab_projectinformation SET date_end = '2023-03-21' WHERE id = 5;



