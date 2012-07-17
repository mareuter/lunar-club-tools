package com.typeiisoft.lct;

import java.util.ArrayList;

import com.typeiisoft.lct.db.DataBaseHelper;
import com.typeiisoft.lct.features.L2FeatureAdapter;
import com.typeiisoft.lct.features.LunarFeature;

import android.app.ListActivity;
import android.os.Bundle;
import android.util.Log;

public class LunarTwoFeaturesActivity extends ListActivity {
	private final static String TAG = "LunarTwoFeaturesActivity";
	
	@Override
	public void onCreate(Bundle savedInstanceState) {
		Log.i(TAG, "Creating tab.");
		super.onCreate(savedInstanceState);
        setContentView(R.layout.l2features);
        DataBaseHelper moonDB = new DataBaseHelper(this);
        L2FeatureAdapter adapter = new L2FeatureAdapter(this, 
        		(ArrayList<LunarFeature>) moonDB.getLunarTwoFeatures());
        setListAdapter(adapter);
	}
}
