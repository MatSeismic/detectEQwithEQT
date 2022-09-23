from obspy.clients.fdsn import Client
from EQTransformer.core.predictor import predictor
import tensorflow as tf
import os
from EQTransformer.utils.downloader import makeStationList
from EQTransformer.utils.downloader import downloadMseeds

date_string="100601base"
json_basepath = os.path.join(os.getcwd(),"json/station_list"+date_string+".json")
start_time="2010-06-01 00:00:00.00"
end_time="2010-06-11 00:00:00.00"
detection_threshold=0.05
p_threshold=0.05
s_threshold=0.05
number_of_plots=300

print("making station list...")
print("="*60)
makeStationList(json_path=json_basepath, client_list=["IRIS"],
     min_lat=43.0, max_lat=46.0, min_lon=-110, max_lon=-101, start_time=start_time,
     end_time=end_time, channel_list=[ "BH[ZNE]"],
     filter_network=["SY", "WY", "MB", "Z2", "IU", "US", "TA", "ZH", "ZI"], filter_station=[])

client_2f = Client('IRIS', user="zhu00064@umn.edu", password="DaxXmgn3kJ4G", timeout=240)


print("downloading mseeds...")
print("="*60)
downloadMseeds(client_list=[client_2f], stations_json=json_basepath,
    output_dir="downloads_mseeds"+date_string,
    min_lat=43.0, max_lat=46.0, min_lon=-110, max_lon=-101,
    start_time=start_time, end_time=end_time, chunk_size=1,
    channel_list=["BH[ZNE]"], n_processor=None)

from EQTransformer.utils.hdf5_maker import preprocessor
preprocessor(preproc_dir="preproc"+date_string,
    mseed_dir="downloads_mseeds"+date_string, stations_json=json_basepath,
    overlap=0.1, n_processor=None)

print("making predictions...")
print("="*60)
predictor(input_dir= "./downloads_mseeds"+ date_string +"_processed_hdfs",
    input_model='./EQTransformer/ModelsAndSampleData/EqT_model_conservative.h5',
    output_dir="detections"+date_string,
    detection_threshold=detection_threshold, P_threshold=p_threshold,
    S_threshold=s_threshold, number_of_plots=number_of_plots,
    plot_mode='time')
