CREATE SCHEMA `cardexdb` ;

CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(55) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(55) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `cardexdb`.`client` (`id`, `name`, `age`, `email`) 
VALUES ('0', 'bal', '23', 'bal@bal.com');
