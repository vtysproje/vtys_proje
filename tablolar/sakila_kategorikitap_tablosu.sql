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
-- Table structure for table `kategorikitap_tablosu`
--

DROP TABLE IF EXISTS `kategorikitap_tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kategorikitap_tablosu` (
  `ktk_id` int NOT NULL,
  `ktk_kategori_id` int NOT NULL,
  `ktk_kitap_isbn` varchar(13) NOT NULL,
  PRIMARY KEY (`ktk_id`),
  UNIQUE KEY `ktk_id_UNIQUE` (`ktk_id`),
  KEY `fk_ktk_kategori_id_idx` (`ktk_kategori_id`),
  KEY `fk_ktk_kitap_isbn_idx` (`ktk_kitap_isbn`),
  CONSTRAINT `fk_ktk_kategori_id` FOREIGN KEY (`ktk_kategori_id`) REFERENCES `kategori_tablosu` (`kategori_id`),
  CONSTRAINT `fk_ktk_kitap_isbn` FOREIGN KEY (`ktk_kitap_isbn`) REFERENCES `kitap_tablosu` (`kitap_isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategorikitap_tablosu`
--

LOCK TABLES `kategorikitap_tablosu` WRITE;
/*!40000 ALTER TABLE `kategorikitap_tablosu` DISABLE KEYS */;
INSERT INTO `kategorikitap_tablosu` VALUES (1,1,'656'),(2,1,'145'),(3,1,'146'),(4,2,'147');
/*!40000 ALTER TABLE `kategorikitap_tablosu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-15 13:27:58
