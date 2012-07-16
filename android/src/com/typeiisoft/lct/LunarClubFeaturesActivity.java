package com.typeiisoft.lct;

import java.util.ArrayList;

import com.typeiisoft.lct.db.DataBaseHelper;
import com.typeiisoft.lct.features.LcFeatureAdapter;
import com.typeiisoft.lct.features.LunarFeature;

import android.app.ListActivity;
import android.os.Bundle;

public class LunarClubFeaturesActivity extends ListActivity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
        setContentView(R.layout.lcfeatures);
        DataBaseHelper moonDB = new DataBaseHelper(this);
        LcFeatureAdapter adapter = new LcFeatureAdapter(this, 
        		(ArrayList<LunarFeature>) moonDB.getLunarClubFeatures());
        setListAdapter(adapter);
	}
}
