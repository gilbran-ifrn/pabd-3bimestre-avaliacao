CREATE DATABASE  IF NOT EXISTS `clinica` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `clinica`;
-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (x86_64)
--
-- Host: localhost    Database: clinica
-- ------------------------------------------------------
-- Server version	8.4.2

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
-- Table structure for table `consulta`
--

DROP TABLE IF EXISTS `consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consulta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idPaciente` int NOT NULL,
  `idProfissional` int NOT NULL,
  `datahora` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_atende_idx` (`idProfissional`),
  KEY `fk_reserva_idx` (`idPaciente`),
  CONSTRAINT `fk_atende` FOREIGN KEY (`idProfissional`) REFERENCES `profissional` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_reserva` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consulta`
--

LOCK TABLES `consulta` WRITE;
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` VALUES 
(1,1,1,'2024-12-15 10:30:00'),
(2,2,2,'2025-01-10 14:00:00'),
(3,3,3,'2025-02-05 16:00:00'),
(4,4,4,'2025-02-10 08:45:00'),
(5,5,5,'2025-01-20 11:15:00'),
(6,6,6,'2025-03-01 13:30:00'),
(7,7,1,'2025-03-15 09:00:00'),
(8,8,7,'2025-02-25 15:00:00'),
(9,9,2,'2025-01-30 10:00:00'),
(10,10,3,'2025-02-28 17:00:00');
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL UNIQUE,
  `senha` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES 
(1,'Ana Silva','ana.silva@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(2,'Carlos Souza','carlos.souza@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(3,'Mariana Oliveira','mariana.oliveira@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(4,'Rafael Pereira','rafael.pereira@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(5,'Fernanda Costa','fernanda.costa@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(6,'Bruno Almeida','bruno.almeida@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(7,'Luiza Martins','luiza.martins@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(8,'Pedro Santos','pedro.santos@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(9,'Beatriz Rodrigues','beatriz.rodrigues@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886'),
(10,'Gabriel Fernandes','gabriel.fernandes@example.com','scrypt:32768:8:1$MxN1ETaizFENYTiE$812933f014e4ffb6836a7bed5e4e7725d19bd7a0df956fad0e0839b97d9a596c8849ae66c9f8b392fc20eb30f7a7baeb335dff2b5bbbacd36b66075429987886');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profissional`
--

DROP TABLE IF EXISTS `profissional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profissional` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `especialidade` varchar(100) NOT NULL,
  `descricao` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profissional`
--

LOCK TABLES `profissional` WRITE;
/*!40000 ALTER TABLE `profissional` DISABLE KEYS */;
INSERT INTO `profissional` VALUES 
(1,'Dr. João Pereira','Cardiologia','Especialista em cardiologia intervencionista com 15 anos de experiência.'),
(2,'Dra. Maria Souza','Dermatologia','Atua na clínica dermatológica, focada em tratamentos estéticos e de doenças de pele.'),
(3,'Dr. Luís Oliveira','Pediatria','Experiência ampla no atendimento pediátrico, garantindo cuidados com crianças.'),
(4,'Dra. Camila Rodrigues','Ortopedia','Especialista em cirurgias ortopédicas e reabilitação.'),
(5,'Dr. Roberto Martins','Neurologia','Focado em tratamentos para doenças neurológicas e reabilitação.'),
(6,'Dra. Helena Costa','Psiquiatria','Atende pacientes com transtornos mentais e promove acompanhamento terapêutico.'),
(7,'Dr. Felipe Santos','Gastroenterologia','Experiência em procedimentos endoscópicos e diagnósticos de doenças gastrointestinais.');
/*!40000 ALTER TABLE `profissional` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-03 10:00:47
