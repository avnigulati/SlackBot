DROP DATABASE if exists `slackbot`;

CREATE DATABASE `slackbot`;

DROP TABLE IF EXISTS `slackbot`.`currentuser` ;

CREATE TABLE `slackbot`.`currentuser` ( 
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    `username` VARCHAR(20),
    PRIMARY KEY (`id`)
);

INSERT INTO `slackbot`.`currentuser`
(`id`,
`username`)
VALUES
(01,'None');
