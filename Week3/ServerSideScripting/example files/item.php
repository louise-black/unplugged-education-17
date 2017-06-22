<html>
<head>
<title>
Sale item
</title>
</head>
<body>
<?php

$db = mysql_connect("localhost","compsci_myuser","compsci_mypassword") or die("Error ".mysql_error($db));
mysql_select_db("compsci_examples");
$sql = "SELECT * FROM products WHERE id='".$_GET['id']."'";
$result = mysql_query($sql) or die("Error ".mysql_error($db));
$row = mysql_fetch_assoc($result);

?>
<h1>Item details</h1>
<hr>
<div>
<p>Name: <? echo $row['name']; ?></p>
<p>Description: <? echo $row['description']; ?></p>
<p>Price: &pound;<? echo $row['price']; ?></p>
<p><img src="<? echo $row['image']; ?>"></p>
</div>
</body>
</html>
