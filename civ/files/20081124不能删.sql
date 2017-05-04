-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.29-rc-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema annals
--

CREATE DATABASE IF NOT EXISTS annals;
USE annals;

--
-- Definition of table `ally_ally`
--

DROP TABLE IF EXISTS `ally_ally`;
CREATE TABLE `ally_ally` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `member_amount` smallint(6) NOT NULL,
  `website` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ally_ally`
--

/*!40000 ALTER TABLE `ally_ally` DISABLE KEYS */;
INSERT INTO `ally_ally` (`id`,`name`,`member_amount`,`website`,`description`) VALUES 
 (1,'香格里拉【Shangri-La】',0,'','0'),
 (2,'天下一统',0,'','0');
/*!40000 ALTER TABLE `ally_ally` ENABLE KEYS */;


--
-- Definition of table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


--
-- Definition of table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


--
-- Definition of table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_message`
--

/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;


--
-- Definition of table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES 
 (1,'Can add permission',1,'add_permission'),
 (2,'Can change permission',1,'change_permission'),
 (3,'Can delete permission',1,'delete_permission'),
 (4,'Can add group',2,'add_group'),
 (5,'Can change group',2,'change_group'),
 (6,'Can delete group',2,'delete_group'),
 (7,'Can add user',3,'add_user'),
 (8,'Can change user',3,'change_user'),
 (9,'Can delete user',3,'delete_user'),
 (10,'Can add message',4,'add_message'),
 (11,'Can change message',4,'change_message'),
 (12,'Can delete message',4,'delete_message'),
 (13,'Can add content type',5,'add_contenttype'),
 (14,'Can change content type',5,'change_contenttype'),
 (15,'Can delete content type',5,'delete_contenttype'),
 (16,'Can add session',6,'add_session'),
 (17,'Can change session',6,'change_session'),
 (18,'Can delete session',6,'delete_session'),
 (19,'Can add site',7,'add_site'),
 (20,'Can change site',7,'change_site'),
 (21,'Can delete site',7,'delete_site'),
 (22,'Can add log entry',8,'add_logentry'),
 (23,'Can change log entry',8,'change_logentry'),
 (24,'Can delete log entry',8,'delete_logentry'),
 (25,'Can add 用户资料',9,'add_profile'),
 (26,'Can change 用户资料',9,'change_profile'),
 (27,'Can delete 用户资料',9,'delete_profile'),
 (28,'Can add 城市信息',10,'add_city'),
 (29,'Can change 城市信息',10,'change_city'),
 (30,'Can delete 城市信息',10,'delete_city'),
 (31,'Can add 建筑元素',11,'add_buildingelement'),
 (32,'Can change 建筑元素',11,'change_buildingelement'),
 (33,'Can delete 建筑元素',11,'delete_buildingelement'),
 (34,'Can add 建筑信息',12,'add_building'),
 (35,'Can change 建筑信息',12,'change_building'),
 (36,'Can delete 建筑信息',12,'delete_building'),
 (37,'Can add 坐标特征',13,'add_coordinate'),
 (38,'Can change 坐标特征',13,'change_coordinate'),
 (39,'Can delete 坐标特征',13,'delete_coordinate'),
 (40,'Can add 盟邦信息',14,'add_ally'),
 (41,'Can change 盟邦信息',14,'change_ally'),
 (42,'Can delete 盟邦信息',14,'delete_ally'),
 (43,'Can add 物件分类',15,'add_catalog'),
 (44,'Can change 物件分类',15,'change_catalog'),
 (45,'Can delete 物件分类',15,'delete_catalog'),
 (46,'Can add 物件信息',16,'add_ware'),
 (47,'Can change 物件信息',16,'change_ware'),
 (48,'Can delete 物件信息',16,'delete_ware');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


--
-- Definition of table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`,`username`,`first_name`,`last_name`,`email`,`password`,`is_staff`,`is_active`,`is_superuser`,`last_login`,`date_joined`) VALUES 
 (1,'ouds','','','ouds@gaing.com','sha1$a0ed7$d64dccef926c4f82d0a70dd7c0c2d8ab8a97e0b5',1,1,1,'2008-11-24 21:37:27','2008-11-23 18:35:11'),
 (8,'gm','Game','Manager','ourunix@gmail.com','sha1$cc977$df3145cd50129d365df240283ef16a5ad1037d41',0,0,0,'2008-11-24 21:38:27','2008-11-24 21:38:27');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


--
-- Definition of table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


--
-- Definition of table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user_user_permissions`
--

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


--
-- Definition of table `city_building`
--

DROP TABLE IF EXISTS `city_building`;
CREATE TABLE `city_building` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_id` int(11) NOT NULL,
  `building_element_id` int(11) NOT NULL,
  `level` smallint(6) NOT NULL,
  `location` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `city_building_city_id` (`city_id`),
  KEY `city_building_building_element_id` (`building_element_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `city_building`
--

/*!40000 ALTER TABLE `city_building` DISABLE KEYS */;
INSERT INTO `city_building` (`id`,`city_id`,`building_element_id`,`level`,`location`) VALUES 
 (1,3,1,1,2),
 (2,3,17,1,3);
/*!40000 ALTER TABLE `city_building` ENABLE KEYS */;


--
-- Definition of table `city_buildingelement`
--

DROP TABLE IF EXISTS `city_buildingelement`;
CREATE TABLE `city_buildingelement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `picture` varchar(50) NOT NULL,
  `water` int(11) NOT NULL,
  `food` int(11) NOT NULL,
  `wood` int(11) NOT NULL,
  `clay_stone` int(11) NOT NULL,
  `ore` int(11) NOT NULL,
  `money` int(11) NOT NULL,
  `people` int(11) NOT NULL,
  `time` smallint(6) NOT NULL,
  `civilization_point` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `picture` (`picture`)
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `city_buildingelement`
--

/*!40000 ALTER TABLE `city_buildingelement` DISABLE KEYS */;
INSERT INTO `city_buildingelement` (`id`,`name`,`picture`,`water`,`food`,`wood`,`clay_stone`,`ore`,`money`,`people`,`time`,`civilization_point`) VALUES 
 (1,'窑厂','jiaochang',1,1,1,1,1,1,1,0,3),
 (2,'酒坊','jiufang',1,1,1,1,1,1,1,0,3),
 (3,'木坊','mufang',1,1,1,1,1,1,1,0,3),
 (4,'石坊','shifang',1,1,1,1,1,1,1,0,3),
 (5,'城墙','chengqiang',1,1,1,1,1,1,1,0,1),
 (6,'城门','chengmen',1,1,1,1,1,1,1,0,1),
 (7,'瞭望塔','liaowangta',1,1,1,1,1,1,1,0,1),
 (8,'烽火台','fenghuotai',1,1,1,1,1,1,1,0,1),
 (9,'木场','muchang',1,1,1,1,1,1,1,0,2),
 (10,'土石场','tushichang',1,1,1,1,1,1,1,0,2),
 (11,'粮田','liangtian',1,1,1,1,1,1,1,0,2),
 (12,'矿场','kuangchang',1,1,1,1,1,1,1,0,2),
 (13,'水井','shuijing',1,1,1,1,1,11,1,90,2),
 (14,'仓库','canku',1,1,1,1,1,1,1,270,3),
 (15,'粮仓','liangcang',1,1,1,1,1,1,1,270,3),
 (16,'水司','shuisi',1,1,1,1,1,1,1,270,3),
 (17,'医馆','yiguan',1,1,1,1,1,1,1,720,8),
 (18,'营建司','yingjiansi',1,1,1,1,1,1,1,720,8),
 (19,'市舶司','shibosi',1,1,1,1,1,1,1,720,8),
 (20,'书院','shuyuan',1,1,1,1,1,1,1,630,7),
 (21,'膳房','shanfang',1,1,1,1,1,1,1,630,7),
 (22,'乐坊','yuefang',1,1,1,1,1,1,1,630,7),
 (23,'酒肆','jiusi',1,1,1,1,1,1,1,630,7),
 (24,'棋院','qiyuan',1,1,1,1,1,1,1,630,7),
 (25,'画坊','huafang',1,1,1,1,1,1,1,630,7),
 (26,'景苑','jingyuan',1,1,1,1,1,1,1,630,7),
 (27,'大剧院','dajuyuan',1,1,1,1,1,1,1,1,7),
 (28,'武馆','wuguan',1,1,1,1,1,1,1,540,6),
 (29,'魔法学校','mofaxuexiao',1,1,1,1,1,1,1,540,6),
 (30,'道观','daoguan',1,1,1,1,1,1,1,450,5),
 (31,'寺院','siyuan',1,1,1,1,1,1,1,450,5),
 (32,'基督教堂','jidujiaotang',1,1,1,1,1,1,1,450,5),
 (33,'清真寺','qingzhensi',1,1,1,1,1,1,1,450,5),
 (34,'兵营','bingying',1,1,1,1,1,1,1,360,4),
 (35,'铁铺','tiepu',1,1,1,1,1,1,1,360,4),
 (36,'马场','machang',1,1,1,1,1,1,1,360,4),
 (37,'器械厂','qixiechang',1,1,1,1,1,1,1,360,4),
 (38,'船坞','chuanwu',1,1,1,1,1,1,1,360,4),
 (39,'皇宫','huanggong',1,1,1,1,1,1,1,810,9),
 (40,'府衙','fuya',1,1,1,1,1,1,1,810,9),
 (41,'鸿胪寺','honglusi',1,1,1,1,1,1,1,810,9);
/*!40000 ALTER TABLE `city_buildingelement` ENABLE KEYS */;


--
-- Definition of table `city_city`
--

DROP TABLE IF EXISTS `city_city`;
CREATE TABLE `city_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) DEFAULT NULL,
  `coordinate_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `is_capital` tinyint(1) NOT NULL,
  `style` varchar(2) NOT NULL,
  `water_speed` int(11) NOT NULL,
  `water_stock` int(11) NOT NULL,
  `water_storage` int(11) NOT NULL,
  `food_speed` int(11) NOT NULL,
  `food_stock` int(11) NOT NULL,
  `food_storage` int(11) NOT NULL,
  `wood_speed` int(11) NOT NULL,
  `wood_stock` int(11) NOT NULL,
  `clay_stone_speed` int(11) NOT NULL,
  `clay_stone_stock` int(11) NOT NULL,
  `ore_speed` int(11) NOT NULL,
  `ore_stock` int(11) NOT NULL,
  `goods_storage` int(11) NOT NULL,
  `horse_speed` int(11) NOT NULL,
  `horse_stock` int(11) NOT NULL,
  `horse_storage` int(11) NOT NULL,
  `money_speed` int(11) NOT NULL,
  `money_stock` int(11) NOT NULL,
  `money_storage` int(11) NOT NULL,
  `people_speed` int(11) NOT NULL,
  `people_stock` int(11) NOT NULL,
  `people_storage` int(11) NOT NULL,
  `civilization_value` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `coordinate_id` (`coordinate_id`),
  UNIQUE KEY `name` (`name`),
  KEY `city_city_profile_id` (`profile_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `city_city`
--

/*!40000 ALTER TABLE `city_city` DISABLE KEYS */;
INSERT INTO `city_city` (`id`,`profile_id`,`coordinate_id`,`name`,`is_capital`,`style`,`water_speed`,`water_stock`,`water_storage`,`food_speed`,`food_stock`,`food_storage`,`wood_speed`,`wood_stock`,`clay_stone_speed`,`clay_stone_stock`,`ore_speed`,`ore_stock`,`goods_storage`,`horse_speed`,`horse_stock`,`horse_storage`,`money_speed`,`money_stock`,`money_storage`,`people_speed`,`people_stock`,`people_storage`,`civilization_value`) VALUES 
 (3,7,3,'gm都城',1,'hx',9,1068,1092,9,1068,1092,9,1068,9,1068,9,1068,1092,0,0,0,9,1068,1092,9,108,108,108);
/*!40000 ALTER TABLE `city_city` ENABLE KEYS */;


--
-- Definition of table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`,`action_time`,`user_id`,`content_type_id`,`object_id`,`object_repr`,`action_flag`,`change_message`) VALUES 
 (1,'2008-11-23 18:43:40',1,15,'1','瓷器 窑厂 jiaochang 3 90',1,''),
 (2,'2008-11-23 18:44:38',1,15,'2','酒 酒坊 jiufang 3 90',1,''),
 (3,'2008-11-23 18:45:04',1,15,'3','木器 木坊 mufang 3 90',1,''),
 (4,'2008-11-23 18:45:25',1,15,'4','石顺 石坊 shifang 3 90',1,''),
 (5,'2008-11-23 18:46:04',1,15,'5','战马 马场 machang 4 90',1,''),
 (6,'2008-11-23 18:46:28',1,15,'6','战狗 兵营 bingying 4 90',1,''),
 (7,'2008-11-23 18:47:37',1,16,'1','战马 战马 马场 machang 4 90 1',1,''),
 (8,'2008-11-23 18:47:47',1,16,'2','战狗 战狗 兵营 bingying 4 90 1',1,''),
 (9,'2008-11-23 18:48:00',1,16,'3','青瓷 瓷器 窑厂 jiaochang 3 90 1',1,''),
 (10,'2008-11-23 18:48:20',1,16,'4','赤瓷 瓷器 窑厂 jiaochang 3 90 2',1,''),
 (11,'2008-11-23 18:48:33',1,16,'5','金瓷 瓷器 窑厂 jiaochang 3 90 3',1,''),
 (12,'2008-11-23 18:48:50',1,16,'6','雪瓷 瓷器 窑厂 jiaochang 3 90 4',1,''),
 (13,'2008-11-23 18:49:16',1,16,'7','幽瓷 瓷器 窑厂 jiaochang 3 90 5',1,''),
 (14,'2008-11-23 18:49:28',1,16,'8','竹叶青 酒 酒坊 jiufang 3 90 1',1,''),
 (15,'2008-11-23 18:49:41',1,16,'9','女儿红 酒 酒坊 jiufang 3 90 2',1,''),
 (16,'2008-11-23 18:49:51',1,16,'10','黄酒 酒 酒坊 jiufang 3 90 3',1,''),
 (17,'2008-11-23 18:50:18',1,16,'11','五粮液 酒 酒坊 jiufang 3 90 4',1,''),
 (18,'2008-11-23 18:50:42',1,16,'10','黄桂稠酒 酒 酒坊 jiufang 3 90 3',2,'已修改 name 。'),
 (19,'2008-11-23 18:51:34',1,16,'12','茅台 酒 酒坊 jiufang 3 90 5',1,''),
 (20,'2008-11-23 18:51:58',1,16,'13','青木家俱 木器 木坊 mufang 3 90 1',1,''),
 (21,'2008-11-23 18:52:14',1,16,'14','红木家俱 木器 木坊 mufang 3 90 2',1,''),
 (22,'2008-11-23 18:52:31',1,16,'15','金色木器 木器 木坊 mufang 3 90 3',1,''),
 (23,'2008-11-23 18:52:58',1,16,'16','莹雪木器 木器 木坊 mufang 3 90 4',1,''),
 (24,'2008-11-23 18:53:21',1,16,'17','焦尾家俱 木器 木坊 mufang 3 90 5',1,''),
 (25,'2008-11-23 18:53:46',1,16,'18','青玉 石顺 石坊 shifang 3 90 1',1,''),
 (26,'2008-11-23 18:53:59',1,16,'19','红宝石 石顺 石坊 shifang 3 90 2',1,''),
 (27,'2008-11-23 18:54:13',1,16,'20','金玉 石顺 石坊 shifang 3 90 3',1,''),
 (28,'2008-11-23 18:54:33',1,16,'21','钻石 石顺 石坊 shifang 3 90 4',1,''),
 (29,'2008-11-23 18:55:00',1,16,'22','黑玉 石顺 石坊 shifang 3 90 5',1,''),
 (30,'2008-11-23 18:57:14',1,15,'7','马车 市舶司 shibosi 8 450',1,''),
 (31,'2008-11-23 18:57:30',1,16,'23','马车 马车 市舶司 shibosi 8 450 1',1,''),
 (32,'2008-11-23 18:59:45',1,15,'8','马蹄铁 铁铺 tiepu 4 90',1,''),
 (33,'2008-11-23 19:00:51',1,15,'9','盾牌铁片 铁铺 tiepu 4 450',1,''),
 (34,'2008-11-23 19:02:20',1,15,'10','盔甲铁 铁铺 tiepu 4 900',1,''),
 (35,'2008-11-23 19:02:40',1,15,'9','铁片 铁铺 tiepu 4 450',2,'已修改 name 。'),
 (36,'2008-11-23 19:04:04',1,15,'10','箭簇 铁铺 tiepu 4 900',2,'已修改 name 。'),
 (37,'2008-11-23 19:11:00',1,15,'11','枪头 铁铺 tiepu 4 900',1,''),
 (38,'2008-11-23 19:11:33',1,15,'12','刀身 铁铺 tiepu 4 900',1,''),
 (39,'2008-11-23 19:19:22',1,15,'13','火器管 铁铺 tiepu 4 900',1,''),
 (40,'2008-11-23 19:20:15',1,15,'14','盾牌 器械厂 qixiechang 4 900',1,''),
 (41,'2008-11-23 19:20:48',1,15,'15','盔甲 器械厂 qixiechang 4 900',1,''),
 (42,'2008-11-23 19:21:14',1,15,'16','朴刀 器械厂 qixiechang 4 900',1,''),
 (43,'2008-11-23 19:21:48',1,15,'17','长枪 器械厂 qixiechang 4 900',1,''),
 (44,'2008-11-23 19:22:20',1,15,'18','陌刀 器械厂 qixiechang 4 900',1,''),
 (45,'2008-11-23 19:22:54',1,15,'19','弓箭 器械厂 qixiechang 4 900',1,''),
 (46,'2008-11-23 19:23:17',1,15,'20','诸葛连驽 器械厂 qixiechang 4 900',1,''),
 (47,'2008-11-23 19:23:42',1,15,'21','火枪 器械厂 qixiechang 4 900',1,''),
 (48,'2008-11-23 19:24:03',1,15,'22','火铳 器械厂 qixiechang 4 900',1,''),
 (49,'2008-11-23 19:24:24',1,15,'23','云梯 器械厂 qixiechang 4 900',1,''),
 (50,'2008-11-23 19:24:44',1,15,'24','冲车 器械厂 qixiechang 4 900',1,''),
 (51,'2008-11-23 19:25:25',1,15,'25','投石机 器械厂 qixiechang 4 900',1,''),
 (52,'2008-11-23 19:25:43',1,15,'26','箭楼 器械厂 qixiechang 4 900',1,''),
 (53,'2008-11-23 19:25:57',1,15,'27','火炮 器械厂 qixiechang 4 900',1,''),
 (54,'2008-11-23 19:26:48',1,15,'7','马车 器械厂 qixiechang 4 450',2,'已修改 building_element 。'),
 (55,'2008-11-23 19:32:34',1,15,'7','器械 器械厂 qixiechang 4 450',2,'已修改 name 。'),
 (56,'2008-11-23 19:33:04',1,15,'8','生铁 铁铺 tiepu 4 90',2,'已修改 name 。'),
 (57,'2008-11-23 19:33:40',1,15,'9','舰船 船坞 chuanwu 4 450',2,'已修改 name 和 building_element 。'),
 (58,'2008-11-23 19:41:36',1,16,'24','盾牌 器械 器械厂 qixiechang 4 450 1',1,''),
 (59,'2008-11-23 19:41:48',1,16,'25','盔甲 器械 器械厂 qixiechang 4 450 1',1,''),
 (60,'2008-11-23 19:42:01',1,16,'26','朴刀 器械 器械厂 qixiechang 4 450 1',1,''),
 (61,'2008-11-23 19:42:17',1,16,'27','长枪 器械 器械厂 qixiechang 4 450 1',1,''),
 (62,'2008-11-23 19:42:45',1,16,'28','陌刀 器械 器械厂 qixiechang 4 450 1',1,''),
 (63,'2008-11-23 19:42:58',1,16,'29','弓箭 器械 器械厂 qixiechang 4 450 1',1,''),
 (64,'2008-11-23 19:43:09',1,16,'30','诸葛连驽 器械 器械厂 qixiechang 4 450 1',1,''),
 (65,'2008-11-23 19:43:22',1,16,'31','火枪 器械 器械厂 qixiechang 4 450 5',1,''),
 (66,'2008-11-23 19:43:33',1,16,'32','火铳 器械 器械厂 qixiechang 4 450 11',1,''),
 (67,'2008-11-23 19:43:45',1,16,'33','云梯 器械 器械厂 qixiechang 4 450 1',1,''),
 (68,'2008-11-23 19:43:59',1,16,'34','冲车 器械 器械厂 qixiechang 4 450 5',1,''),
 (69,'2008-11-23 19:44:13',1,16,'35','箭楼 器械 器械厂 qixiechang 4 450 2',1,''),
 (70,'2008-11-23 19:44:26',1,16,'36','投石机 器械 器械厂 qixiechang 4 450 5',1,''),
 (71,'2008-11-23 19:44:41',1,16,'37','火炮 器械 器械厂 qixiechang 4 450 12',1,''),
 (72,'2008-11-23 19:45:28',1,16,'38','马蹄铁 生铁 铁铺 tiepu 4 90 1',1,''),
 (73,'2008-11-23 19:45:40',1,16,'39','铁片 生铁 铁铺 tiepu 4 90 2',1,''),
 (74,'2008-11-23 19:45:52',1,16,'40','箭簇 生铁 铁铺 tiepu 4 90 3',1,''),
 (75,'2008-11-23 19:46:05',1,16,'41','枪头 生铁 铁铺 tiepu 4 90 4',1,''),
 (76,'2008-11-23 19:46:19',1,16,'42','刀身 生铁 铁铺 tiepu 4 90 5',1,''),
 (77,'2008-11-23 19:46:29',1,16,'43','火器管 生铁 铁铺 tiepu 4 90 6',1,''),
 (78,'2008-11-23 19:47:25',1,16,'44','楼船战舰 舰船 船坞 chuanwu 4 450 12',1,''),
 (79,'2008-11-23 19:47:40',1,16,'45','蒙冲斗舰 舰船 船坞 chuanwu 4 450 9',1,''),
 (80,'2008-11-23 19:47:58',1,16,'46','游击赤马舟 舰船 船坞 chuanwu 4 450 5',1,''),
 (81,'2008-11-23 19:48:13',1,16,'47','粮船 舰船 船坞 chuanwu 4 450 5',1,''),
 (82,'2008-11-23 20:37:31',1,3,'None','gm',3,''),
 (83,'2008-11-23 20:38:28',1,3,'None','gm',3,''),
 (84,'2008-11-23 20:42:49',1,3,'None','gm',3,''),
 (85,'2008-11-23 20:43:52',1,3,'None','gm',3,''),
 (86,'2008-11-24 12:02:24',1,15,'6','战斗力 兵营 bingying 4 90',2,'已修改 name 。'),
 (87,'2008-11-24 21:39:01',1,12,'1','gm cn 文 None  -1 -1 湿地 gm都城 108 窑厂 jiaochang 3 1',1,''),
 (88,'2008-11-24 21:40:58',1,12,'2','gm cn 文 None  -1 -1 湿地 gm都城 108 医馆 yiguan 8 1',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


--
-- Definition of table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES 
 (1,'permission','auth','permission'),
 (2,'group','auth','group'),
 (3,'user','auth','user'),
 (4,'message','auth','message'),
 (5,'content type','contenttypes','contenttype'),
 (6,'session','sessions','session'),
 (7,'site','sites','site'),
 (8,'log entry','admin','logentry'),
 (9,'用户资料','member','profile'),
 (10,'城市信息','city','city'),
 (11,'建筑元素','city','buildingelement'),
 (12,'建筑信息','city','building'),
 (13,'坐标特征','map','coordinate'),
 (14,'盟邦信息','ally','ally'),
 (15,'物件分类','ware','catalog'),
 (16,'物件信息','ware','ware');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


--
-- Definition of table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`,`session_data`,`expire_date`) VALUES 
 ('117be51d817f70075fe18a784e8d8c3f','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-23 19:08:43'),
 ('2c4173b77565b247ad4ebd795270c716','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-23 19:40:38'),
 ('1db67827d3455a7cac469f5a2fef0896','gAJ9cQEoVQ1fYXV0aF91c2VyX2lkcQKKAQFVEl9hdXRoX3VzZXJfYmFja2VuZHEDVSlkamFuZ28u\nY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEEVQ9kamFuZ29fbGFuZ3VhZ2VxBVgC\nAAAAZW5xBnUuZTIzNWQzZTM2MWMxMGNlMGViZmU5NjdhMjFlZTMyMWQ=\n','2008-11-23 20:31:20'),
 ('ddae4cffedc9d9f3be8ed88e770e9620','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UPZGphbmdvX2xhbmd1YWdlcQRVBXpoLWNucQVVDV9hdXRoX3VzZXJf\naWRxBooBAXUuNTg2MzQ3OTBkMGMzZjI4MWFmNDE2ODg0OWE5OTc5MjU=\n','2008-11-23 21:09:45'),
 ('8e603d985159ced491924054e42f2545','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-24 11:13:18'),
 ('20be12d96c7f228b4eb19b511b26d43b','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-24 11:49:01'),
 ('576daafd83dbbeb9149ddd52dbf3882e','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-24 12:32:03'),
 ('eb5d488640dca450dbfcb9a7fc6df263','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UPZGphbmdvX2xhbmd1YWdlcQRVBXpoLWNucQVVDV9hdXRoX3VzZXJf\naWRxBooBAXUuNTg2MzQ3OTBkMGMzZjI4MWFmNDE2ODg0OWE5OTc5MjU=\n','2008-11-24 21:32:33'),
 ('e33b241e2730badd925a0075b1076f77','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS44MzRiYzNiZGEwMTgzYWRiMzY4\nMTA0YTU2YjdlMjdjZQ==\n','2008-11-24 22:07:27');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


--
-- Definition of table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_site`
--

/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` (`id`,`domain`,`name`) VALUES 
 (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;


--
-- Definition of table `map_coordinate`
--

DROP TABLE IF EXISTS `map_coordinate`;
CREATE TABLE `map_coordinate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `longitude` int(11) NOT NULL,
  `latitude` int(11) NOT NULL,
  `property` smallint(6) NOT NULL,
  `water_parameter` decimal(3,2) NOT NULL,
  `food_parameter` decimal(3,2) NOT NULL,
  `wood_parameter` decimal(3,2) NOT NULL,
  `clay_stone_parameter` decimal(3,2) NOT NULL,
  `ore_parameter` decimal(3,2) NOT NULL,
  `people_parameter` decimal(3,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `longitude` (`longitude`,`latitude`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `map_coordinate`
--

/*!40000 ALTER TABLE `map_coordinate` DISABLE KEYS */;
INSERT INTO `map_coordinate` (`id`,`longitude`,`latitude`,`property`,`water_parameter`,`food_parameter`,`wood_parameter`,`clay_stone_parameter`,`ore_parameter`,`people_parameter`) VALUES 
 (1,0,0,8,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (2,1,1,5,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (3,-1,-1,5,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (4,0,1,7,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (5,0,-1,4,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (6,1,0,8,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (7,-1,0,8,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (8,-1,1,8,'1.00','1.00','1.00','1.00','1.00','1.00'),
 (9,1,-1,8,'1.00','1.00','1.00','1.00','1.00','1.00');
/*!40000 ALTER TABLE `map_coordinate` ENABLE KEYS */;


--
-- Definition of table `member_profile`
--

DROP TABLE IF EXISTS `member_profile`;
CREATE TABLE `member_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `is_vip` tinyint(1) NOT NULL,
  `activation_key` varchar(50) NOT NULL,
  `is_email_public` tinyint(1) NOT NULL,
  `sex` varchar(7) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `birth_day` varchar(10) NOT NULL,
  `area` varchar(2) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `occupation` varchar(50) NOT NULL,
  `website` varchar(200) NOT NULL,
  `type` smallint(6) NOT NULL,
  `ally_id` int(11) DEFAULT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `member_profile_ally_id` (`ally_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `member_profile`
--

/*!40000 ALTER TABLE `member_profile` DISABLE KEYS */;
INSERT INTO `member_profile` (`id`,`user_id`,`is_vip`,`activation_key`,`is_email_public`,`sex`,`photo`,`birth_day`,`area`,`phone`,`occupation`,`website`,`type`,`ally_id`,`description`) VALUES 
 (7,8,0,'43bb082bddc816b0ac3a0cdb33b22aca52cba8c7',1,'unknown','','','cn','','','',0,NULL,'aaaaa');
/*!40000 ALTER TABLE `member_profile` ENABLE KEYS */;


--
-- Definition of table `ware_catalog`
--

DROP TABLE IF EXISTS `ware_catalog`;
CREATE TABLE `ware_catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `building_element_id` int(11) NOT NULL,
  `water` int(11) NOT NULL,
  `food` int(11) NOT NULL,
  `wood` int(11) NOT NULL,
  `clay_stone` int(11) NOT NULL,
  `ore` int(11) NOT NULL,
  `money` int(11) NOT NULL,
  `time` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ware_catalog_building_element_id` (`building_element_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ware_catalog`
--

/*!40000 ALTER TABLE `ware_catalog` DISABLE KEYS */;
INSERT INTO `ware_catalog` (`id`,`name`,`building_element_id`,`water`,`food`,`wood`,`clay_stone`,`ore`,`money`,`time`) VALUES 
 (1,'瓷器',1,1,1,1,1,1,1,90),
 (2,'酒',2,1,1,1,1,1,1,90),
 (3,'木器',3,1,1,1,1,1,1,90),
 (4,'石顺',4,1,1,1,1,1,1,90),
 (5,'战马',36,1,1,1,1,1,1,90),
 (6,'战斗力',34,1,1,1,1,1,1,90),
 (7,'器械',37,1,1,1,1,1,1,450),
 (8,'生铁',35,1,1,1,1,1,1,90),
 (9,'舰船',38,1,1,1,1,1,1,450);
/*!40000 ALTER TABLE `ware_catalog` ENABLE KEYS */;


--
-- Definition of table `ware_ware`
--

DROP TABLE IF EXISTS `ware_ware`;
CREATE TABLE `ware_ware` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `catalog_id` int(11) NOT NULL,
  `level` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ware_ware_catalog_id` (`catalog_id`)
) ENGINE=MyISAM AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ware_ware`
--

/*!40000 ALTER TABLE `ware_ware` DISABLE KEYS */;
INSERT INTO `ware_ware` (`id`,`name`,`catalog_id`,`level`) VALUES 
 (1,'战马',5,1),
 (2,'战狗',6,1),
 (3,'青瓷',1,1),
 (4,'赤瓷',1,2),
 (5,'金瓷',1,3),
 (6,'雪瓷',1,4),
 (7,'幽瓷',1,5),
 (8,'竹叶青',2,1),
 (9,'女儿红',2,2),
 (10,'黄桂稠酒',2,3),
 (11,'五粮液',2,4),
 (12,'茅台',2,5),
 (13,'青木家俱',3,1),
 (14,'红木家俱',3,2),
 (15,'金色木器',3,3),
 (16,'莹雪木器',3,4),
 (17,'焦尾家俱',3,5),
 (18,'青玉',4,1),
 (19,'红宝石',4,2),
 (20,'金玉',4,3),
 (21,'钻石',4,4),
 (22,'黑玉',4,5),
 (23,'马车',7,1),
 (24,'盾牌',7,1),
 (25,'盔甲',7,1),
 (26,'朴刀',7,1),
 (27,'长枪',7,1),
 (28,'陌刀',7,1),
 (29,'弓箭',7,1),
 (30,'诸葛连驽',7,1),
 (31,'火枪',7,5),
 (32,'火铳',7,11),
 (33,'云梯',7,1),
 (34,'冲车',7,5),
 (35,'箭楼',7,2),
 (36,'投石机',7,5),
 (37,'火炮',7,12),
 (38,'马蹄铁',8,1),
 (39,'铁片',8,2),
 (40,'箭簇',8,3),
 (41,'枪头',8,4),
 (42,'刀身',8,5),
 (43,'火器管',8,6),
 (44,'楼船战舰',9,12),
 (45,'蒙冲斗舰',9,9),
 (46,'游击赤马舟',9,5),
 (47,'粮船',9,5);
/*!40000 ALTER TABLE `ware_ware` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
