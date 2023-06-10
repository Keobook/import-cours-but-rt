CREATE TABLE `Mon-Banzaii`.`authentification` (
  `id` VARCHAR(255) NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(50) NOT NULL,
  `user_email` VARCHAR(30) NOT NULL
  `user_pwd` VARCHAR(40) NOT NULL,
  `user_salt` VARCHAR(100) NOT NULL,
  `oauth2` TEXT,
  `creation-time` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
