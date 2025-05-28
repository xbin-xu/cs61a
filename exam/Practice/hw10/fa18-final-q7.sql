-- 7. (10 points) SQL of Course
-- The courses table describes the course name, start time hour (h) and
-- minute (m), and length in minutes (len) for different lectures.
-- For example, 61A starts at 13:00 and lasts 50 minutes.
-- The locations table describes the course name and location (loc) of these
-- courses. Assume that each course name appears exactly once in each table.
-- Write your SQL statements so that they would still be correct
-- if the table contents changed.

CREATE TABLE courses AS
    SELECT "1" AS course, 14 AS h, 0 AS m, 80 AS len UNION
    SELECT "2",           13,      30,     80        UNION
    SELECT "8",           12,      30,     50        UNION
    SELECT "10",          12,      30,     110       UNION
    SELECT "50AC",        13,      30,     45        UNION
    SELECT "61A",         13,      0,      50;

CREATE TABLE locations AS
    SELECT "1" AS name, "VLSB" AS loc UNION
    SELECT "2",         "Dwinelle"    UNION
    SELECT "10",        "VLSB"        UNION
    SELECT "50AC",      "Wheeler"     UNION
    SELECT "61A",       "Wheeler";


-- (a) (2 pt) Select a one-column table that contains the course names of all
-- courses that start before 13:30.
-- +-----+
-- | 61A |
-- | 8   |
-- | 10  |
-- +-----+
SELECT course
    FROM courses
    WHERE h < 13 OR (h = 13 AND m < 30);


-- (b) (4 pt) Select a two-column table with one row per location that contains
-- the location, as well as the shortest length in minutes of any lecture held
-- in that location.
-- +----------+----+
-- | Dwinelle | 80 |
-- | VLSB     | 80 |
-- | Wheeler  | 45 |
-- +----------+----+
SELECT loc, min(len)
    FROM courses, locations
    WHERE name = course
    GROUP BY loc;


-- (c) (4 pt) Select a three-column table where each row describes an earlier
-- course, a later course, and the amount of time in minutes between the end
-- time of the earlier course and the start time of the later course.
-- Only include pairs of courses where the lectures do not overlap in time.
-- Note: There are 60 minutes in an hour.
-- +-----+------+----+
-- | 61A | 1    | 10 |
-- | 8   | 1    | 40 |
-- | 8   | 2    | 10 |
-- | 8   | 50AC | 10 |
-- +-----+------+----+
-- SELECT a.course, b.course, (b.h * 60 + b.m) - (a.h * 60 + a.m + a.len)
--     FROM courses AS a, courses AS b
--     WHERE a.h * 60 + a.m + a.len < b.h * 60 + b.m;
-- Official Solution
SELECT a.course, b.course, (b.h - a.h) * 60 + b.m - a.m - a.len AS gap
    FROM courses AS a, courses AS b
    WHERE gap > 0;