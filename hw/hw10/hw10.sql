CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  -- SELECT child
  --   FROM dogs AS a, parents, dogs AS b
  --   WHERE a.name = child AND parent = b.name
  --   ORDER BY b.height DESC;
  -- Official Solution
  SELECT child
    FROM parents, dogs
    WHERE name = parent
    ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
    FROM dogs, sizes
    WHERE height > min AND height <= max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  -- SELECT a.name AS dog_a, b.name AS dog_b, a.size
  --   FROM size_of_dogs AS a, parents as pa, size_of_dogs AS b, parents AS pb
  --   WHERE a.name = pa.child AND
  --     b.name = pb.child AND
  --     pa.parent = pb.parent AND
  --     a.name < b.name AND a.size = b.size;
  -- Official Solution
  SELECT a.child AS first, b.child AS second
    FROM parents AS a, parents AS b
    WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  -- SELECT "The two siblings, " || dog_a || " and " || dog_b || ", have the same size: " || size
  --   FROM siblings;
  -- Official Solution
  SELECT "The two siblings, " || first || " and " || second || ", have the same size: " || a.size
    FROM siblings, size_of_dogs AS a, size_of_dogs AS b
    WHERE a.size = b.size AND a.name = first AND b.name = second;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, MAX(height)  - MIN(height)
    FROM dogs
    GROUP BY fur
    HAVING MIN(height) >= AVG(height) * 0.7 AND MAX(height) <= AVG(height) * 1.3;

