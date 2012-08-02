package com.typeiisoft.lct.features;

import java.util.Comparator;

/**
 * This class is responsible for the sorting criteria for the Lunar II feature 
 * list.
 * 
 * @author Michael Reuter
 *
 */
public class L2Comparator implements Comparator<LunarFeature> {

	@Override
	public int compare(LunarFeature arg0, LunarFeature arg1) {
		int value = arg0.getFeatureType().compareTo(arg1.getFeatureType());
		if (0 != value) {
			return value;
		}
		else {
			return Double.compare(arg0.getLatitude(), arg1.getLatitude());
		}
	}

}
