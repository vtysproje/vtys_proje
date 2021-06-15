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
-- Table structure for table `kitap_tablosu`
--

DROP TABLE IF EXISTS `kitap_tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kitap_tablosu` (
  `kitap_isbn` varchar(13) NOT NULL,
  `kitap_baslik` varchar(45) NOT NULL,
  `kitap_yayinevi` varchar(100) NOT NULL,
  `kitap_kutuphane_id` int NOT NULL,
  PRIMARY KEY (`kitap_isbn`),
  UNIQUE KEY `kitap_isbn_UNIQUE` (`kitap_isbn`),
  KEY `fk_kitap_kutuphane_id_idx` (`kitap_kutuphane_id`),
  CONSTRAINT `fk_kitap_kutuphane_id` FOREIGN KEY (`kitap_kutuphane_id`) REFERENCES `kutuphane_tablosu` (`kutuphane_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kitap_tablosu`
--

LOCK TABLES `kitap_tablosu` WRITE;
/*!40000 ALTER TABLE `kitap_tablosu` DISABLE KEYS */;
INSERT INTO `kitap_tablosu` VALUES ('145','labirent2','yayinevi2',2),('146','labirent3','yayinevi3',2),('147','labirent4','yayinevi4',1),('158','labirent5','yayinevi5',2),('656','Labirent','yayınevi1',1);
/*!40000 ALTER TABLE `kitap_tablosu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-15 13:27:57
