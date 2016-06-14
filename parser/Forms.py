'''
Created on Jun 14, 2016

@author: barryjus
'''

class DiscLobbyForm(object):
    def __init__(self):
        pass

    def set_type_federal_action(self, type_federal_action):
        self.type_federal_action = type_federal_action

    def set_status_federal_action(self, status_federal_action):
        self.status_federal_action = status_federal_action

    def set_report_type(self, report_type):
        self.report_type = report_type

    def set_material_change_year(self, material_change_year):
        self.material_change_year = material_change_year

    def set_material_change_qtr(self, material_change_qtr):
        self.material_change_qtr = material_change_qtr
        
    def set_last_report_date(self, last_report_date):
        self.last_report_date = last_report_date
        
    def set_re_is_prime(self, re_is_prime):
        self.re_is_prime = re_is_prime
        
    def set_prime_re_org_name(self, prime_re_org_name):
        self.prime_re_org_name = prime_re_org_name
        
    def set_prime_re_address_street1(self, prime_re_address_street1):
        self.prime_re_address_street1 = prime_re_address_street1
        
    def set_prime_re_address_street2(self, prime_re_address_street2):
        self.prime_re_address_street2 = prime_re_address_street2

    def set_prime_re_address_city(self, prime_re_address_city):
        self.prime_re_address_city = prime_re_address_city

    def set_prime_re_address_state(self, prime_re_address_state):
        self.prime_re_address_state = prime_re_address_state

    def set_prime_re_address_zip(self, prime_re_address_zip):
        self.prime_re_address_zip = prime_re_address_zip
        
    def set_prime_re_cong_dist(self, prime_re_cong_dist):
        self.prime_re_cong_dist = prime_re_cong_dist
        
    def set_sub_awd_re_org_name(self, sub_awd_re_org_name):
        self.sub_awd_re_org_name = sub_awd_re_org_name
        
    def set_sub_awd_re_address_street1(self, sub_awd_re_address_street1):
        self.sub_awd_re_address_street1 = sub_awd_re_address_street1

    def set_sub_awd_re_address_street2(self, sub_awd_re_address_street2):
        self.sub_awd_re_address_street2 = sub_awd_re_address_street2

    def set_sub_awd_re_address_city(self, sub_awd_re_address_city):
        self.sub_awd_re_address_city = sub_awd_re_address_city

    def set_sub_awd_re_address_state(self, sub_awd_re_address_state):
        self.sub_awd_re_address_state = sub_awd_re_address_state

    def set_sub_awd_re_address_zip(self, sub_awd_re_address_zip):
        self.sub_awd_re_address_zip = sub_awd_re_address_zip
        
    def set_sub_awd_re_cong_dist(self, sub_awd_re_cong_dist):
        self.sub_awd_re_cong_dist = sub_awd_re_cong_dist
        
    def set_tier_value(self, tier_value):
        self.tier_value = tier_value
        
    def set_fdrl_agency_dept(self, fdrl_agency_dept):
        self.fdrl_agency_dept = fdrl_agency_dept
        
    def set_fdrl_program_name(self, fdrl_program_name):
        self.fdrl_program_name = fdrl_program_name

    def set_fdrl_program_desc(self, fdrl_program_desc):
        self.fdrl_program_desc = fdrl_program_desc
        
    def set_cfda_number(self, cfda_number):
        self.cfda_number = cfda_number
        
    def set_fdrl_action_number(self, fdrl_action_number):
        self.fdrl_action_number = fdrl_action_number
        
    def set_award_amount(self, award_amount):
        self.award_amount = award_amount
        
    def set_lobby_reg_name_prefix(self, lobby_reg_name_prefix):
        self.lobby_reg_name_prefix = lobby_reg_name_prefix

    def set_lobby_reg_name_first(self, lobby_reg_name_first):
        self.lobby_reg_name_first = lobby_reg_name_first

    def set_lobby_reg_name_middle(self, lobby_reg_name_middle):
        self.lobby_reg_name_middle = lobby_reg_name_middle

    def set_lobby_reg_name_last(self, lobby_reg_name_last):
        self.lobby_reg_name_last = lobby_reg_name_last

    def set_lobby_reg_name_suffix(self, lobby_reg_name_suffix):
        self.lobby_reg_name_suffix = lobby_reg_name_suffix
        
class LobbyPerfSrvc(object):

    def __init__(self):
        self.perf_serv_name_prefix = 'NULL'
    
    def set_perf_srvc_name_prefix(self, perf_serv_name_prefix):
        self.perf_serv_name_prefix = perf_serv_name_prefix
        
    def set_perf_srvc_name_first(self, perf_srvc_name_first):
        self.perf_serv_name_first = perf_srvc_name_first

    def set_perf_srvc_name_last(self, perf_srvc_name_last):
        self.perf_serv_name_last = perf_srvc_name_last

    def set_perf_srvc_name_middle(self, perf_srvc_name_middle):
        self.perf_serv_name_middle = perf_srvc_name_middle

    def set_perf_srvc_name_suffix(self, perf_srvc_name_suffix):
        self.perf_serv_name_suffix = perf_srvc_name_suffix

    def set_perf_srvc_address_street1(self, perf_srvc_address_street1):
        self.perf_serv_address_street1 = perf_srvc_address_street1

    def set_perf_srvc_address_street2(self, perf_srvc_address_street2):
        self.perf_serv_address_street2 = perf_srvc_address_street2

    def set_perf_srvc_address_city(self, perf_srvc_address_city):
        self.perf_serv_address_city = perf_srvc_address_city

    def set_perf_srvc_address_state(self, perf_srvc_address_state):
        self.perf_serv_address_state = perf_srvc_address_state

    def set_perf_srvc_address_zip(self, perf_srvc_address_zip):
        self.perf_serv_address_zip = perf_srvc_address_zip

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