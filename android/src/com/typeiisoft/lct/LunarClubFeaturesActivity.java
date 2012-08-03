package com.typeiisoft.lct;

import java.util.ArrayList;

import com.typeiisoft.lct.db.DataBaseHelper;
import com.typeiisoft.lct.features.LcFeatureAdapter;
import com.typeiisoft.lct.features.LunarFeature;

import android.app.ExpandableListActivity;
import android.app.ListActivity;
import android.os.Bundle;

public class LunarClubFeaturesActivity extends ExpandableListActivity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
        setContentView(R.layout.lcfeatures);
        DataBaseHelper moonDB = new DataBaseHelper(this);
        
        ArrayList<String> categories = new ArrayList<String>();
        categories.add(new String("Naked Eye"));
        categories.add(new String("Binocular"));
        categories.add(new String("Telescopic"));
        
        LcFeatureAdapter adapter = new LcFeatureAdapter(this, categories,
        		moonDB.getLunarClubFeatures());
        setListAdapter(adapter);
	}
}
