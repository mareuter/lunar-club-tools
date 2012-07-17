package com.typeiisoft.lct;

import java.util.ArrayList;

import com.typeiisoft.lct.db.DataBaseHelper;
import com.typeiisoft.lct.features.L2FeatureAdapter;
import com.typeiisoft.lct.features.LunarFeature;

import android.app.ListActivity;
import android.os.Bundle;

public class LunarTwoFeaturesActivity extends ListActivity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
        setContentView(R.layout.l2features);
        DataBaseHelper moonDB = new DataBaseHelper(this);
        L2FeatureAdapter adapter = new L2FeatureAdapter(this, 
        		(ArrayList<LunarFeature>) moonDB.getLunarTwoFeatures());
        setListAdapter(adapter);
	}
}
