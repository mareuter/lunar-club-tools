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
import android.widget.BaseExpandableListAdapter;
import android.widget.TextView;

public class LcFeatureAdapter extends BaseExpandableListAdapter {
	private final Context context;
	private final ArrayList<String> headers;
	private final ArrayList<ArrayList<LunarFeature>> features;
	private static final String TAG = "LcFeatureAdapter";
	
	public LcFeatureAdapter(Context context, ArrayList<String> hvals,
			ArrayList<ArrayList<LunarFeature>> values) {
		//super(context, R.layout.lcfeatureitem, values);
		this.context = context;
		this.headers = hvals;
		this.features = values;
	}
	
    // Return a child view. You can load your custom layout here.
    @Override
    public View getChildView(int groupPosition, int childPosition, 
    		boolean isLastChild, View convertView, ViewGroup parent) {
        LunarFeature feature = (LunarFeature) this.getChild(groupPosition, 
        		childPosition);
        if (convertView == null) {
            LayoutInflater infalInflater = (LayoutInflater) this.context
                    .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = infalInflater.inflate(R.layout.lcfeatures_item, null);
        }
        TextView tv = (TextView) convertView.findViewById(R.id.tv_item);
        tv.setText(feature.getName());
        return convertView;
    }

    // Return a group view. You can load your custom layout here.
    @Override
    public View getGroupView(int groupPosition, boolean isExpanded, 
    		View convertView, ViewGroup parent) {
        String header = (String) this.getGroup(groupPosition);
        if (convertView == null) {
            LayoutInflater infalInflater = (LayoutInflater) this.context
                    .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = infalInflater.inflate(R.layout.lcfeatures_group, null);
        }
        TextView tv = (TextView) convertView.findViewById(R.id.tv_group);
        tv.setText(header);
        return convertView;
    }
/*
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
*/
    @Override
    public boolean areAllItemsEnabled()
    {
        return true;
    }

    @Override
    public Object getChild(int groupPosition, int childPosition) {
        return this.features.get(groupPosition).get(childPosition);
    }

    @Override
    public long getChildId(int groupPosition, int childPosition) {
        return childPosition;
    }
    
    @Override
    public int getChildrenCount(int groupPosition) {
        return this.features.get(groupPosition).size();
    }

    @Override
    public Object getGroup(int groupPosition) {
        return this.headers.get(groupPosition);
    }

    @Override
    public int getGroupCount() {
        return this.headers.size();
    }

    @Override
    public long getGroupId(int groupPosition) {
        return groupPosition;
    }

    @Override
    public boolean hasStableIds() {
        return true;
    }

    @Override
    public boolean isChildSelectable(int arg0, int arg1) {
        return true;
    }
}
