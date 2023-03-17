import drms
import datetime


def connect_client(jsoc_email):
    return drms.Client(email=jsoc_email, verbose=True)

def make_date(year, month, day, hour, minute=0, second=0, days=None, cadence=None):
    date = "%04d.%02d.%02d_%02d:%02d:%02d_TAI" % (year, month, day, hour, minute, second)
    if days is not None and cadence is not None :
        date = "%s/%s@%s" % (date, days, cadence)
    return date

def export(client, query_string, method="url", protocol="fits"):
    request = client.export(query_string, method=method, protocol=protocol)
    return request

def export_exist_id(client, request_id):
    return client.export_from_id(request_id)

def download_request(request, out_dir):
    request.download(out_dir)


if __name__ == "__main__" :


    jsoc_email = "eunsupark@kasi.re.kr"
    out_dir = "/Users/eunsu/download"
    client = connect_client(jsoc_email)


    # query_string = "hmi.sharp_720s[4864][2014.11.30_00:00:00_TAI/1d@8h]{continuum, magnetogram, field}"
    # print(f"Data export query:\n  {query_string}\n")
    # export_protocol = "fits"
    # result = client.export(query_string, method="url", protocol=export_protocol)

    # # Print request URL.
    # print(f"\nRequest URL: {result.request_url}")
    # print(f"{int(len(result.urls))} file(s) available for download.\n")

    # # Download selected files.
    # result.download(out_dir)
    # print("Download finished.")
    # print(f'\nDownload directory:\n  "{(out_dir)}"\n')



    year, month, day, hour, minute, second = 2017, 9, 6, 8, 36, 0
    days, cadence = "1d", "8h"
    date = make_date(year=year, month=month, day=day, hour=hour, minute=minute, second=second, days=days, cadence=cadence)

    series, segments = "hmi.B_720s", "{inclination,azimuth,disambig,field}"
    query_string = "%s[%s]%s" % (series, date, segments)
    print(query_string)
    # request = export(client, query_string)
    # print(request)
    # download_request(request, out_dir)



    year, month, day, hour, minute, second = 2017, 9, 6, 8, 36, 0
    date = make_date(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    series, segments = "hmi.sharp_cea_720s", "{Bp,Br,Bt,Bp_err,Br_err,Bt_err}"
    noaa_num = [12673]
    harp_num = 7115
    query_string = "%s[%d][%s]%s" % (series, harp_num, date, segments)
    print(query_string)
    # request = export(client, query_string)
    # print(request)
    # download_request(request, out_dir)





# def get_request(my_key, year, month, day, days, cadence, out_dir):
#     query_string = '%s[%04d.%02d.%02d_00:00_TAI/%dd@%dd]{inclination, azimuth, disambig, field}' % (my_key, year, month, day, days, cadence)
#     export_request = client.export(query_string, method='url', protocol='fits')
#     export_request.wait()
#     export_request.download(out_dir)

# def download_exist_request(request_id, out_dir):
#     export_request = client.export_from_id(request_id)
#     export_request.download(out_dir)

# if __name__ == "__main__" :
    #get_request(my_key, 2014, 1, 1, 365, 1, out_dir)
 
#     request_id = "JSOC_20230316_410"
#     export_request = client.export_from_id(request_id)
#     export_request.download(out_dir)


#     for idx in range(680, 1440):
#         export_request.download(out_dir, method="url", idx)
# #    export_request.download(out_dir, 680)


# #    download_exist_request(request_id, out_dir)





# jsoc_email = "eunsupark@kasi.re.kr"#os.environ["JSOC_EMAIL"]
# my_key = "hmi.B_720s"
# #out_dir = './B_720s'
# out_dir = './SHARP_720s'


# client = drms.Client(email=jsoc_email, verbose=True)
# print(client)
# export_request = client.export("hmi.sharp_720s[2011.1.1_TAI/1@1d]{inclination,azimuth,disambig,field}")
# #export_request = client.export("hmi.B_720s[2011.1.1_TAI/1@1d]{inclination,azimuth,disambig,field}")
# print(export_request)
# print(export_request.data.filename)
# nb = len(export_request.data)



#export_request.download(out_dir)
#def run_down(n):
#    export_request.download(out_dir, n)


#if __name__ == "__main__" :

#    freeze_support()

#    pool = Pool(4)
#    pool.map(run_down, range(nb))
#    pool.close()



#pkeys = client.pkeys(my_key)
#print(pkeys)

#series_info = client.info(my_key)
#print(series_info.segments)

# query = client.query("hmi.B_720s[2011.01.01_TAI/1d@1d]", key="T_REC")
# print(query)

