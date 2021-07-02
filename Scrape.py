from googlesearch import search
from htmldate import find_date
import pandas as pd
import numpy as np

# to search
query = ['Tuskegee,AL', 'West Kentucky Cooperative', 'ACE Power,MS', 'Albertville,AL', 'Benson,NC', 'Benton County,TN', 'Blakely,GA', 'Blue Ridge Mountain,GA', 'Bolivar,TN', 'Caney Fork EC,TN', 'Cleveland Utilities,TN', 'Clinton,TN', 'Columbia Power and Water,TN', 'Cowlitz PUD,WA', 'Denton,TX', 'Dickson Electric,TN', 'Dixie EC,AL', 'Dothan,AL', 'Douglas,GA', 'Franklin EPB,KY', 'Fulton,KY', 'Glasgow EPB,KY', 'Guntersville,AL', 'Holly Springs,MS', 'Hopkinsville,KY', 'Humboldt Utilities,TN', 'JEA,FL', 'Kansas City BPU,KS', 'La Grange,NC', 'Lake Worth Beach,FL', 'Lenoir City,TN', 'Lexington Electric,TN', 'MLGW,TN', 'Marshall-DeKalb EC,AL', 'Mayfield,KY', 'Midstate,OR', 'Mt Pleasant,TN', 'New Bern,NC', 'Ocala,FL', 'Orlando,FL', 'Pickwick EC,TN', 'Ripley Power and Light,TN', 'Rockwood,TN', 'Rush Shelby,IN', 'Russellville EPB,KY', 'Scottsboro EPB,AL', 'Selma,NC', 'Shelbyville,TN', 'Southwest TN,TN', 'St Croix EC,WI', 'TVEC,TN', 'Tarrant Electric,AL', 'Tombigbee EPA,MS', 'Tri-State,GA', 'Union City,TN', 'Wilson Internet,NC', 'Wilson,NC']
utility_links = ['https://www.yourubt.com/', 'https://wkrecc.com/index.php/18-billing', 'https://ace-power.com/account/payment-options/', 'http://www.mub-albertville.com/', 'https://www.townofbenson.com/2191/Bill-Payment', 'http://www.bcestn.org/index.php/manage-existing-service/pay-my-monthly-bill/106-pay-by-phone-or-online', 'https://cityofblakely.net/pay-online/', 'https://www.cityofblueridgega.gov/WastewaterandWater.aspx', 'https://www.bolivarutility.com/', 'https://www.caneyforkec.com', 'http://www.clevelandutilities.com/', 'http://www.clintonutilities.com/pmtopts.html', 'https://cpws.com/my-account/', 'https://www.cowlitzpud.org/customer-services/pay-my-bill/', 'https://www.cityofdenton.com/en-us/pay-my-bill', 'https://dicksonelectric.com/', 'https://www.dixie.coop/online-account-access', 'https://www.dothan.org/175/Pay-View-Utility-Bill-Online', 'https://www.cityofdouglasga.gov/84/Make-a-Utility-Payment', 'http://www.franklinepb.com/bill-payment-options', 'https://www.fulton-ky.com/frequently-asked-questions/', 'http://www.glasgowepb.net/?page_id=343', 'https://guntersvilleal.org/departments/utilites/', 'http://www.hsutilities.com/', 'https://hop-electric.com/electric/residential-electric/bill-payment-options/', 'https://www.humboldtutilities.com/', 'https://www.jea.com/my_account/billing_and_payment_options/', 'https://www.bpu.com/', 'https://lagrangenc.com/703/Online-Billing', 'https://lakeworthbeachfl.gov/payment-portal/', 'https://www.lcub.com/', 'https://www.lexingtontn.gov/pay_online.html', 'https://www.mlgw.com/residential/payingyourbill_b', 'https://mdec.org/', 'https://www.mayfieldews.com/index.php/electric/smartpay', 'https://midstateelectric.coop/payment-options', 'https://www.mtpleasant-tn.gov/utility-payments', 'https://www.newbernnc.gov/departments/administration/finance/utilities_business_office/pay_my_bill.php', 'https://www.ocalafl.org/government/city-departments-a-h/customer-service-office/pay-my-bill', 'https://www.orangecountyfl.net/WaterGarbageRecycling/BillPaymentOptions.aspx', 'http://www.pickwickec.com/bill-payment-information/', 'https://ripleypower.com/account/payment-options.php', 'https://cityofrockwood.com/online-bill-pay', 'https://www.rse.coop/', 'https://www.epbnet.com/index.php/support/bill-pay/', 'https://www.sepb.net/payment-2/bill-pay/', 'https://selma-nc.com/departments/customer-service/', 'http://www.shelbyvillepower.com/', 'https://www.stemc.com/my-payment-options', 'https://www.scecnet.net/content/pay-my-bill', 'https://www.tvec.com/index.asp?fullsite=1', 'https://www.needhelppayingbills.com/html/tarrant_county_assistance_prog.html', 'https://www.tombigbeeelectric.com/payments', 'https://www.tsemc.net/my-account/pay-bill-online/', 'http://unioncitytn.gov/pay-online.html', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options']
gov_links = ['https://www.cityofalbertville.com/', 'https://www.townofbenson.com/', 'https://www.bentoncountytn.gov/', 'https://cityofblakely.net/', 'https://www.cityofblueridgega.gov/', 'https://www.cityofbolivar.com/', 'https://www.caneyforkec.com', 'http://www.clevelandutilities.com/', 'http://www.clintontn.net/', 'https://cpws.com/', 'https://www.cowlitzpud.org/', 'https://www.dentoncounty.gov/', 'https://dicksonelectric.com/', 'https://www.dixie.coop/', 'https://www.dothan.org/', 'https://www.cityofdouglasga.gov/', 'http://www.franklinepb.com/', 'https://www.fulton-ky.com/', 'http://www.glasgowepb.net/', 'https://guntersvilleal.org/', 'https://hollyspringsmsus.com/', 'https://www.hopkinsvilleky.us/', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
New_Utility_Links = ['https://www.ci.richland.wa.us/departments/energy-services', 'https://cityofcovington.org/index.php?section=covington_utilities3', 'http://unioncitytn.gov/pay-online.html', 'https://dicksonelectric.com/', 'https://www.jea.com/my_account/billing_and_payment_options/', 'https://www.mtpleasant-tn.gov/utility-payments', 'https://www.sepb.net/payment-2/bill-pay/', 'https://www.fulton-ky.com/frequently-asked-questions/', 'https://www.cityofblueridgega.gov/WastewaterandWater.aspx', 'https://midstateelectric.coop/payment-options', 'https://wkrecc.com/index.php/18-billing', 'https://mdec.org/', 'https://www.mlgw.com/residential/payingyourbill_b', 'https://www.caneyforkec.com/', 'https://www.humboldtutilities.com/', 'http://www.hsutilities.com/', 'https://www.cityofmadison.com/water', 'https://hop-electric.com/electric/residential-electric/bill-payment-options/', 'https://ace-power.com/account/payment-options/', 'https://www.ocalafl.org/government/city-departments-a-h/customer-service-office/pay-my-bill', 'https://www.bolivarutility.com/', 'https://lakeworthbeachfl.gov/payment-portal/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.bpu.com/', 'https://www.cityofdenton.com/en-us/pay-my-bill', 'https://www.stemc.com/my-payment-options', 'https://www.dixie.coop/online-account-access', 'https://www.orangecountyfl.net/WaterGarbageRecycling/BillPaymentOptions.aspx', 'https://cityofblakely.net/pay-online/', 'https://www.epbnet.com/index.php/support/bill-pay/', 'http://www.bcestn.org/index.php/manage-existing-service/pay-my-monthly-bill/106-pay-by-phone-or-online', 'https://www.salemmo.com/city/government/departments/utility_department/index.php', 'https://www.lexingtontn.gov/pay_online.html', 'https://www.newbernnc.gov/departments/administration/finance/utilities_business_office/pay_my_bill.php', 'https://www.tsemc.net/my-account/pay-bill-online/', 'https://cpws.com/my-account/', 'https://www.lcub.com/', 'https://www.dothan.org/175/Pay-View-Utility-Bill-Online', 'http://www.pickwickec.com/bill-payment-information/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.tombigbeeelectric.com/payments', 'https://cityofrockwood.com/online-bill-pay', 'http://www.shelbyvillepower.com/', 'https://www.yourubt.com/', 'http://www.clintonutilities.com/pmtopts.html', 'https://www.rse.coop/', 'https://www.geus.org/', 'https://selma-nc.com/departments/customer-service/', 'http://www.clevelandutilities.com/', 'https://www.mayfieldews.com/index.php/electric/smartpay', 'https://guntersvilleal.org/departments/utilites/', 'https://ripleypower.com/account/payment-options.php', 'http://www.mub-albertville.com/', 'http://www.franklinepb.com/bill-payment-options', 'https://lagrangenc.com/703/Online-Billing', 'https://www.cityofdouglasga.gov/84/Make-a-Utility-Payment', 'https://www.townofbenson.com/2191/Bill-Payment', 'https://www.scecnet.net/content/pay-my-bill', 'http://www.glasgowepb.net/?page_id=343', 'https://www.needhelppayingbills.com/html/tarrant_county_assistance_prog.html', 'https://www.tvec.com/index.asp?fullsite=1']

"""
for i in query:
    for j in search("Official government website for " + i, tld="co.in", num=1, stop=1, pause=3):
        print(j)

"""
"""
find_date('http://blog.python.org/2016/12/python-360-is-now-available.html')

for i in utility_links:
    if i == "https://www.caneyforkec.com" or i == "https://lakeworthbeachfl.gov/payment-portal/" or i == "https://midstateelectric.coop/payment-options" or i == "https://www.rse.coop/" or i == "https://www.stemc.com/my-payment-options" or i == "https://www.scecnet.net/content/pay-my-bill" or i == "https://www.tsemc.net/my-account/pay-bill-online/" or i == "http://unioncitytn.gov/pay-online.html":
        print("None")
    else:
        print(find_date(i, original_date=True))

# pip htmldate -max MAXDATE -u [utility_links]
"""
"""
print(""*5)

for i in gov_links:
    if i == "https://www.caneyforkec.com" or i == "https://lakeworthbeachfl.gov/payment-portal/" or i == "https://midstateelectric.coop/payment-options" or i == "https://www.rse.coop/" or i == "https://www.stemc.com/my-payment-options" or i == "https://www.scecnet.net/content/pay-my-bill" or i == "https://www.tsemc.net/my-account/pay-bill-online/" or i == "http://unioncitytn.gov/pay-online.html":
        print("None")
    else:
        print(find_date(i, original_date=True))

print(""*5)
"""


"""
import whois
w = whois.whois('https://www.humboldtutilities.com/') 
print(w)
"""

"""
customers_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQcmuZiLz645g0LV2MetG-9Uj4EeTxGMVGPR7D4U88hh-pgEyLKM7nVAuC3k4-6peJ6MevszPQ01IE5/pub?output=csv"

customers_df = pd.read_csv(customers_url)

customers_df = customers_df.loc[:, customers_df.columns.intersection(["Customer","Reed Link"])]

customers_df['Reed Link'] = customers_df['Reed Link'].replace(np.nan, 0)

customers_df.rename(columns = {"Reed Link": "Reed_Link"}, inplace=True)

df_new = customers_df.query("Reed_Link==0")

df_new.set_index("Customer")

ukn = df_new["Customer"].tolist()

for i in ukn:
    for j in search("Utility website for " + i, tld="co.in", num=1, stop=1, pause=3):
        print(j)
"""
"""
import whois
import json
import time

New_Utility_Links = ['https://www.ci.richland.wa.us/departments/energy-services', 'https://cityofcovington.org/index.php?section=covington_utilities3', 'http://unioncitytn.gov/pay-online.html', 'https://dicksonelectric.com/', 'https://www.jea.com/my_account/billing_and_payment_options/', 'https://www.mtpleasant-tn.gov/utility-payments', 'https://www.sepb.net/payment-2/bill-pay/', 'https://www.fulton-ky.com/frequently-asked-questions/', 'https://www.cityofblueridgega.gov/WastewaterandWater.aspx', 'https://midstateelectric.coop/payment-options', 'https://wkrecc.com/index.php/18-billing', 'https://mdec.org/', 'https://www.mlgw.com/residential/payingyourbill_b', 'https://www.caneyforkec.com/', 'https://www.humboldtutilities.com/', 'http://www.hsutilities.com/', 'https://www.cityofmadison.com/water', 'https://hop-electric.com/electric/residential-electric/bill-payment-options/', 'https://ace-power.com/account/payment-options/', 'https://www.ocalafl.org/government/city-departments-a-h/customer-service-office/pay-my-bill', 'https://www.bolivarutility.com/', 'https://lakeworthbeachfl.gov/payment-portal/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.bpu.com/', 'https://www.cityofdenton.com/en-us/pay-my-bill', 'https://www.stemc.com/my-payment-options', 'https://www.dixie.coop/online-account-access', 'https://www.orangecountyfl.net/WaterGarbageRecycling/BillPaymentOptions.aspx', 'https://cityofblakely.net/pay-online/', 'https://www.epbnet.com/index.php/support/bill-pay/', 'http://www.bcestn.org/index.php/manage-existing-service/pay-my-monthly-bill/106-pay-by-phone-or-online', 'https://www.salemmo.com/city/government/departments/utility_department/index.php', 'https://www.lexingtontn.gov/pay_online.html', 'https://www.newbernnc.gov/departments/administration/finance/utilities_business_office/pay_my_bill.php', 'https://www.tsemc.net/my-account/pay-bill-online/', 'https://cpws.com/my-account/', 'https://www.lcub.com/', 'https://www.dothan.org/175/Pay-View-Utility-Bill-Online', 'http://www.pickwickec.com/bill-payment-information/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.tombigbeeelectric.com/payments', 'https://cityofrockwood.com/online-bill-pay', 'http://www.shelbyvillepower.com/', 'https://www.yourubt.com/', 'http://www.clintonutilities.com/pmtopts.html', 'https://www.rse.coop/', 'https://www.geus.org/', 'https://selma-nc.com/departments/customer-service/', 'http://www.clevelandutilities.com/', 'https://www.mayfieldews.com/index.php/electric/smartpay', 'https://guntersvilleal.org/departments/utilites/', 'https://ripleypower.com/account/payment-options.php', 'http://www.mub-albertville.com/', 'http://www.franklinepb.com/bill-payment-options', 'https://lagrangenc.com/703/Online-Billing', 'https://www.cityofdouglasga.gov/84/Make-a-Utility-Payment', 'https://www.townofbenson.com/2191/Bill-Payment', 'https://www.scecnet.net/content/pay-my-bill', 'http://www.glasgowepb.net/?page_id=343', 'https://www.needhelppayingbills.com/html/tarrant_county_assistance_prog.html', 'https://www.tvec.com/index.asp?fullsite=1']

DNS_0 = []
DNS_1 = []
DNS_2 = []
DNS_3 = []
DNS_4 = []


t = (5)


for i in New_Utility_Links:
    data = whois.whois(i)
    if "name" in data:
        DNS_0.append(data["name"])
    elif "registrant_name" in data:
        DNS_0.append(data["registrant_name"])
    elif "admin_name" in data:
        DNS_0.append(data["admin_name"])
    else:
        DNS_0.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "name" in data:
        DNS_1.append(data["name"])
    elif "registrant_name" in data:
        DNS_1.append(data["registrant_name"])
    elif "admin_name" in data:
        DNS_1.append(data["admin_name"])
    else:
        DNS_1.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "name" in data:
        DNS_2.append(data["name"])
    elif "registrant_name" in data:
        DNS_2.append(data["registrant_name"])
    elif "admin_name" in data:
        DNS_2.append(data["admin_name"])
    else:
        DNS_2.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "name" in data:
        DNS_3.append(data["name"])
    elif "registrant_name" in data:
        DNS_3.append(data["registrant_name"])
    elif "admin_name" in data:
        DNS_3.append(data["admin_name"])
    else:
        DNS_3.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "name" in data:
        DNS_4.append(data["name"])
    elif "registrant_name" in data:
        DNS_4.append(data["registrant_name"])
    elif "admin_name" in data:
        DNS_4.append(data["admin_name"])
    else:
        DNS_4.append("None")

DNS_df = pd.DataFrame(
    {'DNS_0': DNS_0,
     'DNS_1': DNS_1,
     'DNS_2': DNS_2,
     'DNS_3': DNS_3,
     'DNS_4': DNS_4,
    })

print(DNS_df)

DNS_df.replace(to_replace ="none", value ="nan")
DNS_df.replace(to_replace ="None", value ="nan")

print(DNS_df)

DNS_df["DNS_0"].fillna(DNS_df["DNS_1"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_2"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_3"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_4"])

print(DNS_df)

DNS_df = DNS_df.drop(["DNS_1", "DNS_2", "DNS_3", "DNS_4"], axis=1)

print(DNS_df)

final = DNS_df["DNS_0"].tolist()

for i in final:
    print(i)
"""


"""
import whois
import json
import time

New_Utility_Links = ['https://www.ci.richland.wa.us/departments/energy-services', 'https://cityofcovington.org/index.php?section=covington_utilities3', 'http://unioncitytn.gov/pay-online.html', 'https://dicksonelectric.com/', 'https://www.jea.com/my_account/billing_and_payment_options/', 'https://www.mtpleasant-tn.gov/utility-payments', 'https://www.sepb.net/payment-2/bill-pay/', 'https://www.fulton-ky.com/frequently-asked-questions/', 'https://www.cityofblueridgega.gov/WastewaterandWater.aspx', 'https://midstateelectric.coop/payment-options', 'https://wkrecc.com/index.php/18-billing', 'https://mdec.org/', 'https://www.mlgw.com/residential/payingyourbill_b', 'https://www.caneyforkec.com/', 'https://www.humboldtutilities.com/', 'http://www.hsutilities.com/', 'https://www.cityofmadison.com/water', 'https://hop-electric.com/electric/residential-electric/bill-payment-options/', 'https://ace-power.com/account/payment-options/', 'https://www.ocalafl.org/government/city-departments-a-h/customer-service-office/pay-my-bill', 'https://www.bolivarutility.com/', 'https://lakeworthbeachfl.gov/payment-portal/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.bpu.com/', 'https://www.cityofdenton.com/en-us/pay-my-bill', 'https://www.stemc.com/my-payment-options', 'https://www.dixie.coop/online-account-access', 'https://www.orangecountyfl.net/WaterGarbageRecycling/BillPaymentOptions.aspx', 'https://cityofblakely.net/pay-online/', 'https://www.epbnet.com/index.php/support/bill-pay/', 'http://www.bcestn.org/index.php/manage-existing-service/pay-my-monthly-bill/106-pay-by-phone-or-online', 'https://www.salemmo.com/city/government/departments/utility_department/index.php', 'https://www.lexingtontn.gov/pay_online.html', 'https://www.newbernnc.gov/departments/administration/finance/utilities_business_office/pay_my_bill.php', 'https://www.tsemc.net/my-account/pay-bill-online/', 'https://cpws.com/my-account/', 'https://www.lcub.com/', 'https://www.dothan.org/175/Pay-View-Utility-Bill-Online', 'http://www.pickwickec.com/bill-payment-information/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.tombigbeeelectric.com/payments', 'https://cityofrockwood.com/online-bill-pay', 'http://www.shelbyvillepower.com/', 'https://www.yourubt.com/', 'http://www.clintonutilities.com/pmtopts.html', 'https://www.rse.coop/', 'https://www.geus.org/', 'https://selma-nc.com/departments/customer-service/', 'http://www.clevelandutilities.com/', 'https://www.mayfieldews.com/index.php/electric/smartpay', 'https://guntersvilleal.org/departments/utilites/', 'https://ripleypower.com/account/payment-options.php', 'http://www.mub-albertville.com/', 'http://www.franklinepb.com/bill-payment-options', 'https://lagrangenc.com/703/Online-Billing', 'https://www.cityofdouglasga.gov/84/Make-a-Utility-Payment', 'https://www.townofbenson.com/2191/Bill-Payment', 'https://www.scecnet.net/content/pay-my-bill', 'http://www.glasgowepb.net/?page_id=343', 'https://www.needhelppayingbills.com/html/tarrant_county_assistance_prog.html', 'https://www.tvec.com/index.asp?fullsite=1']

DNS_0 = []
DNS_1 = []
DNS_2 = []
DNS_3 = []
DNS_4 = []


t = (5)


for i in New_Utility_Links:
    data = whois.whois(i)
    if "registrar" in data:
        DNS_0.append(data["registrar"])
    elif "registrar_name" in data:
        DNS_0.append(data["registrar_name"])
    else:
        DNS_0.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "registrar" in data:
        DNS_1.append(data["registrar"])
    elif "registrar_name" in data:
        DNS_1.append(data["registrar_name"])
    else:
        DNS_1.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "registrar" in data:
        DNS_2.append(data["registrar"])
    elif "registrar_name" in data:
        DNS_2.append(data["registrar_name"])
    else:
        DNS_2.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "registrar" in data:
        DNS_3.append(data["registrar"])
    elif "registrar_name" in data:
        DNS_3.append(data["registrar_name"])
    else:
        DNS_3.append("None")

time.sleep(t)

for i in New_Utility_Links:
    data = whois.whois(i)
    if "registrar" in data:
        DNS_4.append(data["registrar"])
    elif "registrar_name" in data:
        DNS_4.append(data["registrar_name"])
    else:
        DNS_4.append("None")

DNS_df = pd.DataFrame(
    {'DNS_0': DNS_0,
     'DNS_1': DNS_1,
     'DNS_2': DNS_2,
     'DNS_3': DNS_3,
     'DNS_4': DNS_4,
    })

print(DNS_df)

DNS_df.replace(to_replace ="none", value ="nan")
DNS_df.replace(to_replace ="None", value ="nan")

print(DNS_df)

DNS_df["DNS_0"].fillna(DNS_df["DNS_1"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_2"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_3"])
DNS_df["DNS_0"].fillna(DNS_df["DNS_4"])

print(DNS_df)

DNS_df = DNS_df.drop(["DNS_1", "DNS_2", "DNS_3", "DNS_4"], axis=1)

print(DNS_df)

final = DNS_df["DNS_0"].tolist()

for i in final:
    print(i)
"""
"""
# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

total_urls_visited = 0

urls = []

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                #print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        #print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls


def crawl(url, max_urls=30):
    global total_urls_visited
    total_urls_visited += 1
    #print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)
"""
"""
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time

query = "myusage"
query_return = []

for i in New_Utility_Links:
    try:
        print("Testing " + i)

        # Test 1st page & capture all internal and external
        # test all internal for query
        internal_urls = []
        external_urls = []

        domain_name = urlparse(i).netloc
        req = requests.get(i)
        soup = BeautifulSoup(req.content, 'html.parser')
        for tag in soup.findAll("a"):
            href = tag.attrs.get("href")

            if href == "" or href is None:
                continue
            
            href = urljoin(i, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

            if domain_name not in href:
                if href not in external_urls:
                    if ".com" in href or ".net" in href or ".org" in href or ".co" in href or ".us" in href or ".uk" in href or ".in" in href:
                        if ".pdf" not in href or ".DOC" not in href or ".DOCX" not in href:
                            external_urls.append(href)
                continue
            else:
                if href not in internal_urls:
                    if ".com" in href or ".net" in href or ".org" in href or ".co" in href or ".us" in href or ".uk" in href or ".in" in href:
                        if ".pdf" not in href and ".DOC" not in href and ".DOCX" not in href:
                            internal_urls.append(href)
                continue
        
        #print(str(len(internal_urls)))
        #print(str(len(external_urls)))
        if query in external_urls:
            query_return.append("True")
        else:
            for j in internal_urls:
                try:
                    #print("Testing " + j + " inside of " + i)
                    req = requests.get(j)
                    soup = BeautifulSoup(req.content, 'html.parser')
                    for tag in soup.findAll("a"):
                        href = tag.attrs.get("href")

                        if href == "" or href is None:
                            continue
                        
                        href = urljoin(j, href)
                        parsed_href = urlparse(href)
                        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
                        if href in external_urls:
                            continue
                        if domain_name not in href:
                            if href not in external_urls:
                                if ".com" in href or ".net" in href or ".org" in href or ".co" in href or ".us" in href or ".uk" in href or ".in" in href:
                                    if ".pdf" not in href or ".DOC" not in href or ".DOCX" not in href:
                                        external_urls.append(href)
                            continue
                except:
                    continue
            
            checks = []
            for exlink in external_urls:
                if query in exlink:
                    checks.append("True")
                else:
                    checks.append("False")
            
            if "True" in checks:
                query_return.append("True")
            else:
                query_return.append("False")
                    

    except:
        query_return.append("Failure")

for boolean in query_return:
    print(boolean)
"""






import pandas as pd
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time

query = "myusage"

df = pd.DataFrame({"URL":[],"BOOL":[""]})
print(df)

for i in New_Utility_Links:
    try:
        df = pd.DataFrame({"Names":["Tom", "Bill", "Jerry"],"Age":["5", "50", "15"]})
        print(df)
    except:

query_return = df['BOOL'].tolist()
for boolean in query_return:
    print(boolean)




""" 
FOR TESTING
Wiper is cool, good thing about it is I don't have to type '()' around it. Here is slight variation to it

# wiper.py
import os
class Cls(object):
    def __repr__(self):
        os.system('cls')
        return ''
The usage is quite simple:

>>> cls = Cls()
>>> cls # this will clear console.




TIMER THREADING AKA DAEMON THREADING
    from time import sleep
    from threading import Thread

    def some_task():
        while True:
            pass

    t = Thread(target=some_task)  # run the some_task function in another
                                # thread
    t.daemon = True               # Python will exit when the main thread
                                # exits, even if this thread is still
                                # running
    t.start()

    snooziness = int(raw_input('Enter the amount of seconds you want to run this: '))
    sleep(snooziness)

    # Since this is the end of the script, Python will now exit.  If we
    # still had any other non-daemon threads running, we wouldn't exit.
    # However, since our task is a daemon thread, Python will exit even if
    # it's still going.

WHILE "THREAD"
    import time

    max_time = int(raw_input('Enter the amount of seconds you want to run this: '))
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < max_time:
        do_stuff()
"""

















































"""
ALL FUNCTIONS IN A CLASS


import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import argparse
import pandas as pd

class Dataset:
    # Constructor
    def __init__(self, names, search_query):
        self.names = names
        self.search_query = search_query

        '''
        parser = argparse.ArgumentParser()
        parser.add_argument("names",)
        parser.add_argument("search_query", help="This is required for scraping a link to a website from a name...")
        '''
    
    def get_website(self):
    
    def get_all_links_per_website(self):
        print(self.names)
    
    def get_all info(self):
        print("")
    
    def clear_and_print(self):


    








# Call these fuctions / objects
Names = ['Richland Energy Services', 'City of Covington - (GA)', 'Union City Energy Authority', 'Dickson Electric Systems', 'JEA', 'Mount Pleasant Power System', 'Scottsboro Electric Power Board', 'Fulton Electric System', 'Blue Ridge Mountain EMC', 'Midstate', 'West Kentucky RECC', 'Marshall-DeKalb EC', 'Memphis Light, Gas, & Water', 'Caney Fork EC', 'Humboldt Utilities', 'Holly Springs Electric Department', 'City of Madison', 'Hopkinsville Electric System', 'ACE Power', 'Ocala Utility Services', 'Bolivar Energy Authority', 'Lake Worth Beach Utilities', 'Wilson Energy', 'Kansas City BPU', 'Denton Municipal Electric', 'Southwest Tennessee EMC', 'Dixie Electric Coop', 'Orlando Utilities Commission', 'City of Blakely', 'Russellville Electric Plant Board', 'Benton County Electric System', 'City of Salem, MO', 'Lexington Electric System', 'City of New Bern', 'Tri-State', 'Columbia Power and Water Systems', 'Lenoir City Utilities Board', 'Dothan', 'Pickwick EC', 'Wilson Internet', 'Tombigbee EPA', 'Rockwood Electric Utility', 'Shelbyville Power System', 'Utilities Board of Tuskegee (UBT)', 'Clinton Utilities Board', 'Rush Shelby', 'Greenville Electric Utility System (GEUS)', 'Town of Selma', 'Cleveland Utilities', 'Mayfield Electric & Water Systems', 'Guntersville Electric Board', 'Ripley Power and Light Cpmpany', 'Albertville Municipal Utilities Board', 'Franklin EPB', 'Town of La Grange', 'City of Douglas', 'Town of Benson', 'St Croix EC', 'Glasgow EPB', 'City of Tarrant Electric Department', 'Tennessee Valley EC']
search_query = input("Type the search that you would like to perform(for example, type: 'Official utility website for '(should include space at the end)) : ")
Dataset = Dataset(Names, search_query)
Dataset.
"""
