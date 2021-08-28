package com.home.web;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/spag")
public class Spag extends HttpServlet{
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int num = 0;

		String num_ = req.getParameter("n");
		if (num_ != null && !num_.equals(""))
			num = Integer.parseInt(num_);
		
		String result;
		if (num%2 == 1)
			result = "홀수";
		else 
			result = "짝수";
		
		req.setAttribute("result", result);
		
		String names[] = {"newlec", "dragon"};
		req.setAttribute("names", names);
		
		Map<String, Object> notice = new HashMap<String, Object>();
		notice.put("id", 1);
		notice.put("title", "이거 참 신기하네");
		req.setAttribute("notice", notice);
		
		RequestDispatcher dispatcher
			= req.getRequestDispatcher("spag.jsp");
		dispatcher.forward(req, resp);
	}
}
