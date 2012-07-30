package com.typeiisoft.lct.utils;

import java.util.Calendar;
import android.util.Log;

import com.mhuss.AstroLib.Astro;
import com.mhuss.AstroLib.AstroDate;
import com.mhuss.AstroLib.Lunar;
import com.mhuss.AstroLib.LunarCalc;
import com.mhuss.AstroLib.NoInitException;
import com.mhuss.AstroLib.ObsInfo;
import com.typeiisoft.lct.features.LunarFeature;

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
	
	private enum Phase {
		NM, WAXING_CRESENT, FQ, WAXING_GIBBOUS, FM, WANING_GIBBOUS, TQ,
		WANING_CRESENT;
	}
	
	private String[] phaseNames = {"New Moon", "Waxing Cresent", 
			"First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous",
			"Third Quarter", "Waning Cresent"};
	
	private enum TimeOfDay {
		MORNING, EVENING;
	}
	
	private static final double FEATURE_CUTOFF = 15D;
	
	private String[] noCutoffType = {"Mare", "Oceanus"};
	
	/**
	 * This function is the class constructor.
	 */
	public MoonInfo() {
		if (!this.isInitialized) {
			Calendar now = Calendar.getInstance();
			this.obsDate = new AstroDate(now.get(Calendar.DATE), 
					now.get(Calendar.MONTH)+1, now.get(Calendar.YEAR), 
					now.get(Calendar.HOUR_OF_DAY), now.get(Calendar.MINUTE), 
					now.get(Calendar.SECOND));
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
		return StrFormat.formatDouble(currentAge, 2) + " days";
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
	
	/**
	 * This function returns the currently held observation date and time 
	 * as separate strings.
	 * @return : A date string and a time string.
	 */
	public String[] obsDateTime() {
		return this.obsDate.toStringTZ().split(" ", 2);
	}
	
	/**
	 * This function returns the selenographic colongitude for the current 
	 * date and time.
	 * @return : The selenographic colongitude as a DMS string.
	 */
	public String colong() {
		double colong = LunarCalc.selenographicColongitude(this.getJulianCenturies());
		Log.i(TAG, "Colongitude calculated = " + Double.toString(colong));
		return StrFormat.dmsFromDd(colong, false);
	}
	
	/**
	 * This function returns the phase of the Moon as a string.
	 * @return : The Moon phase as a string.
	 */
	public String phase() {
		return this.phaseNames[this.getPhase().ordinal()];
	}
	
	/**
	 * This function determines if the given lunar feature is visible based 
     * on the current selenographic colongitude (SELCO). For most features 
     * near the equator, from NM to FM once the SELCO recedes about 15 
     * degrees, the shadow relief makes it tough to observe. Conversely, the 
     * SELCO needs to be within 15 degrees of the feature from FM to NM. 
     * Features closer to the poles are visible much longer after the 15 
     * degree cutoff. A 1/cos(latitude) will be applied to the cutoff. 
     * Mare and Oceanus are special exceptions and once FULLY visible they are 
     * always visible.
	 * @param feature : The lunar feature to check for visibility.
	 * @return : True is the feature is visible.
	 */
	public boolean isVisible(LunarFeature feature) {
		double selcoLong = this.colongToLong();
		int curTod = this.getTimeOfDay().ordinal();
		
		double minLon = feature.getLongitude() - feature.getDeltaLongitude() / 2.0;
		double maxLon = feature.getLongitude() + feature.getDeltaLongitude() / 2.0;
		
		// Switch things around
		if (minLon > maxLon) {
			double temp = minLon;
			minLon = maxLon;
			maxLon = temp;
		}
		
		boolean isVisible = false;
		double latitudeScaling = Math.cos(Math.toRadians(feature.getLatitude()));
		double cutoff = MoonInfo.FEATURE_CUTOFF / latitudeScaling;
		
		double lonCutoff = 0.0;
		if (TimeOfDay.MORNING.ordinal() == curTod) {
			// Minimum longitude for morning visibility
			lonCutoff = minLon - cutoff;
			if (this.noCutoffFeature(feature.getFeatureType())) {
				isVisible = selcoLong <= minLon;
			}
			else {
				isVisible = (selcoLong >= lonCutoff || selcoLong <= minLon);
			}
		}
		if (TimeOfDay.EVENING.ordinal() == curTod) {
			// Maximum longitude for evening visibility
			lonCutoff = maxLon + cutoff;
			if (this.noCutoffFeature(feature.getFeatureType())) {
				isVisible = maxLon <= selcoLong;
			}
			else {
				isVisible = (selcoLong >= maxLon || selcoLong <= lonCutoff);
			}
		}
		
		return isVisible;
	}
	
	/**
	 * This function checks a given lunar feature type against the list of lunar 
	 * feature types that have no cutoff.
	 * @param type : The string containing the lunar feature type.
	 * @return : True is the incoming feature type is in no cutoff list.
	 */
	private boolean noCutoffFeature(String type) {
		for (String s : this.noCutoffType) {
			if (s.toLowerCase() == type.toLowerCase()) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * This function returns the moon phase according to standard nomenclature.
	 * @return : The moon phase as an enum value.
	 */
	private Phase getPhase() {
		double colong = LunarCalc.selenographicColongitude(this.getJulianCenturies());
		if (270.0 == colong) {
			return Phase.NM;
		}
		else if (colong > 270.0 && colong < 360.0) {
			return Phase.WAXING_CRESENT;
		}
		else if (0.0 == colong || 360.0 == colong) {
			return Phase.FQ;
		}
		else if (colong > 0.0 && colong < 90.0) {
			return Phase.WAXING_GIBBOUS;
		}
		else if (90.0 == colong) {
			return Phase.FM;
		}
		else if (colong > 90.0 && colong < 180.0) {
			return Phase.WANING_GIBBOUS;
		}
		else if (180.0 == colong) {
			return Phase.TQ;
		}
		else if (colong > 180.0 && colong < 270.0) {
			return Phase.WANING_CRESENT;
		}
		else {
			return Phase.NM;
		}
	}
	
	/**
	 * This function determines the current time of day on the moon. In 
     * otherwords, if the sun is rising on the moon it is morning or if the 
     * sun is setting on the moon it is evening.
	 * @return : The current time of day.
	 */
	private TimeOfDay getTimeOfDay() {
		int phase = this.getPhase().ordinal();
		if (phase >= Phase.NM.ordinal() && 
				phase <= Phase.WAXING_GIBBOUS.ordinal()) {
			return TimeOfDay.MORNING;
		}
		else {
			return TimeOfDay.EVENING;
		}
	}
	
	/**
	 * This function calculates the conversion between the selenographic  
     * colongitude and actual lunar longitude.
	 * @return : The lunar longitude for the current selenographic colongitude.
	 */
	private double colongToLong() {
		double colong = LunarCalc.selenographicColongitude(this.getJulianCenturies());
		int phase = this.getPhase().ordinal();
		if (Phase.NM.ordinal() == phase || Phase.WAXING_CRESENT.ordinal() == phase) {
			return 360.0 - colong;
		}
		else if (Phase.FQ.ordinal() == phase || Phase.WAXING_GIBBOUS.ordinal() == phase) {
			return -1.0 * colong;
		}
		else if (Phase.FM.ordinal() == phase || Phase.WANING_GIBBOUS.ordinal() == phase) {
			return 180.0 - colong;
		}
		else {
			return -1.0 * (colong - 180.0);
		}
	}
}
