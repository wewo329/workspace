package com.web.dbinform;

public class DBVO {
	private final String url = "jdbc:mysql://172.30.1.30:3306/web";
	private final String id = "web";
	private final String pwd = "Cyber2020!@";
	private final String driver = "com.mysql.cj.jdbc.Driver";
	
	public String getUrl() {
		return url;
	}
	public String getId() {
		return id;
	}
	public String getPwd() {
		return pwd;
	}
	public String getDriver() {
		return driver;
	}
}
