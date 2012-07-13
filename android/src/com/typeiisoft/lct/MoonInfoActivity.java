package com.typeiisoft.lct;

import java.util.GregorianCalendar;

import android.app.Activity;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.widget.TextView;

public class MoonInfoActivity extends Activity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mooninfo);
		
		String now = DateFormat.format("yyyy/MM/dd hh:mm:ss", 
				new GregorianCalendar()).toString();
		
		this.appendText(R.id.obsdate_label, now.split(" ")[0]);
		this.appendText(R.id.obstime_label, now.split(" ")[1]);
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
