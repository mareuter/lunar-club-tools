package com.typeiisoft.lct.utils;

import java.text.DecimalFormat;

/**
 * This class is designed to provide varioud string formatting methods. It 
 * should only be used via the static methods as instantiation is not allowed.
 * @author Michael Reuter
 *
 */
public final class StrFormat {
	
	/**
	 * This function formats a latitude or longitude value into one with 
	 * a direction label and two numbers after the decimal.
	 * @param coordType : The coord type: lat/lon.
	 * @param coord : The value of the latitude or longitude.
	 * @return : A formatted string.
	 */
	public static String coordFormat(String coordType, double coord) {
		String dir = "";
		if ("lat" == coordType.toLowerCase()) {
			if (coord < 0.0) {
				dir = "S";
			}
			else {
				dir = "N";
			}
		}
		if ("lon" == coordType.toLowerCase()) {
			if (coord < 0.0) {
				dir = "W";
			}
			else {
				dir = "E";
			}
		}
		String dbl_fmt = StrFormat.formatDouble(Math.abs(coord), 2);
		StringBuffer buf = new StringBuffer(dbl_fmt);
		// This is the degree symbol in unicode.
		buf.append("\u00b0 ");
		buf.append(dir);
		return buf.toString();
	}
	
	/**
	 * This function formats a double with a given precision. The resulting 
	 * string will have that many numbers after the decimal.
	 * @param value : The value to format.
	 * @param precision : The number of digits after the decimal to keep.
	 * @return : A formatted string.
	 */
	public static String formatDouble(double value, int precision) {
		StringBuffer buf = new StringBuffer(".");
		for (int i = 0; i < precision; i++) {
			buf.append("#");
		}
		DecimalFormat format = new DecimalFormat(buf.toString());
		return format.format(value);
	}
	
	/**
	 * This function takes a many word string and converts it to a multi-line 
	 * string.
	 * @param value : The string to format.
	 * @return : The formatted string.
	 */
	public static String multiLine(String value) {
		String[] results = value.split("\\s+");
		StringBuffer buf = new StringBuffer();
		for (String result : results) {
			buf.append(result).append(System.getProperty("line.separator"));
		}
		return buf.toString().trim();
	}
	
	/**
	 * Do not allow class instantiation.
	 */
	private StrFormat() {
	}
}
