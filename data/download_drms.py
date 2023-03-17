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
    print(f"Data export query:\n  {query_string}\n")
    request = client.export(query_string, method=method, protocol=protocol)
    print(f"\nRequest URL: {request.request_url}")
    print(f"{int(len(request.urls))} file(s) available for download.\n")
    return request

def export_exist_id(client, request_id):
    return client.export_from_id(request_id)

def download_request(request, out_dir):
    request.download(out_dir)
    print("Download finished.")
    print(f'\nDownload directory:\n  "{(out_dir)}"\n')


if __name__ == "__main__" :


    jsoc_email = "eunsupark@kasi.re.kr"
    out_dir = "/Users/eunsu/download"
    client = connect_client(jsoc_email)

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