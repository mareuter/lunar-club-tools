package com.typeiisoft.lct.utils;

import java.util.Calendar;
import java.util.GregorianCalendar;

import android.util.Log;

import com.mhuss.AstroLib.Astro;
import com.mhuss.AstroLib.AstroDate;
import com.mhuss.AstroLib.Lunar;
import com.mhuss.AstroLib.LunarCalc;
import com.mhuss.AstroLib.NoInitException;
import com.mhuss.AstroLib.ObsInfo;

/**
 * This class handles calling calculations and returning various bits of 
 * information about the moon. It will also handle the logic for determining 
 * if a lunar feature is visible.
 * @author Michael Reuter
 *
 */
public class MoonInfo {
	/** Logging tag. */
	private static final String TAG = "MoonInfo";
	/** The current date and time for all observation information. */
	private AstroDate obsDate;
	/** Flag to stop objects from being created unnecessarily */
	private boolean isInitialized = false;
	/** Object that does most of the calculations. */
	private Lunar lunar;
	/** Object that holds the observing site information. */
	private ObsInfo obsInfo;
	
	/**
	 * This function is the class constructor.
	 */
	public MoonInfo() {
		if (!this.isInitialized) {
			this.obsDate = new AstroDate(Calendar.DATE, Calendar.MONTH, 
					Calendar.YEAR, Calendar.HOUR_OF_DAY, Calendar.MINUTE, 
					Calendar.SECOND);
			this.lunar = new Lunar(this.getJulianCenturies());
			this.obsInfo = new ObsInfo();
			this.isInitialized = true;
		}
	}
	
	/**
	 * This function calculates the Julian centuries based on the current 
	 * observation date/time. The empty AstroDate constructor defaults to 
	 * epoch J2000.0
	 * @return : The Julian centuries for the current observation date/time.
	 */
	private double getJulianCenturies() {
		double daysSinceEpoch = this.obsDate.jd() - new AstroDate().jd();
		return daysSinceEpoch / Astro.TO_CENTURIES;
	}
	
	/**
	 * This function sets the latitude and longitude for an observing site. 
	 * This is used for some of the calculations.
	 * @param lat : The observing site's latitude in decimal degrees.
	 * @param lon : The observing site's longitude in decimal degrees.
	 */
	public void setObservationInfo(double lat, double lon) {
		this.obsInfo.setLatitudeDeg(lat);
		this.obsInfo.setLongitudeDeg(lon);
	}
	
	/**
	 * This function gets the age of the Moon in days and gives back a string 
	 * containing two decimal places.
	 * @return : A string representing the Moon's age.
	 */
	public String age() {
		double currentAge = LunarCalc.ageOfMoonInDays(this.obsDate.jd());
		return StrFormat.formatDouble(currentAge, 2);
	}
	
	/**
	 * This function gets the illuminated fraction of the Moon's surface and 
	 * gives that as a percentage in a string.
	 * @return : A string containing the percentage of the illuminated Moon surface.
	 */
	public String illumation() {
		double illum = 0.0;
		try {
			illum = this.lunar.illuminatedFraction();
		}
		catch (NoInitException nie) {
			Log.e(TAG, "Lunar object is not initialized for calculating illumination.");
		}
		return StrFormat.formatDouble(illum * 100.0, 1) + "%";
	}
}
