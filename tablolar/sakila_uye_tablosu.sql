-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sakila
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `uye_tablosu`
--

DROP TABLE IF EXISTS `uye_tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uye_tablosu` (
  `uye_id` int NOT NULL AUTO_INCREMENT,
  `uye_adi` varchar(45) NOT NULL,
  `uye_soyadi` varchar(45) NOT NULL,
  `uye_tel` varchar(11) NOT NULL,
  `uye_mail` varchar(45) NOT NULL,
  `uye_adres_no` varchar(45) NOT NULL,
  PRIMARY KEY (`uye_id`),
  UNIQUE KEY `uye_mail_UNIQUE` (`uye_mail`),
  UNIQUE KEY `uye_tel_UNIQUE` (`uye_tel`)
) ENGINE=InnoDB AUTO_INCREMENT=12572 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uye_tablosu`
--

LOCK TABLES `uye_tablosu` WRITE;
/*!40000 ALTER TABLE `uye_tablosu` DISABLE KEYS */;
INSERT INTO `uye_tablosu` VALUES (1,'grkm','brbr','548','grkmbr','15'),(45,'gorkem','berberoglu','543','berber','15'),(78,'gor','ber','569','grkm','15'),(89,'grkm','brbr','258','berberoglu10','15'),(596,'br','kko','256','gbt','15'),(12569,'grkm123','brbr123','543408','gorkemberberoglu@gmail.com','15'),(12570,'gorkem','berberoglu','05434086892','gorkemberberoglu10@gmail.com','adres1'),(12571,'furkan','çelik','05555555555','furkan@gmail.com','adres2');
/*!40000 ALTER TABLE `uye_tablosu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-15 13:27:56
