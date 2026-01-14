<?php

$login = $_POST['login'];
$password = $_POST['password'];

$conn = new PDO("mysql:host=localhost;dbname=db01", "root", "");

// $conn -> exec("INSERT INTO users" (login, password) Values ('$login', '$password'));




?>