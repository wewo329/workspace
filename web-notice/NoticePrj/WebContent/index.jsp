<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="css/style.css">
    <meta charset="UTF-8">
    <title>Insert title here</title>
</head>

<body>
    <div class="container">
    	<jsp:include page="header.jsp"></jsp:include>
        <section class="free-screen">
            <table class="free-table">
                <colgroup>
                    <col width="15%" />
                    <col width="35%" />
                    <col width="15%" />
                    <col width="20%" />
                    <col width="15%" />
                </colgroup>
                <thead>
                    <tr>
                        <th>No</th>
                        <th>title</th>
                        <th>name</th>
                        <th>regDate</th>
                        <th>hit</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td><a href="#">Hello? What are you doing now?</a></td>
                        <td>Tineil</td>
                        <td>2020-01-01</td>
                        <td>3</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <jsp:include page="footer.jsp"></jsp:include>
    </div>
</body>

</html>