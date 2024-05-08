CREATE SCHEMA `wazdan_project` ;


CREATE TABLE `games` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `js_file` varchar(45) NOT NULL,
  `token` varchar(45) NOT NULL,
  `licence` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

ALTER TABLE `games`
ADD `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
ADD `updated_at` timestamp NULL ON UPDATE CURRENT_TIMESTAMP AFTER `created_at`;


INSERT INTO `wazdan_project`.`games` (`name`, `js_file`, `token`, `licence`) VALUES ('gra1', 'game1.js', 'x', 'x');
INSERT INTO `wazdan_project`.`games` (`name`, `js_file`, `token`, `licence`) VALUES ('gra2', 'game2.js', 'y', 'y');
