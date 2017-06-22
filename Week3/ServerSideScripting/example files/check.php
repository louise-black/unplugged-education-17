<html>
<head>
<title>Sale code access!</title>
</head>
<body>
<?php

if($_GET['code']=="MAGICDUCKS") {

?>Yay! Let's go shopping! 
<a href="sale.php">Click here to go the secret sale</a>
<?
} else {

?>
You didn't have the code. Better luck next year!
<?

}

?>
</body>
</html>