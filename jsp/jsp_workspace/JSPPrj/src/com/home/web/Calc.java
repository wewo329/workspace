package com.home.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/calc")
public class Calc extends HttpServlet {
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		Cookie cookies[] = req.getCookies();

		String v = req.getParameter("v");
		String op = req.getParameter("operator");

		PrintWriter out = resp.getWriter();

		if (op.equals("=")) {
			int x = 0;
			int y = Integer.parseInt(v);
			int result = 0;

			for (Cookie cookie : cookies) {
				if (cookie.getName().equals("value")) {
					x = Integer.parseInt(cookie.getValue());
				}
			}

			for (Cookie cookie : cookies) {
				if (cookie.getName().equals("op")) {
					String operator = cookie.getValue();
					System.out.println(operator);
					System.out.printf("%d %d", x, y);
					if (operator.equals("+"))
						result = x + y;
					else
						result = x - y;

				}
			}

			out.printf("result is %d", result);

		} else {
			// 쿠키 저장.
			Cookie valueCookie = new Cookie("value", v);
			Cookie opCookie = new Cookie("op", op);

			resp.addCookie(valueCookie);
			resp.addCookie(opCookie);

			resp.sendRedirect("/calc.html");
		}

	}
}
