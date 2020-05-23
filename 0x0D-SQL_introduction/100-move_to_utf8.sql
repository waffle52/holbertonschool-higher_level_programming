-- a script that converts:
-- hbtn_0c_0 database to UTF8
-- first_table table in hbtn_0c_0 to UTF8
-- name column from firt_table to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
