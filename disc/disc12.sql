-- Q4: A Secret Message
-- A substitution cipher replaces each word with another word in a table in
-- order to encrypt a message. To decode an encrypted message, replace each
-- word x with its corresponding y in a code table.

-- Write a select statement to decode the original message
-- It's The End using the code table.
CREATE TABLE original AS
    SELECT 1 AS n, "It's" AS word UNION
    SELECT 2,      "The"          UNION
    SELECT 3,      "End";

CREATE TABLE code AS
    SELECT "Up" AS x, "Down" AS y UNION
    SELECT "Now",     "Home"      UNION
    SELECT "It's",    "What"      UNION
    SELECT "See",     "Do"        UNION
    SELECT "Can",     "See"       UNION
    SELECT "End",     "Now"       UNION
    SELECT "What",    "You"       UNION
    SELECT "The",     "Happens"   UNION
    SELECT "Love",    "Scheme"    UNION
    SELECT "Not",     "Mess"      UNION
    SELECT "Happens", "Go";

-- Join the original and code tables and make sure that the joined roles have
-- the same word and x.
SELECT y
    FROM original, code
    WHERE word = x
    ORDER by n;


-- What happens now? Write another select statement to decode this encrypted
-- message using the same code table.
CREATE TABLE original AS
    SELECT 1 AS n, "It's" AS word UNION
    SELECT 2,      "The"          UNION
    SELECT 3,      "End";

CREATE TABLE code AS
    SELECT "Up" AS x, "Down" AS y UNION
    SELECT "Now",     "Home"      UNION
    SELECT "It's",    "What"      UNION
    SELECT "See",     "Do"        UNION
    SELECT "Can",     "See"       UNION
    SELECT "End",     "Now"       UNION
    SELECT "What",    "You"       UNION
    SELECT "The",     "Happens"   UNION
    SELECT "Love",    "Scheme"    UNION
    SELECT "Not",     "Mess"      UNION
    SELECT "Happens", "Go";

-- Join original with code AS a and code AS b to create six-column rows
-- like: 2|The|The|Happens|Happens|Go,
-- The Go at the end is part of the decoded message.
SELECT b.y
    FROM original, code AS a, code AS b
    WHERE word = a.x AND a.y = b.x
    ORDER by n;

