<html>
<head>
<title>Secret Sale</title>
</head>
<body>
<h1>Sale page</h1>
<hr>
<p>Click on any item to view the full details</p>
<?php

$db = mysql_connect("localhost","compsci_myuser","compsci_mypassword") or die("Error ".mysql_error($db));
mysql_select_db("compsci_examples");

$sql = "SELECT * FROM products ORDER BY id";

$result = mysql_query($sql) or die("Error ".mysql_error($db));
while($row = mysql_fetch_assoc($result)) {

?><div style='display: table-row;'>
	<span style='display: table-cell; border: 1px solid #CCC;'>
		<? echo $row['name']; ?>
	</span>
	<span style='display: table-cell; border: 1px solid #CCC;'>
	&pound;<? echo $row['price']; ?>
	</span>
	<span style='display: table-cell; border: 1px solid #CCC;'>
	<a href='item.php?id=<? echo $row['id']?>'>Click for more information</a>
	</span>
</div>
<?


}

?>
</body>
</html>
