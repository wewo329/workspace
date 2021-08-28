package com.home.web;

import java.sql.*;

public class Program {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		
		String url = "jdbc:mysql://172.30.1.30/web";
		String sql = "delete from NOTICE where id=?";

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection(url, "web", "Cyber2020!@");
		Statement st = con.createStatement();
		ResultSet rs = st.executeQuery(sql);
		
		System.out.println();
		
		rs.close();
		st.close();
		con.close();
	}
}
