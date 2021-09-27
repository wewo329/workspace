<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
	<header class="home-header">
		<a href="home.jsp">Home</a>
	</header>
	<section class="login-section">
		
		<form action="login" method="POST" id="login-form">
			<input type="text" placeholder="Email" required name="email">
			<input type="password" placeholder="Password" required name="pwd">
			<input type="submit" value="Log In">
			<a href="join.jsp">회원가입</a>
		</form>
	</section>
</body>
</html>