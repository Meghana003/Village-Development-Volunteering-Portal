/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.0.67-community-nt : Database - volunteer_portal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`volunteer_portal` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `volunteer_portal`;

/*Table structure for table `apply_event` */

DROP TABLE IF EXISTS `apply_event`;

CREATE TABLE `apply_event` (
  `id` int(11) NOT NULL auto_increment,
  `eid` varchar(1000) default NULL,
  `location` varchar(100) default NULL,
  `date` varchar(100) default NULL,
  `event` varchar(100) default NULL,
  `uid` varchar(100) default NULL,
  `username` varchar(100) default NULL,
  `status` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `apply_event` */

insert  into `apply_event`(`id`,`eid`,`location`,`date`,`event`,`uid`,`username`,`status`) values (5,'4','Dilsukhnagar','2023-02-09','Blood Camp','1','gkv','Confirmed'),(6,'4','Dilsukhnagar','2023-02-09','Blood Camp','2','kishan','Confirmed');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `id` int(11) NOT NULL auto_increment,
  `location` varchar(100) default NULL,
  `date_of_event` varchar(100) default NULL,
  `event` varchar(100) default NULL,
  `description` longtext,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`id`,`location`,`date_of_event`,`event`,`description`) values (3,'Dilsukhnagar','2023-02-05','Medical','In this area many peoples are suffering with health issues\r\nso we are requesting volunteers to come forward to conduct \r\na medical camp in this are'),(4,'Dilsukhnagar','2023-02-09','Blood Camp','we are going to conduct blood camp at dilsukhnagar');

/*Table structure for table `volunteer` */

DROP TABLE IF EXISTS `volunteer`;

CREATE TABLE `volunteer` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(1000) default NULL,
  `email` varchar(100) default NULL,
  `mobile` varchar(100) default NULL,
  `address` varchar(100) default NULL,
  `username` varchar(100) default NULL,
  `password` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `volunteer` */

insert  into `volunteer`(`id`,`name`,`email`,`mobile`,`address`,`username`,`password`) values (1,'GKVTechSolutions','GkvTechSolutions@gmail.com','9640257292','hyderabad','gkv','123'),(2,'kishan','kishan@gmail.com','9640257292','hyderabad','kishan','123'),(3,'venkat','venkat@gmail.com','9640340708','hyderabad','venkat','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
