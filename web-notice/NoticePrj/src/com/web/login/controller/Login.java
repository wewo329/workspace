package com.web.login.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.web.login.module.LoginDTO;

@WebServlet("/login")
public class Login extends HttpServlet {
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		resp.setCharacterEncoding("UTF-8");
		resp.setContentType("text/html; charset=UTF-8");
		req.setCharacterEncoding("UTF-8");
		String email = req.getParameter("email");
		String pwd = req.getParameter("pwd");
		
		LoginDAO loginDAO = new LoginDAO();
		int flag = loginDAO.checkUser(email, pwd);
		
		switch (flag) {
			case 1:
				// 로그인 성공!
				LoginDTO loginDTO = loginDAO.login(email, pwd);
				Cookie uidCook = new Cookie("uid", Integer.toString(loginDTO.getId()));
				Cookie emailCook = new Cookie("email", loginDTO.getEmail());
				Cookie nameCook = new Cookie("name", loginDTO.getName());
				resp.addCookie(uidCook);
				resp.addCookie(emailCook);
				resp.addCookie(nameCook);
				resp.sendRedirect("/home.jsp");
				break;
			case 0:
				// 비밀번호가 틀린 경우
			case -1:
				// 이메일 자체가 없는 경우
				resp.sendRedirect("/login-fail.jsp?fail=" + flag);
				break;
			case -2:
				resp.sendRedirect("/errorpage.html");
				break;
			default:
				break;
		}
	}
}
