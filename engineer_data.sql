CREATE TABLE Machine(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        x1 INTEGER NOT NULL,
        x2 INTEGER NOT NULL,
        x3 INTEGER NOT NULL,
        x4 INTEGER NOT NULL,
        x5 INTEGER NOT NULL,
        br_chance INTEGER );

INSERT INTO Machine (
    id,
    x1,
    x2,
    x3,
    x4,
    x5,
    br_chance)
values
(
    1, 23,34,45,56,78, null
);

INSERT INTO Machine (
    id,
    x1,
    x2,
    x3,
    x4,
    x5,
    br_chance)
values
(
    2, 23,34,45,56,78, 0.3
);

INSERT INTO Machine (
    id,
    x1,
    x2,
    x3,
    x4,
    x5,
    br_chance)
values
(
    3, 23,47,45,56,78, null
);