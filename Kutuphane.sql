-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: Kutuphane
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
-- Table structure for table `Adres_Tablosu`
--

DROP TABLE IF EXISTS `Adres_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Adres_Tablosu` (
  `adres_no` int NOT NULL,
  `adres_bilgisi` text NOT NULL,
  PRIMARY KEY (`adres_no`),
  UNIQUE KEY `adres_no_UNIQUE` (`adres_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Adres_Tablosu`
--

LOCK TABLES `Adres_Tablosu` WRITE;
/*!40000 ALTER TABLE `Adres_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Adres_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alinan_Tablosu`
--

DROP TABLE IF EXISTS `Alinan_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alinan_Tablosu` (
  `alinan_emanet_no` int NOT NULL,
  `alinan_alis_tarihi` date NOT NULL,
  `alinan_teslim_tarihi` date NOT NULL,
  `alinan_uye_id` int NOT NULL,
  `alinan_kitap_isbn` varchar(13) NOT NULL,
  `alinan_kutuphane_id` int NOT NULL,
  PRIMARY KEY (`alinan_emanet_no`),
  UNIQUE KEY `alinan_emanet_no_UNIQUE` (`alinan_emanet_no`),
  KEY `fk_kutuphane_id_idx` (`alinan_kutuphane_id`),
  KEY `fk_kitap_isbn_idx` (`alinan_kitap_isbn`),
  KEY `fk_alinan_uye_id_idx` (`alinan_uye_id`),
  CONSTRAINT `fk_alinan_kitap_isbn` FOREIGN KEY (`alinan_kitap_isbn`) REFERENCES `Kitap_Tablosu` (`kitap_isbn`),
  CONSTRAINT `fk_alinan_kutuphane_id` FOREIGN KEY (`alinan_kutuphane_id`) REFERENCES `Kutuphane_Tablosu` (`kutuphane_id`),
  CONSTRAINT `fk_alinan_uye_id` FOREIGN KEY (`alinan_uye_id`) REFERENCES `Uye_Tablosu` (`uye_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alinan_Tablosu`
--

LOCK TABLES `Alinan_Tablosu` WRITE;
/*!40000 ALTER TABLE `Alinan_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Alinan_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kategori-Kitap_Tablosu`
--

DROP TABLE IF EXISTS `Kategori-Kitap_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kategori-Kitap_Tablosu` (
  `ktk_id` int NOT NULL,
  `ktk_kategori_id` int NOT NULL,
  `ktk_kitap_isbn` varchar(13) NOT NULL,
  PRIMARY KEY (`ktk_id`),
  UNIQUE KEY `ktk_id_UNIQUE` (`ktk_id`),
  KEY `fk_ktk_kategori_id_idx` (`ktk_kategori_id`),
  KEY `fk_ktk_kitap_isbn_idx` (`ktk_kitap_isbn`),
  CONSTRAINT `fk_ktk_kategori_id` FOREIGN KEY (`ktk_kategori_id`) REFERENCES `Kategori_Tablosu` (`kategori_id`),
  CONSTRAINT `fk_ktk_kitap_isbn` FOREIGN KEY (`ktk_kitap_isbn`) REFERENCES `Kitap_Tablosu` (`kitap_isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kategori-Kitap_Tablosu`
--

LOCK TABLES `Kategori-Kitap_Tablosu` WRITE;
/*!40000 ALTER TABLE `Kategori-Kitap_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kategori-Kitap_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kategori_Tablosu`
--

DROP TABLE IF EXISTS `Kategori_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kategori_Tablosu` (
  `kategori_id` int NOT NULL,
  `kategori_adi` varchar(45) NOT NULL,
  PRIMARY KEY (`kategori_id`),
  UNIQUE KEY `kategori_id_UNIQUE` (`kategori_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kategori_Tablosu`
--

LOCK TABLES `Kategori_Tablosu` WRITE;
/*!40000 ALTER TABLE `Kategori_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kategori_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kitap-Yazar_Tablosu`
--

DROP TABLE IF EXISTS `Kitap-Yazar_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kitap-Yazar_Tablosu` (
  `kty_id` int NOT NULL,
  `kty_kitap_isbn` varchar(13) NOT NULL,
  `kty_yazar_id` int NOT NULL,
  PRIMARY KEY (`kty_id`),
  UNIQUE KEY `kty_id_UNIQUE` (`kty_id`),
  KEY `fk_kty_kitap_isbn_idx` (`kty_kitap_isbn`),
  KEY `fk_kty_yazar_id_idx` (`kty_yazar_id`),
  CONSTRAINT `fk_kty_kitap_isbn` FOREIGN KEY (`kty_kitap_isbn`) REFERENCES `Kitap_Tablosu` (`kitap_isbn`),
  CONSTRAINT `fk_kty_yazar_id` FOREIGN KEY (`kty_yazar_id`) REFERENCES `Yazar_Tablosu` (`yazar_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kitap-Yazar_Tablosu`
--

LOCK TABLES `Kitap-Yazar_Tablosu` WRITE;
/*!40000 ALTER TABLE `Kitap-Yazar_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kitap-Yazar_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kitap_Tablosu`
--

DROP TABLE IF EXISTS `Kitap_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kitap_Tablosu` (
  `kitap_isbn` varchar(13) NOT NULL,
  `kitap_baslik` varchar(45) NOT NULL,
  `kitap_yayinevi` varchar(100) NOT NULL,
  `kitap_kutuphane_id` int NOT NULL,
  PRIMARY KEY (`kitap_isbn`),
  UNIQUE KEY `kitap_isbn_UNIQUE` (`kitap_isbn`),
  KEY `fk_kitap_kutuphane_id_idx` (`kitap_kutuphane_id`),
  CONSTRAINT `fk_kitap_kutuphane_id` FOREIGN KEY (`kitap_kutuphane_id`) REFERENCES `Kutuphane_Tablosu` (`kutuphane_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kitap_Tablosu`
--

LOCK TABLES `Kitap_Tablosu` WRITE;
/*!40000 ALTER TABLE `Kitap_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kitap_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kutuphane_Tablosu`
--

DROP TABLE IF EXISTS `Kutuphane_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Kutuphane_Tablosu` (
  `kutuphane_id` int NOT NULL,
  `kutuphane_isim` varchar(100) NOT NULL,
  `kutuphane_adres_no` int NOT NULL,
  PRIMARY KEY (`kutuphane_id`),
  UNIQUE KEY `kutuphane_id_UNIQUE` (`kutuphane_id`),
  KEY `fk_kutuphane_adres_no_idx` (`kutuphane_adres_no`),
  CONSTRAINT `fk_kutuphane_adres_no` FOREIGN KEY (`kutuphane_adres_no`) REFERENCES `Adres_Tablosu` (`adres_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kutuphane_Tablosu`
--

LOCK TABLES `Kutuphane_Tablosu` WRITE;
/*!40000 ALTER TABLE `Kutuphane_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Kutuphane_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Uye_Tablosu`
--

DROP TABLE IF EXISTS `Uye_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Uye_Tablosu` (
  `uye_id` int NOT NULL,
  `uye_adi` varchar(45) NOT NULL,
  `uye_soyadi` varchar(45) NOT NULL,
  `uye_tel` varchar(11) NOT NULL,
  `uye_mail` varchar(45) NOT NULL,
  `uye_adres_no` int NOT NULL,
  PRIMARY KEY (`uye_id`),
  UNIQUE KEY `uye_id_UNIQUE` (`uye_id`),
  UNIQUE KEY `uye_mail_UNIQUE` (`uye_mail`),
  UNIQUE KEY `uye_tel_UNIQUE` (`uye_tel`),
  KEY `fk_adres_no_idx` (`uye_adres_no`),
  CONSTRAINT `fk_uye_adres_no` FOREIGN KEY (`uye_adres_no`) REFERENCES `Adres_Tablosu` (`adres_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Uye_Tablosu`
--

LOCK TABLES `Uye_Tablosu` WRITE;
/*!40000 ALTER TABLE `Uye_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Uye_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Yazar_Tablosu`
--

DROP TABLE IF EXISTS `Yazar_Tablosu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Yazar_Tablosu` (
  `yazar_id` int NOT NULL,
  `yazar_ad` varchar(45) NOT NULL,
  `yazar_soyad` varchar(45) NOT NULL,
  PRIMARY KEY (`yazar_id`),
  UNIQUE KEY `yazar_id_UNIQUE` (`yazar_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Yazar_Tablosu`
--

LOCK TABLES `Yazar_Tablosu` WRITE;
/*!40000 ALTER TABLE `Yazar_Tablosu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Yazar_Tablosu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-14 23:28:32
