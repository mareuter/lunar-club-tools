package com.typeiisoft.lct.features;

import java.util.ArrayList;

import com.typeiisoft.lct.R;
import com.typeiisoft.lct.utils.StrFormat;

import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

public class LcFeatureAdapter extends ArrayAdapter<LunarFeature> {
	private final Context context;
	private final ArrayList<LunarFeature> features;
	private static final String TAG = "LcFeatureAdapter";
	
	public LcFeatureAdapter(Activity context, ArrayList<LunarFeature> values) {
		super(context, R.layout.lcfeatureitem, values);
		this.context = context;
		this.features = values;
	}
	
	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		Log.d(TAG, "RowView for " + this.features.get(position).getName() + " starting.");

		LayoutInflater inflater = (LayoutInflater) context
				.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
		View rowView = inflater.inflate(R.layout.lcfeatureitem, parent, false);
		TextView featureNameView = (TextView) rowView.findViewById(R.id.feature_name);
		featureNameView.setText(this.features.get(position).getName());
		
		TextView featureTypeView = (TextView) rowView.findViewById(R.id.feature_type);
		featureTypeView.setText(this.features.get(position).getFeatureType());
		
		TextView featureTargetView = (TextView) rowView.findViewById(R.id.club_target_type);
		featureTargetView.setText(this.features.get(position).getClubType());
		
		TextView featureLatView = (TextView) rowView.findViewById(R.id.feature_latitude);
		String lat = StrFormat.coordFormat("lat", this.features.get(position).getLatitude());
		featureLatView.setText(lat);
		
		Log.d(TAG, "RowView for " + this.features.get(position).getName() + " done.");
		return rowView;
	}
}
