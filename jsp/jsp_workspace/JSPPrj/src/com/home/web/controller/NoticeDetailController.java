package com.home.web.controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.home.web.entity.Notice;

@WebServlet("/notice/detail")
public class NoticeDetailController extends HttpServlet{
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int id = Integer.valueOf(request.getParameter("id"));

		String url = "jdbc:mysql://172.30.1.30/web";
		String sql = "select * from NOTICE where id=?";

		try {
			Class.forName("com.mysql.jdbc.Driver");
			
			Connection con = DriverManager.getConnection(url, "web", "Cyber2020!@");
			PreparedStatement st = con.prepareStatement(sql);

			st.setInt(1, id);

			ResultSet rs = st.executeQuery();
			rs.next();

			String title = rs.getString("title");
			Date regDate = rs.getDate("regdate");
			String writerId = rs.getString("writer_id");
			int hit = rs.getInt("hit");
			String files = rs.getString("files");
			String content = rs.getString("content");

			rs.close();
			st.close();
			con.close();
			Notice notice = new Notice(id, title, regDate, writerId, hit, files, content);
			request.setAttribute("n", notice);
			/*
			request.setAttribute("title", title);
			request.setAttribute("regDate", regDate);
			request.setAttribute("writerId", writerId);
			request.setAttribute("hit", hit);
			request.setAttribute("files", files);
			request.setAttribute("content", content);
			*/
			
			RequestDispatcher dispatcher = request.getRequestDispatcher("/WEB-INF/view/notice/detail.jsp");
			dispatcher.forward(request, response);
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
}
