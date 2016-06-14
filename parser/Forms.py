'''
Created on Jun 14, 2016

@author: barryjus
'''

class DiscLobbyForm(object):

    def __init__(self):
        self.perf_serv_name_prefix = 'NULL'
    
    def set_perf_srvc_name_prefix(self, perf_serv_name_prefix):
        self.perf_serv_name_prefix = perf_serv_name_prefix
        
    def set_perf_srvc_name_first(self, perf_serv_name_first):
        self.perf_serv_name_first = perf_serv_name_first

    def set_perf_srvc_name_last(self, perf_serv_name_first):
        self.perf_serv_name_last = perf_serv_name_first

    def set_perf_srvc_name_middle(self, perf_serv_name_first):
        self.perf_serv_name_middle = perf_serv_name_first

    def set_perf_srvc_name_suffix(self, perf_serv_name_first):
        self.perf_serv_name_suffix = perf_serv_name_first
    
class KeyContact(object):
   
    def __init__(self):
        self.contact_order = 'NULL'
        self.project_role = 'NULL'
        self.first_name = 'NULL'
        self.middle_name = 'NULL'
        self.last_name = 'NULL'
        self.suffix_name = 'NULL'
        self.prefix_name = 'NULL'
        self.contact_title = 'NULL'
        self.org_affil = 'NULL'
        self.street1 = 'NULL'
        self.street2 = 'NULL'
        self.city = 'NULL'
        self.state = 'NULL'
        self.zip_code = 'NULL'
        self.country = 'NULL'
        self.county = 'NULL'
        self.email = 'NULL'
        self.phone = 'NULL'
        self.province = 'NULL'
        self.fax = 'NULL'
    
    def set_contact_order(self, contact_order):
        self.contact_order = contact_order
        
    def set_project_role(self, project_role):
        self.project_role = project_role
        
    def set_first_name(self, first_name):
        self.first_name = first_name;
        
    def set_middle_name(self, middle_name):
        self.middle_name = middle_name;
        
    def set_last_name(self, last_name):
        self.last_name = last_name
        
    def set_suffix_name(self, suffix_name):
        self.suffix_name = suffix_name

    def set_prefix_name(self, prefix_name):
        self.prefix_name = prefix_name
    
    def set_contact_title(self, contact_title):
        self.contact_title = contact_title
        
    def set_org_affil(self, org_affil):
        self.org_affil = org_affil
        
    def set_street1(self, street1):
        self.street1 = street1

    def set_street2(self, street2):
        self.street2 = street2

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_country(self, country):
        self.country = country

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_province(self, province):
        self.province = province

    def set_county(self, county):
        self.county = county

    def set_fax(self, fax):
        self.fax = fax