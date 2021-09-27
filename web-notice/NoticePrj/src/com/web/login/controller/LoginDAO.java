package com.web.login.controller;

import java.sql.*;

import com.web.dbinform.DBVO;
import com.web.login.module.LoginDTO;

public class LoginDAO {
	
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	
	public LoginDAO() {
		try {
			DBVO db = new DBVO();
			Class.forName(db.getDriver());
			conn = DriverManager.getConnection(db.getUrl(), db.getId(), db.getPwd());
			db = null;
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
	}
	
	public int checkUser(String email, String pwd) {
		String sql = "select pwd from USER where email = ?";
		
		try {
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, email);
			rs = pstmt.executeQuery();
			
			if (rs.next()) {
				if (rs.getString(1).equals(pwd)) return 1;
				else return 0;
			}
			
			return -1;
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return -2; // 오류
	}
	
	public LoginDTO login(String email, String pwd) {
		String sql = "select * from USER where email = ?";
		
		try {
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, email);
			rs = pstmt.executeQuery();
			
			rs.next();
			int id = rs.getInt("id");
			String name = rs.getString("name");
			String gender = rs.getString("gender");
			Date regDate = rs.getDate("regDate");
			
			LoginDTO user = new LoginDTO(id, email, pwd, name, gender, regDate);
			return user; 
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}
}
