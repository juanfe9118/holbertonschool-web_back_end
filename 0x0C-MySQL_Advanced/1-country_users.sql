
-- Task 1: 1. In and not out - creates a table users
-- script can be executed on any database and if it is already created it doesn't fail
CREATE TABLE IF NOT EXISTS `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL 
)