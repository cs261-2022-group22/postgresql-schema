DROP TABLE IF EXISTS Skill CASCADE;
CREATE TABLE Skill (
  skillId SERIAL PRIMARY KEY,
  name VARCHAR
);

DROP TABLE IF EXISTS BusinessSector CASCADE;
CREATE TABLE BusinessSector (
  businessSectorId SERIAL PRIMARY KEY,
  name VARCHAR
);

DROP TABLE IF EXISTS WebsiteFeedback CASCADE;
CREATE TABLE WebsiteFeedback (
  websiteFeedbackId SERIAL PRIMARY KEY,
  message VARCHAR
);

DROP TABLE IF EXISTS Account CASCADE;
CREATE TABLE Account (
  accountId SERIAL PRIMARY KEY,
  name VARCHAR,
  email VARCHAR UNIQUE,
  passwordHash BYTEA,
  dob DATE,
  businessSectorId INTEGER REFERENCES BusinessSector(businessSectorId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Mentor CASCADE;
CREATE TABLE Mentor (
  mentorId SERIAL PRIMARY KEY,
  accountId INTEGER REFERENCES Account(accountId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS MentorSkill CASCADE;
CREATE TABLE MentorSkill (
  mentorSkillId SERIAL PRIMARY KEY,
  mentorId INTEGER REFERENCES Mentor(mentorId) ON DELETE CASCADE,
  skillId INTEGER REFERENCES Skill(skillId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Mentee CASCADE;
CREATE TABLE Mentee (
  menteeId SERIAL PRIMARY KEY,
  accountId INTEGER REFERENCES Account(accountId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS MenteeSkill CASCADE;
CREATE TABLE MenteeSkill (
  menteeSkillId SERIAL PRIMARY KEY,
  menteeId INTEGER REFERENCES Mentee(menteeId) ON DELETE CASCADE,
  skillId INTEGER REFERENCES Skill(skillId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Assignment CASCADE;
CREATE TABLE Assignment (
  assignmentId SERIAL PRIMARY KEY,
  mentorId INTEGER REFERENCES Mentor(mentorId) ON DELETE CASCADE,
  menteeId INTEGER REFERENCES Mentee(menteeId) ON DELETE CASCADE
);

DROP TABLE IF EXISTS DevelopmentFeedback CASCADE;
CREATE TABLE DevelopmentFeedback (
  developmentFeedbackId SERIAL PRIMARY KEY,
  assignmentId INTEGER REFERENCES Assignment(assignmentId) ON DELETE CASCADE,
  content VARCHAR
);

DROP TABLE IF EXISTS Meeting CASCADE;
CREATE TABLE Meeting (
  meetingId SERIAL PRIMARY KEY,
  assignmentId INTEGER REFERENCES Assignment(assignmentId) ON DELETE CASCADE,
  link VARCHAR,
  start TIMESTAMP,
  duration INTEGER /* in minutes */
);

DROP TABLE IF EXISTS MenteeMessage CASCADE;
CREATE TABLE MenteeMessage (
  menteeMessageId SERIAL PRIMARY KEY,
  menteeId INTEGER REFERENCES Mentee(menteeId) ON DELETE CASCADE,
  message VARCHAR
);

DROP TABLE IF EXISTS MentorMessage CASCADE;
CREATE TABLE MentorMessage (
  mentorMessageId SERIAL PRIMARY KEY,
  mentorId INTEGER REFERENCES Mentor(mentorId) ON DELETE CASCADE,
  message VARCHAR
);

DROP TABLE IF EXISTS MentorFeedback CASCADE;
CREATE TABLE MentorFeedback (
  mentorFeedbackId SERIAL PRIMARY KEY,
  assignmentId INTEGER REFERENCES Assignment(assignmentId) ON DELETE CASCADE,
  rating DOUBLE PRECISION
);

DROP TABLE IF EXISTS MenteeFeedback CASCADE;
CREATE TABLE MenteeFeedback (
  menteeFeedbackId SERIAL PRIMARY KEY,
  assignmentId INTEGER REFERENCES Assignment(assignmentId) ON DELETE CASCADE,
  rating DOUBLE PRECISION
);

DROP TABLE IF EXISTS Milestone CASCADE;
CREATE TABLE Milestone (
  milestoneId SERIAL PRIMARY KEY,
  menteeId INTEGER REFERENCES Mentee(menteeId) ON DELETE CASCADE,
  content VARCHAR,
  completed BOOLEAN
);

DROP TABLE IF EXISTS Workshop CASCADE;
CREATE TABLE Workshop (
  workshopId SERIAL PRIMARY KEY,
  skillId INTEGER REFERENCES Skill(skillId) ON DELETE CASCADE,
  link VARCHAR,
  start TIMESTAMP,
  duration INTEGER /* in minutes */
);

DROP TABLE IF EXISTS RatingModel CASCADE;
CREATE TABLE RatingModel (
    businessArea1Id INTEGER,
    businessArea2Id INTEGER,
    skillOverlapCoefficient DOUBLE PRECISION,
    ageDifferenceCoefficient DOUBLE PRECISION,
    modelOffset DOUBLE PRECISION,
    CONSTRAINT businessAreaOrdering CHECK (businessarea1id < businessarea2id)
);

DROP TABLE IF EXISTS PendingRatingFeedback CASCADE;
CREATE TABLE PendingRatingFeedback (
    businessArea1Id INTEGER, 
    businessArea2Id INTEGER, 
    skillOverlap INTEGER, 
    ageDifference INTEGER, 
    rating DOUBLE PRECISION, 
    CONSTRAINT businessAreaOrdering CHECK (businessarea1id < businessarea2id)
);

DROP TABLE IF EXISTS PendingTextFeedback CASCADE;
CREATE TABLE PendingTextFeedback (
    businessArea1Id INTEGER, 
    businessArea2Id INTEGER, 
    skillOverlap INTEGER, 
    ageDifference INTEGER, 
    content VARCHAR, 
    CONSTRAINT businessAreaOrdering CHECK (businessarea1id < businessarea2id)
);

ALTER SEQUENCE skill_skillid_seq RESTART WITH 1001;
ALTER SEQUENCE businesssector_businesssectorid_seq RESTART WITH 1001;
ALTER SEQUENCE websitefeedback_websitefeedbackid_seq RESTART WITH 1001;
ALTER SEQUENCE developmentfeedback_developmentfeedbackid_seq RESTART WITH 1001;
ALTER SEQUENCE account_accountid_seq RESTART WITH 1001;
ALTER SEQUENCE mentor_mentorid_seq RESTART WITH 1001;
ALTER SEQUENCE mentorskill_mentorskillid_seq RESTART WITH 1001;
ALTER SEQUENCE mentee_menteeid_seq RESTART WITH 1001;
ALTER SEQUENCE menteeskill_menteeskillid_seq RESTART WITH 1001;
ALTER SEQUENCE assignment_assignmentid_seq RESTART WITH 1001;
ALTER SEQUENCE meeting_meetingid_seq RESTART WITH 1001;
ALTER SEQUENCE menteemessage_menteemessageid_seq RESTART WITH 1001;
ALTER SEQUENCE mentormessage_mentormessageid_seq RESTART WITH 1001;
ALTER SEQUENCE mentorfeedback_mentorfeedbackid_seq RESTART WITH 1001;
ALTER SEQUENCE menteefeedback_menteefeedbackid_seq RESTART WITH 1001;
ALTER SEQUENCE milestone_milestoneid_seq RESTART WITH 1001;
ALTER SEQUENCE workshop_workshopid_seq RESTART WITH 1001;
