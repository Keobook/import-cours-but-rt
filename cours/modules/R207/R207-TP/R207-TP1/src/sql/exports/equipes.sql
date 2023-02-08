-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 07, 2023 at 09:26 AM
-- Server version: 10.5.18-MariaDB-log
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_OPOLKA`
--

-- --------------------------------------------------------

--
-- Table structure for table `equipes`
--

CREATE TABLE `equipes` (
  `id` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `groupe` varchar(1) NOT NULL DEFAULT '0',
  `points` int(11) NOT NULL DEFAULT 0,
  `joues` int(11) NOT NULL DEFAULT 0,
  `gagnes` int(11) NOT NULL DEFAULT 0,
  `perdus` int(11) NOT NULL DEFAULT 0,
  `nuls` int(11) NOT NULL DEFAULT 0,
  `marques` int(11) NOT NULL DEFAULT 0,
  `encaisses` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `equipes`
--

INSERT INTO `equipes` (`id`, `nom`, `groupe`, `points`, `joues`, `gagnes`, `perdus`, `nuls`, `marques`, `encaisses`) VALUES
(1, 'Marseille', '0', 0, 0, 0, 0, 0, 0, 0),
(2, 'Toulouse', '0', 0, 0, 0, 0, 0, 0, 0),
(3, 'Angers', '0', 0, 0, 0, 0, 0, 0, 0),
(4, 'Nimes', '0', 0, 0, 0, 0, 0, 0, 0),
(5, 'Lille', '0', 0, 0, 0, 0, 0, 0, 0),
(6, 'Rennes', '0', 0, 0, 0, 0, 0, 0, 0),
(7, 'Montpellier', '0', 0, 0, 0, 0, 0, 0, 0),
(8, 'Dijon', '0', 0, 0, 0, 0, 0, 0, 0),
(9, 'Nantes', '0', 0, 0, 0, 0, 0, 0, 0),
(10, 'Monaco', '0', 0, 0, 0, 0, 0, 0, 0),
(11, 'Nice', '0', 0, 0, 0, 0, 0, 0, 0),
(12, 'Reims', '0', 0, 0, 0, 0, 0, 0, 0),
(13, 'St Etienne', '0', 0, 0, 0, 0, 0, 0, 0),
(14, 'Guingamp', '0', 0, 0, 0, 0, 0, 0, 0),
(15, 'Bordeaux', '0', 0, 0, 0, 0, 0, 0, 0),
(16, 'Strasbourg', '0', 0, 0, 0, 0, 0, 0, 0),
(17, 'Lyon', '0', 0, 0, 0, 0, 0, 0, 0),
(18, 'Amiens', '0', 0, 0, 0, 0, 0, 0, 0),
(19, 'Paris SG', '0', 0, 0, 0, 0, 0, 0, 0),
(20, 'Caen', '0', 0, 0, 0, 0, 0, 0, 0),
(22, 'Béziers', '0', 0, 0, 0, 0, 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipes`
--
ALTER TABLE `equipes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `equipes`
--
ALTER TABLE `equipes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
