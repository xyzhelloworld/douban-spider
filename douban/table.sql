#CREATE DATABASE douban DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `bookinfo` (
  `isbn` char(32) NOT NULL COMMENT 'ISBN',
  `title` varchar(100) COMMENT '书名',
  `author` varchar(10) COMMENT '作者',
  `press` varchar(20) COMMENT '出版社',
  `pages` int  COMMENT '页面数',
  `price` double COMMENT '价格',
  `press_date` datetime DEFAULT NULL  COMMENT '出版时间',
  PRIMARY KEY (`isbn`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

select * from bookinfo；