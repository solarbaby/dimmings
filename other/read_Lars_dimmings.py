# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:05:09 2016

@author: alyshareinard
"""

import sys
sys.path.append('../common/')
from scipy.io.idl import readsav
import os
from datetime import datetime, timezone
from sunpy_time import parse_time

def read_Lars_dimmings():
 #   rootdir=os.getcwd()+"/Lars dimmings/Example_dimmings/"  
#    print("root first", rootdir)
    
#    print("root", rootdir)
  #  dim_num=[]
    area_mm_total=[]
    thresh=[]
    time=[]
    east_coos=[]
    west_coos=[]
    north_coos=[]
    south_coos=[]
    bad_files=[]
    if os.sep=="/":
        osdir=os.path.join("/Users", "alyshareinard", "Dropbox", "Work")
    else:
        osdir=os.path.join("C:"+os.sep+"Users", "alysha.reinard", "Documents")

    rootdir=os.path.join(osdir, "data", "Lars dimmings", "Example_dimmings")+os.sep
    print("fulldir", rootdir)

    try:
        eventdirs=os.listdir(rootdir)
    except:
        print("Nothing found")
        eventdirs=[]
    print(eventdirs)
        
    for eachdir in eventdirs:
#        print("eachdir", eachdir)
    
#        print(rootdir+eachdir+"/SAV/")
        if eachdir!=".DS_Store":
            time_through=0
            got_time=0
            print("eachdir", eachdir)
            try:
#                print('separator looks like', os.sep)
                full_dir=os.path.join(rootdir+eachdir, "SAV")+os.sep
                print("dir", full_dir)
                files=os.listdir(rootdir+eachdir+os.sep+"SAV"+os.sep)
#                print("files", files)
            except:
                files=[]
            for file in files:
#                print(file)
                if file.startswith("contdim") and got_time==0:
                    data=readsav(rootdir+eachdir+"/SAV/"+file) #contains firstbox_time, curr_euvtime, curr_magtime, doi, area_px, contour_x_coos, contour_y_coos, box_coos, euvfile and magfile

#                    print("reading file", file)
#                    print("time val?", data['dimstr_cont'].firstbox_time[0])
                    time_val=parse_time(data['dimstr_cont'].firstbox_time[0], timezone.utc)
    #                print("time val is", time_val, data['dimstr_cont'].firstbox_time)
     #               got_time=1
                if file.startswith("coordinates") and file.endswith(".sav"):
    
    #                    print("time_through", time_through)
                    filepath=rootdir+eachdir+"/SAV"+os.sep+file
#                    print("reading", file) 
                    data = readsav(filepath) #contains instrument, time, time_mag, dim_num, thresh, area_mm, area_px_total, area_mm_total, contour_length_pix, contour_x_coos, contour_y_coos, contour_x_coos_tot, countour_y_coos_tot, map_sizex, map_sizey, east_coos, west_coos, north_coos, south_coos
#                    print(data)
    #                    print("east from file", data['dimstr3'].east_coos)
    #                print("len", len(data['dimstr3'].east_coos[0]))
    #                if len(data['dimstr3'].east_coos[0])>1:
    #                    bad_files.append(filepath)
    #                    print('bad file', filepath)
    
                    if time_through==0:
    
    #                    print("starting new directory")
    #                        print(data['dimstr3'].time[0])
                        #time_val=data['dimstr3'].time[0]
    #                    dim=data['dimstr3'].dim_num[0]
                        thr=data['dimstr3'].thresh[0]
                        area=sum(data['dimstr3'].area_mm_total[0])
                        east=min(data['dimstr3'].east_coos[0])
                        west=max(data['dimstr3'].west_coos[0])
                        north=max(data['dimstr3'].north_coos[0])
                        south=min(data['dimstr3'].south_coos[0])
                        time_val=parse_time(data['dimstr3'].time, time_format="utime")
    #                    print(time_val, data['dimstr3'].time)
                        time_through=1
                    else:
    #                    print("time", data['dimstr3'].time)
    #                    print("continuing in this directory")
     #                   if dim !=data['dimstr3'].dim_num[0]:
     #                       print("DIM!", dim[0], data['dimstr3'].dim_num[0])
                        if thr !=data['dimstr3'].thresh[0]:
                            print("THRESH!", thresh, data)
                        if area<sum(data['dimstr3'].area_mm_total[0]):
                            area=sum(data['dimstr3'].area_mm_total[0])
                            #time_val=parse_time(data['dimstr3'].time, time_format="utime")
                            #print(time_val, data['dimstr3'].time)
    
    #                    print("north", north)
    #                    print("new north", data['dimstr3'].north_coos[0])
    #                    print("south", south)
    #                    print("new south", data['dimstr3'].south_coos[0])
#    
#                        if east>min(data['dimstr3'].east_coos[0]):
#    #                        print("east is smaller", east, data['dimstr3'].east_coos[0])
#                            east=min(data['dimstr3'].east_coos[0])
#                            
#                        if west<max(data['dimstr3'].west_coos[0]):
#    #                        print("west change", west, data['dimstr3'].west_coos[0])
#                            west=max(data['dimstr3'].west_coos[0])
#    
#    
#                        if south>min(data['dimstr3'].south_coos[0]):
#    #                        print("south change", south, data['dimstr3'].south_coos[0])
#                            south=min(data['dimstr3'].south_coos[0])
#                            
#                        if north<max(data['dimstr3'].north_coos[0]):
#    #                        print("north is smaller", north, data['dimstr3'].north_coos[0])
#                            north=max(data['dimstr3'].north_coos[0])
#                            
    #                        print("area", data['dimstr3'].area_mm_total)
    #                        print("east", data['dimstr3'].east_coos, east)   
    #                        print("west", data['dimstr3'].west_coos, west)
    #                        print("north", data['dimstr3'].north_coos, north)
    #                        print("south", data['dimstr3'].south_coos, south)
        try:                
            area_mm_total.append(area)
            east_coos.append(east)
            west_coos.append(west)
            north_coos.append(north)
            south_coos.append(south)
            time.append(time_val)
        except:
            print("no data for directory", eachdir)
                

#    print("area", area_mm_total)
#    print("east", east_coos)
#    print("west", west_coos)
#    print("north", north_coos)
#    print("south", south_coos)
#    for i in range(len(area_mm_total)):
#        print("time", time[i], "area: ", area_mm_total[i], "east: ", east_coos[i], "west: ", west_coos[i], "north: ", north_coos[i], "south: ", south_coos[i])

    mean_EW=[(x+y)/2 for x,y in zip(east_coos, west_coos)]
    mean_NS=[(x+y)/2 for x,y in zip(north_coos, south_coos)]
   
    
    dimmings={'time':time, 'area':area_mm_total, 'eastedge':east_coos, \
    'westedge':west_coos, 'northedge':north_coos, 'southedge':south_coos, \
    'mean_EW':mean_EW, 'mean_NS':mean_NS}
    print("in routine", type(dimmings))
    return dimmings

read_Lars_dimmings()