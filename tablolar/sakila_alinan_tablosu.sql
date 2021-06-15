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
-- Table structure for table `alinan_tablosu`
--

DROP TABLE IF EXISTS `alinan_tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alinan_tablosu` (
  `alinan_emanet_no` int NOT NULL AUTO_INCREMENT,
  `alinan_alis_tarihi` date NOT NULL,
  `alinan_teslim_tarihi` date NOT NULL,
  `alinan_uye_id` int NOT NULL,
  `alinan_kitap_isbn` varchar(13) NOT NULL,
  `alinan_kutuphane_id` int NOT NULL,
  PRIMARY KEY (`alinan_emanet_no`),
  UNIQUE KEY `alinan_emanet_no_UNIQUE` (`alinan_emanet_no`) /*!80000 INVISIBLE */,
  KEY `fk_kutuphane_id_idx` (`alinan_kutuphane_id`),
  KEY `fk_kitap_isbn_idx` (`alinan_kitap_isbn`),
  KEY `fk_alinan_uye_id_idx` (`alinan_uye_id`),
  CONSTRAINT `alinan_tablosu_ibfk_1` FOREIGN KEY (`alinan_uye_id`) REFERENCES `uye_tablosu` (`uye_id`),
  CONSTRAINT `fk_alinan_kitap_isbn` FOREIGN KEY (`alinan_kitap_isbn`) REFERENCES `kitap_tablosu` (`kitap_isbn`),
  CONSTRAINT `fk_alinan_kutuphane_id` FOREIGN KEY (`alinan_kutuphane_id`) REFERENCES `kutuphane_tablosu` (`kutuphane_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alinan_tablosu`
--

LOCK TABLES `alinan_tablosu` WRITE;
/*!40000 ALTER TABLE `alinan_tablosu` DISABLE KEYS */;
INSERT INTO `alinan_tablosu` VALUES (17,'2021-06-13','2021-08-13',45,'145',2),(19,'2021-06-13','2021-08-13',12570,'145',2),(20,'2021-06-13','2021-08-13',12571,'145',2);
/*!40000 ALTER TABLE `alinan_tablosu` ENABLE KEYS */;
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
