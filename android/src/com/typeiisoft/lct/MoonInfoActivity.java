package com.typeiisoft.lct;

import com.typeiisoft.lct.utils.MoonInfo;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MoonInfoActivity extends Activity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mooninfo);
		
		MoonInfo moonInfo = new MoonInfo();
		String[] dateTime = moonInfo.obsDateTime();
		this.appendText(R.id.obsdate_label, dateTime[0]);
		this.appendText(R.id.obstime_label, dateTime[1]);
		this.appendText(R.id.moon_age_label, moonInfo.age());
		this.appendText(R.id.moon_illum_label, moonInfo.illumation());
	}
	
	/**
	 * This function handles appending text to the labels that are already 
	 * displayed on the layout.
	 * @param layoutResId
	 * @param more_text
	 */
	private void appendText(int layoutResId, String more_text) {
		TextView tv = (TextView) this.findViewById(layoutResId);
		String cur_text = tv.getText().toString();
		StringBuffer buff = new StringBuffer(cur_text).append(" ").append(more_text);
		tv.setText(buff);
	}
}
