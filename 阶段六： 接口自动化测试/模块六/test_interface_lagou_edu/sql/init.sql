-- MySQL dump 10.13  Distrib 8.0.28, for macos12.0 (x86_64)
--
-- Host: 150.158.25.85    Database: ssm_lagou_edu
-- ------------------------------------------------------
-- Server version	5.7.10-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `course_name` varchar(255) DEFAULT NULL COMMENT '课程名',
  `brief` varchar(255) DEFAULT '' COMMENT '课程一句话简介',
  `price` double(10,2) DEFAULT NULL COMMENT '原价',
  `price_tag` varchar(255) DEFAULT '' COMMENT '原价标签',
  `discounts` double(10,2) DEFAULT NULL COMMENT '优惠价',
  `discounts_tag` varchar(255) DEFAULT NULL COMMENT '优惠标签',
  `course_description_mark_down` longtext COMMENT '描述markdown',
  `course_description` longtext COMMENT '课程描述',
  `course_img_url` varchar(255) DEFAULT NULL COMMENT '课程分享图片url',
  `is_new` tinyint(1) DEFAULT NULL COMMENT '是否新品',
  `is_new_des` varchar(255) DEFAULT NULL COMMENT '广告语',
  `last_operator_id` int(11) DEFAULT NULL COMMENT '最后操作者',
  `auto_online_time` datetime DEFAULT NULL COMMENT '自动上架时间',
  `create_time` datetime NOT NULL COMMENT '记录创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `is_del` tinyint(1) DEFAULT '0' COMMENT '是否删除',
  `total_duration` int(11) DEFAULT NULL COMMENT '总时长(分钟)',
  `course_list_img` varchar(255) DEFAULT NULL COMMENT '课程列表展示图片',
  `status` int(2) DEFAULT '0' COMMENT '课程状态，0-草稿，1-上架',
  `sort_num` int(11) DEFAULT NULL COMMENT '课程排序，用于后台保存草稿时用到',
  `preview_first_field` varchar(255) DEFAULT NULL COMMENT '课程预览第一个字段',
  `preview_second_field` varchar(255) DEFAULT NULL COMMENT '课程预览第二个字段',
  `sales` int(11) DEFAULT '0' COMMENT '销量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;
