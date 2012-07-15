package com.typeiisoft.lct.features;

/**
 * This class is responsible for containing the relevant information for 
 * a given lunar feature.
 * 
 * @author Michael Reuter
 *
 */
public class LunarFeature {
	/** Clean name of the lunar feature (no dicritical marks). */
	private String name;
	/** Latitude of the lunar feature in decimal degrees. North is positive. */
	private double latitude;
	/** Longitude of the lunar feature in decimal degrees. East is positive. */
	private double longitude;
	/** Short description of feature type. */
	private String featureType;
	/** Width of the lunar feature in latitude in decimal degrees. */
	private double deltaLatitude;
	/** Width of the lunar feature in longitude in decimal degrees. */
	private double deltaLongitude;
	/** Target type name for Lunar Club */
	private String codeName;
	/** Observing club lunar feature belongs to. */
	private String clubType;
	
	/**
	 * Parametered class constructor.
	 * @param name : clean name of feature
	 * @param latitude : latitude of feature
	 * @param longitude : longitude of feature
	 * @param featureType : description of feature
	 * @param deltaLatitude : latitude width of feature
	 * @param deltaLongitude : longitude width of feature
	 * @param codeName : Lunar Club target type
	 * @param clubType : club list for feature
	 */
	public LunarFeature(String name, double latitude, double longitude,
			String featureType, double deltaLatitude, double deltaLongitude,
			String codeName, String clubType) {
		this.name = name;
		this.latitude = latitude;
		this.longitude = longitude;
		this.featureType = featureType;
		this.deltaLatitude = deltaLatitude;
		this.deltaLongitude = deltaLongitude;
		this.codeName = codeName;
		this.clubType = clubType;
	}
	
	/**
	 * Getter for feature name
	 * @return : the clean lunar feature name
	 */
	public String getName() {
		return this.name;
	}
	
	/**
	 * Getter for feature latitude
	 * @return : the feature latitude
	 */
	public double getLatitude() {
		return this.latitude;
	}
	
	/**
	 * Getter for feature longitude
	 * @return : the feature longitude
	 */
	public double getLongitude() {
		return this.longitude;
	}
	
	/**
	 * Getter for the feature type name
	 * @return : the feature type name
	 */
	public String getFeatureType() {
		return this.featureType;
	}
	
	/**
	 * Getter for the feature latitude width
	 * @return : the feature latitude width
	 */
	public double getDeltaLatitude() {
		return this.deltaLatitude;
	}
	
	/**
	 * Getter for the feature longitude width
	 * @return : the feature longitude width
	 */
	public double getDeltaLongitude() {
		return this.deltaLongitude;
	}
	
	/**
	 * Getter for the Lunar Club target type name. Can be None.
	 * @return : the Lunar Club target type name
	 */
	public String getCodeName() {
		return this.codeName;
	}
	
	/**
	 * Getter for the observing club list name. Can be Lunar, LunarII or Both
	 * @return : the observing cub list name
	 */
	public String getClubType() {
		return this.clubType;
	}
}
