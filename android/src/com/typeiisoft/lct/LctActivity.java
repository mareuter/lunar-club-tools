package com.typeiisoft.lct;

import android.app.TabActivity;
import android.content.Intent;
import android.content.res.Resources;
import android.graphics.drawable.StateListDrawable;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.TabHost;

public class LctActivity extends TabActivity {
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        Resources res = getResources(); // Resource object to get Drawables
        TabHost tabHost = getTabHost();  // The activity TabHost
        TabHost.TabSpec spec;  // Reusable TabSpec for each tab
        Intent intent;  // Reusable Intent for each tab

        // Create an Intent to launch an Activity for the tab (to be reused)
        intent = new Intent().setClass(this, MoonInfoActivity.class);

        // Initialize a TabSpec for each tab and add it to the TabHost
        spec = tabHost.newTabSpec("mooninfo").setIndicator("Moon Info",
                          new StateListDrawable())
                      .setContent(intent);
        tabHost.addTab(spec);

        // Do the same for the other tabs
        intent = new Intent().setClass(this, LunarClubFeaturesActivity.class);
        spec = tabHost.newTabSpec("lunar_club_features").setIndicator("LC Features",
                          new StateListDrawable())
                      .setContent(intent);
        tabHost.addTab(spec);
        
        intent = new Intent().setClass(this, LunarTwoFeaturesActivity.class);
        spec = tabHost.newTabSpec("lunar_two_features").setIndicator("LII Features",
                          new StateListDrawable())
                      .setContent(intent);
        tabHost.addTab(spec);

        tabHost.setCurrentTab(0);
    }
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
    	super.onCreateOptionsMenu(menu);
    	MenuInflater inflater = getMenuInflater();
    	inflater.inflate(R.menu.menu, menu);
    	return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
    	switch (item.getItemId()) {
    	case R.id.about:
    		startActivity(new Intent(this, About.class));
    		return true;
    	}
    	return false;
    }
}