package com.typeiisoft.lct;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MoonInfoActivity extends Activity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

        TextView textview = new TextView(this);
        textview.setText("This is the Moon Info tab");
        setContentView(textview);
	}
}
