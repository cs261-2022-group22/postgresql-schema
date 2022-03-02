--
-- Business Sectors
--
INSERT INTO businesssector (businesssectorid, name) VALUES (1, 'Private Banking');
INSERT INTO businesssector (businesssectorid, name) VALUES (2, 'Sector 2');
INSERT INTO businesssector (businesssectorid, name) VALUES (3, 'Sector 3');
INSERT INTO businesssector (businesssectorid, name) VALUES (4, 'Sector 4');
INSERT INTO businesssector (businesssectorid, name) VALUES (5, 'Sector 5');
INSERT INTO businesssector (businesssectorid, name) VALUES (6, 'Sector 6');
INSERT INTO businesssector (businesssectorid, name) VALUES (7, 'Sector 7');
INSERT INTO businesssector (businesssectorid, name) VALUES (8, 'Sector 8');
INSERT INTO businesssector (businesssectorid, name) VALUES (9, 'Sector 9');

--
-- Mentees Account
--
INSERT INTO Account VALUES (10000, 'Mentee Doe', 'test-mentee@gmail.com', E'\\x243262243132245159367569413552717a613166754f4b533478524c4f5041724a33645270774970376f334e703671324f44524c4859424256755632', DATE '1999-01-01', 1);
INSERT INTO account VALUES (10001, 'Test Mentee 02', 'Mentee-02@mooody.me', null::bytea, '2022-03-02'::date, 2);
INSERT INTO account VALUES (10002, 'Test Mentee 03', 'Mentee-03@mooody.me', null::bytea, '2022-03-02'::date, 3);
INSERT INTO account VALUES (10003, 'Test Mentee 04', 'Mentee-04@mooody.me', null::bytea, '2022-03-02'::date, 5);
INSERT INTO account VALUES (10004, 'Test Mentee 05', 'Mentee-05@mooody.me', null::bytea, '2022-03-02'::date, 1);
INSERT INTO account VALUES (10005, 'Test Mentee 06', 'Mentee-06@mooody.me', null::bytea, '2022-03-02'::date, 7);
INSERT INTO account VALUES (10006, 'Test Mentee 07', 'Mentee-07@mooody.me', null::bytea, '2022-03-02'::date, 6);
INSERT INTO account VALUES (10007, 'Test Mentee 08', 'Mentee-08@mooody.me', null::bytea, '2022-03-02'::date, 7);
INSERT INTO account VALUES (10008, 'Test Mentee 09', 'Mentee-09@mooody.me', null::bytea, '2022-03-02'::date, 9);
INSERT INTO account VALUES (10009, 'Test Mentee 10', 'Mentee-10@mooody.me', null::bytea, '2022-03-02'::date, 1);
INSERT INTO account VALUES (10010, 'Test Mentee 11', 'Mentee-11@mooody.me', null::bytea, '2022-03-02'::date, 8);
INSERT INTO account VALUES (10011, 'Test Mentee 12', 'Mentee-12@mooody.me', null::bytea, '2022-03-02'::date, 2);
INSERT INTO account VALUES (10012, 'Test Mentee 13', 'Mentee-13@mooody.me', null::bytea, '2022-03-02'::date, 4);

--
-- Mentees
--
INSERT INTO mentee (menteeid, accountid) VALUES (1,  10000);
INSERT INTO mentee (menteeid, accountid) VALUES (2,  10001);
INSERT INTO mentee (menteeid, accountid) VALUES (3,  10002);
INSERT INTO mentee (menteeid, accountid) VALUES (4,  10003);
INSERT INTO mentee (menteeid, accountid) VALUES (5,  10004);
INSERT INTO mentee (menteeid, accountid) VALUES (6,  10005);
INSERT INTO mentee (menteeid, accountid) VALUES (7,  10006);
INSERT INTO mentee (menteeid, accountid) VALUES (8,  10007);
INSERT INTO mentee (menteeid, accountid) VALUES (9,  10008);
INSERT INTO mentee (menteeid, accountid) VALUES (10, 10009);
INSERT INTO mentee (menteeid, accountid) VALUES (11, 10010);
INSERT INTO mentee (menteeid, accountid) VALUES (12, 10011);
INSERT INTO mentee (menteeid, accountid) VALUES (13, 10012);

--
-- Mentors Account
--
INSERT INTO Account VALUES (20000, 'John Doe', 'test@gmail.com', E'\\x243262243132245159367569413552717a613166754f4b533478524c4f5041724a33645270774970376f334e703671324f44524c4859424256755632', DATE '1999-01-01', 1);
INSERT INTO account VALUES (20001, 'Test Mentor 02', 'Mentor-02@mooody.me', null::bytea, '2022-03-02'::date, 4);
INSERT INTO account VALUES (20002, 'Test Mentor 03', 'Mentor-03@mooody.me', null::bytea, '2022-03-02'::date, 7);
INSERT INTO account VALUES (20003, 'Test Mentor 04', 'Mentor-04@mooody.me', null::bytea, '2022-03-02'::date, 9);
INSERT INTO account VALUES (20004, 'Test Mentor 05', 'Mentor-05@mooody.me', null::bytea, '2022-03-02'::date, 9);
INSERT INTO account VALUES (20005, 'Test Mentor 06', 'Mentor-06@mooody.me', null::bytea, '2022-03-02'::date, 5);
INSERT INTO account VALUES (20006, 'Test Mentor 07', 'Mentor-07@mooody.me', null::bytea, '2022-03-02'::date, 1);
INSERT INTO account VALUES (20007, 'Test Mentor 08', 'Mentor-08@mooody.me', null::bytea, '2022-03-02'::date, 8);
INSERT INTO account VALUES (20008, 'Test Mentor 09', 'Mentor-09@mooody.me', null::bytea, '2022-03-02'::date, 2);
INSERT INTO account VALUES (20009, 'Test Mentor 10', 'Mentor-10@mooody.me', null::bytea, '2022-03-02'::date, 6);
INSERT INTO account VALUES (20010, 'Test Mentor 11', 'Mentor-11@mooody.me', null::bytea, '2022-03-02'::date, 2);
INSERT INTO account VALUES (20011, 'Test Mentor 12', 'Mentor-12@mooody.me', null::bytea, '2022-03-02'::date, 3);
INSERT INTO account VALUES (20012, 'Test Mentor 13', 'Mentor-13@mooody.me', null::bytea, '2022-03-02'::date, 3);

--
-- Mentors
--
INSERT INTO mentor (mentorid, accountid) VALUES (1,  20000);
INSERT INTO mentor (mentorid, accountid) VALUES (2,  20001);
INSERT INTO mentor (mentorid, accountid) VALUES (3,  20002);
INSERT INTO mentor (mentorid, accountid) VALUES (4,  20003);
INSERT INTO mentor (mentorid, accountid) VALUES (5,  20004);
INSERT INTO mentor (mentorid, accountid) VALUES (6,  20005);
INSERT INTO mentor (mentorid, accountid) VALUES (7,  20006);
INSERT INTO mentor (mentorid, accountid) VALUES (8,  20007);
INSERT INTO mentor (mentorid, accountid) VALUES (9,  20008);
INSERT INTO mentor (mentorid, accountid) VALUES (10, 20009);
INSERT INTO mentor (mentorid, accountid) VALUES (11, 20010);
INSERT INTO mentor (mentorid, accountid) VALUES (12, 20011);
INSERT INTO mentor (mentorid, accountid) VALUES (13, 20012);

--
-- Assignments
--

-- Mentor 1 (John Doe) has already got 5 assignments, so cannot be chosen anymore.
INSERT INTO assignment VALUES (1, 1, 1);
INSERT INTO assignment VALUES (2, 1, 2);
INSERT INTO assignment VALUES (3, 1, 3);
INSERT INTO assignment VALUES (4, 1, 4);
INSERT INTO assignment VALUES (5, 1, 5);


--
-- Mentor Messages
--
INSERT INTO MentorMessage VALUES(1, 1, 'notification1');
INSERT INTO MentorMessage VALUES(2, 1, 'notification2');
INSERT INTO MentorMessage VALUES(3, 1, 'notification3');
