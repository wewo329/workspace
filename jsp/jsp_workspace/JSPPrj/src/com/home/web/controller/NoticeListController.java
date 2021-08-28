package com.home.web.controller;

import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.home.web.entity.Notice;

@WebServlet("/notice/list")
public class NoticeListController extends HttpServlet{
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		List<Notice> list = new ArrayList<Notice>();
		
		String url = "jdbc:mysql://172.30.1.30/web";
		String sql = "select * from NOTICE";

		try {
			Class.forName("com.mysql.jdbc.Driver");
			Connection con = DriverManager.getConnection(url, "web", "Cyber2020!@");
			Statement st = con.createStatement();
			ResultSet rs = st.executeQuery(sql);

			while (rs.next()) {
				
				int id = rs.getInt("id");
				String title = rs.getString("title");
				Date regDate = rs.getDate("regdate");
				String writerId = rs.getString("writer_id");
				int hit = rs.getInt("hit");
				String files = rs.getString("files");
				String content = rs.getString("content");
				
				Notice notice = new Notice(id, title, regDate, writerId, hit, files, content);
				list.add(notice);
			}

			request.setAttribute("list", list);			
			request.getRequestDispatcher("/WEB-INF/view/notice/list.jsp").forward(request, response);
			
			rs.close();
			st.close();
			con.close();	
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}
}
