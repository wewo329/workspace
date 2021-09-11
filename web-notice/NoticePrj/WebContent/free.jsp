<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="css/style.css">
	<meta charset="UTF-8">
	<script src="https://use.fontawesome.com/releases/v5.2.0/js/all.js"></script>
	<title>자유게시판</title>
</head>
<body>
	<div class="container">
		<jsp:include page="header.jsp"></jsp:include>
		<section>
	        <div class="screen">
	            <div class="search-box">
	                <input type="text" placeholder="Search for">
	            </div>
	            <table class="free-notice">
	                <colgroup>
	                    <col width="7%" />
	                    <col width="50%" />
	                    <col width="13%" />
	                    <col width="15%" />
	                    <col width="10%" />
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
					<c:forEach begin="0" end="19" varStatus="stat">
						<tr class="free-notice-content">
							<td>${stat.index}</td>
							<td><a class="color_link__" href="#">Hello? What are you doing now?</a></td>
							<td>Tineil</td>
							<td>2020-01-01</td>
							<td>3</td>
						</tr>
					</c:forEach>
						<tr>
							<td colspan="5">
								<div  class="free-notice-nav_bar">
									<span><a href="#"><i class="fas fa-arrow-circle-left"></i></a></span>
									<ul>
										<c:forEach begin="1" end="5" varStatus="stat">
											<li><a class="color_link__" href="#">${stat.index+10}</a></li>
										</c:forEach>
									</ul>
									<span><a href="#"><i class="fas fa-arrow-circle-right"></i></a></span>
								</div>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>
		<jsp:include page="footer.jsp"></jsp:include>
	</div>
</body>
</html>