-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2023 at 05:53 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `payroll`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_detail`
--

CREATE TABLE `admin_detail` (
  `Name` text NOT NULL,
  `Mobile` bigint(11) NOT NULL,
  `Email` text NOT NULL,
  `Password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_detail`
--

INSERT INTO `admin_detail` (`Name`, `Mobile`, `Email`, `Password`) VALUES
('anisha kumari', 8085524857, 'ani@gmail.com', 'ani123'),
('Subhash Kumar', 9098606846, 'subhash2004ka@gmail.com', '1234'),
('roy rr', 9589030618, 'roy@gmail.com', 'roy123'),
('ranika sahu', 8889163207, 'ranika@gmail.com', 'ranika123'),
('anjali  kumari', 7489287181, 'anjalikumari8269@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `emp_detail`
--

CREATE TABLE `emp_detail` (
  `Name` text NOT NULL,
  `Address` text NOT NULL,
  `City` text NOT NULL,
  `Pincode` int(6) NOT NULL,
  `Mobile` bigint(20) NOT NULL,
  `Degree` text NOT NULL,
  `Designation` text NOT NULL,
  `Salary` int(11) NOT NULL,
  `Bank_no` bigint(11) NOT NULL,
  `Email` text NOT NULL,
  `Password` text NOT NULL,
  `Status` text NOT NULL DEFAULT 'active',
  `Branch` text NOT NULL,
  `Empid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emp_detail`
--

INSERT INTO `emp_detail` (`Name`, `Address`, `City`, `Pincode`, `Mobile`, `Degree`, `Designation`, `Salary`, `Bank_no`, `Email`, `Password`, `Status`, `Branch`, `Empid`) VALUES
('subhash kumar', 'chattisgarh', 'raipur', 492661, 9098606846, 'BCA', 'python developer', 50000, 7318001000128604, 'subhash2004ka@gmail.com', '1234', 'deactive', 'IT', 100),
('anisha kumari', 'chattisgarh', 'raipur', 492661, 9589030618, 'BCA', 'web developer', 50000, 1233001000128604, 'ani@gmail.com', 'ani123', 'active', 'IT', 101),
('ranika mandal', 'durg,c.g.', 'bhilai', 499860, 8889163207, 'BCA', 'WEB Devloper', 50000, 1234567891234567, 'sahuranika557@gmail.com', '1234', 'active', 'IT', 102),
('raja singh', 'c.g.', 'bhilapur', 894251, 9589030618, 'BSC', 'Software developer', 60000, 1234567891234568, 'raja@gmail.com', '1234', 'active', 'IT', 103),
('anjali kumari', '103, New, HAL 3rd Stage, New Tippasandra, Bengaluru, Karnataka', 'Bengaluru ', 560075, 7489287181, 'BSC', 'paytho developer', 99999, 123456789123456789, 'anjalikumari8269@gmail.com', '1234', 'deactive', 'IT', 104),
('raj kumar', 'cg', 'raipur', 492001, 9098606846, 'B.Tech', 'BSC developer', 50000, 1234567891234567, 'rajaraj@gmail.com', '1234', 'active', 'IT', 105);

-- --------------------------------------------------------

--
-- Table structure for table `emp_report`
--

CREATE TABLE `emp_report` (
  `Name` text NOT NULL,
  `Email` text NOT NULL,
  `Leave_Day` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Reason` text NOT NULL,
  `Status` text NOT NULL DEFAULT 'on',
  `Approve` text DEFAULT NULL,
  `Month` text DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emp_report`
--

INSERT INTO `emp_report` (`Name`, `Email`, `Leave_Day`, `Date`, `Reason`, `Status`, `Approve`, `Month`, `Year`) VALUES
('subhash kumar', 'subhash2004ka@gmail.com', 3, '2023-01-18', 'dryry', 'off', 'approved', 'January', 2023),
('subhash kumar', 'subhash2004ka@gmail.com', 3, '2023-01-18', 'ryttu', 'off', 'Reject', 'January', 2023),
('subhash kumar', 'subhash2004ka@gmail.com', 5, '2023-01-22', 'rftyr', 'off', 'approved', 'January', 2023),
('raja singh', 'raja@gmail.com', 5, '2023-01-18', 'dfht', 'off', 'approved', 'January', 2023),
('raja singh', 'raja@gmail.com', 3, '2023-01-18', 'er5y5er', 'off', 'Reject', 'January', 2023),
('anisha kumari', 'ani@gmail.com', 5, '2023-01-23', 'aefdqw', 'off', 'approved', 'January', 2023),
('subhash kumar', 'subhash2004ka@gmail.com', 1, '2023-01-17', 'dr', 'Reject', 'Reject', 'January', 2023),
('raja singh', 'raja@gmail.com', 4, '2023-01-23', 'drtg', 'off', 'approved', 'January', 2023),
('subhash kumar', 'subhash2004ka@gmail.com', 5, '2023-01-23', 'jk', 'Reject', 'Reject', 'January', 2023),
('anjali kumari', 'anjalikumari8269@gmail.com', 5, '2023-02-01', 'asd', 'on', 'approved', 'January', 2023),
('anjali kumari', 'anjalikumari8269@gmail.com', 5, '2023-02-01', 'drty', 'Reject', 'Reject', 'January', 2023),
('subhash kumar', 'subhash2004ka@gmail.com', 4, '2023-02-02', 'reason', 'on', 'approved', 'January', 2023);

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `Name` text NOT NULL,
  `Email` text NOT NULL,
  `Allowance` int(11) NOT NULL,
  `Deduction` int(11) NOT NULL,
  `Total_Salary` int(11) NOT NULL,
  `Month` text NOT NULL,
  `Year` int(11) NOT NULL,
  `Status` text DEFAULT 'unpaid'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`Name`, `Email`, `Allowance`, `Deduction`, `Total_Salary`, `Month`, `Year`, `Status`) VALUES
('subhash kumar', 'subhash2004ka@gmail.com', 45000, 5000, 50000, 'December', 2022, 'paid'),
('subhash kumar', 'subhash2004ka@gmail.com', 48000, 2000, 50000, 'November', 2022, 'paid'),
('anisha kumari', 'ani@gmail.com', 48000, 2000, 50000, 'December', 2022, 'paid');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_detail`
--
ALTER TABLE `admin_detail`
  ADD UNIQUE KEY `Email` (`Email`) USING HASH;

--
-- Indexes for table `emp_detail`
--
ALTER TABLE `emp_detail`
  ADD PRIMARY KEY (`Empid`),
  ADD UNIQUE KEY `Email` (`Email`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_detail`
--
ALTER TABLE `emp_detail`
  MODIFY `Empid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

DELIMITER $$
--
-- Events
--
CREATE DEFINER=`root`@`localhost` EVENT `emp_detail_anjalikumari8269@gmail.com` ON SCHEDULE AT '2023-02-06 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `emp_detail` SET `Status`='active' WHERE Email='anjalikumari8269@gmail.com'$$

CREATE DEFINER=`root`@`localhost` EVENT `emp_report_anjalikumari8269@gmail.com` ON SCHEDULE AT '2023-02-06 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `emp_report` SET `Status`='off' WHERE Email='anjalikumari8269@gmail.com'$$

CREATE DEFINER=`root`@`localhost` EVENT `emp_detail_subhash2004ka@gmail.com` ON SCHEDULE AT '2023-02-06 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `emp_detail` SET `Status`='active' WHERE Email='subhash2004ka@gmail.com'$$

CREATE DEFINER=`root`@`localhost` EVENT `emp_report_subhash2004ka@gmail.com` ON SCHEDULE AT '2023-02-06 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `emp_report` SET `Status`='off' WHERE Email='subhash2004ka@gmail.com'$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
