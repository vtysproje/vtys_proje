-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: kutuphanedb
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `kitapyazar_tablosu`
--

DROP TABLE IF EXISTS `kitapyazar_tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kitapyazar_tablosu` (
  `kty_id` int NOT NULL AUTO_INCREMENT,
  `kty_kitap_isbn` varchar(13) NOT NULL,
  `kty_yazar_id` int NOT NULL,
  PRIMARY KEY (`kty_id`),
  UNIQUE KEY `kty_id_UNIQUE` (`kty_id`),
  KEY `fk_kty_kitap_isbn_idx` (`kty_kitap_isbn`),
  KEY `fk_kty_yazar_id_idx` (`kty_yazar_id`),
  CONSTRAINT `fk_kty_kitap_isbn` FOREIGN KEY (`kty_kitap_isbn`) REFERENCES `kitap_tablosu` (`kitap_isbn`),
  CONSTRAINT `fk_kty_yazar_id` FOREIGN KEY (`kty_yazar_id`) REFERENCES `yazar_tablosu` (`yazar_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kitapyazar_tablosu`
--

LOCK TABLES `kitapyazar_tablosu` WRITE;
/*!40000 ALTER TABLE `kitapyazar_tablosu` DISABLE KEYS */;
INSERT INTO `kitapyazar_tablosu` VALUES (1,'3165',1),(2,'3598',2),(3,'4136',3),(4,'4781',4),(5,'5896',5),(6,'5987',6),(7,'7231',7),(8,'8102',8),(9,'9637',9);
/*!40000 ALTER TABLE `kitapyazar_tablosu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-17  1:37:03
