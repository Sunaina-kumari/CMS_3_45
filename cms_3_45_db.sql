-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2021 at 11:45 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cms_3_45_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `dname` varchar(100) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `fee` float(20,2) NOT NULL,
  `duration` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`dname`, `cname`, `fee`, `duration`) VALUES
('IT', 'BCA', 100000.00, '3 yrs'),
('Commerce', 'Bcom', 90000.00, '3 yrs');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `dname` varchar(100) NOT NULL,
  `head_of_dept` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dname`, `head_of_dept`) VALUES
('Commerce', 'simran'),
('IT', 'sarita'),
('Science', 'mukul');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `rollno` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `dept` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL,
  `pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`rollno`, `name`, `phone`, `gender`, `dob`, `address`, `dept`, `course`, `pic`) VALUES
(12, 'wer', '2342342344', 'f', '2010-11-23', 'delhi', 'IT', 'BCA', 'default_user.png'),
(102, 'aman', '98989', 'f', '1999-02-23', 'jalandhar', 'IT', 'MCA', 'default_user.png'),
(103, 'aman', '9898989', 'f', '2000-02-12', 'delhi', 'IT', 'MCA', 'default_user.png'),
(104, 'ekam', '98989889', 'm', '2021-11-10', 'delhi', 'IT', 'BCA', 'default_user.png'),
(108, 'riya', '66666', 'f', '2010-11-26', 'jaipur', 'Commerce', 'Bcom', 'default_user.png'),
(109, 'riya', '66666', 'f', '2010-11-26', 'jaipur', 'Commerce', 'Bcom', '1637581211hj.jpg'),
(110, 'riya', '66666', 'f', '2010-11-26', 'jaipur', 'Commerce', 'Bcom', '1637581170cat5.png');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('divyanshi', '123', 'Admin'),
('ekam', '123', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`cname`),
  ADD KEY `dname` (`dname`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dname`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`rollno`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `const1` FOREIGN KEY (`dname`) REFERENCES `department` (`dname`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
