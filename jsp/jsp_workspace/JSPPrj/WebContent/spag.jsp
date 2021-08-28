<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<%
pageContext.setAttribute("result", "hello");
%>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<span>${requestScope.result} 입니다.</span>
	<span>${names[1]}</span>
	<span>${notice.title}</span>
	<span>${result}</span>
	<span>${header.host}</span>
</body>
</html>