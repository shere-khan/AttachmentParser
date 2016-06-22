'''
Created on Jun 7, 2016

@author: barryjus
'''

def create_gms_gg_form(gov_tracking_no, form_code, xml_data_string):
    print "insert into gms_gg_form \n(gms_gg_form_id, gms_gg_application_id, form_xml_document, ref_code_id_gg_form_type," \
          " created_user_id, created_date, created_ip)\nvalues\n" \
          "(gms_gg_form_seq.nextval, (select gms_gg_application_id from gms_gg_application where gms_application_id =\n(select gms_application_id from gmsg2k.gms_application where gov_tracking_no" \
          "='%s')), '%s', \n(select ref_code_id from gmsg2k.ref_code where code = '%s'), " \
          "(select created_user_id from gmsg2k.gms_application where \ngov_tracking_no ='%s'), sysdate, " \
          "'@connector.name@')\n"%(gov_tracking_no, xml_data_string, form_code, gov_tracking_no)
    
def create_gg_key_contact_form(gov_tracking_no, app_org_name):
    select_gms_gg_form_id_str = select_gms_gg_form_id(gov_tracking_no)
    select_gms_user_str = select_gms_user(gov_tracking_no)
    print "insert into gms_gg_key_contact_form\n(gms_gg_key_contact_form_id, gms_gg_form_id, applicant_org_name, created_user_id," \
          "created_date, created_ip) values\n(gms_gg_key_contact_form_seq.nextval, (%s),\n'%s'," \
          ", (%s), sysdate, '@connector.name@')\n"%(select_gms_gg_form_id_str, app_org_name, select_gms_user_str)

def select_gms_user(gov_tracking_no):
    return "select created_user_id from gmsg2k.gms_application where gov_tracking_no ='%s'"%(gov_tracking_no)

def create_gg_key_contact(gov_tracking_no, key_contact):
    #print select_gms_gg_key_contact_form_id(gov_tracking_no)
    select_gms_user_str = select_gms_user(gov_tracking_no)
    print "insert into gms_gg_key_contact\n(gms_gg_key_contact_id, gms_gg_key_contact_form_id, " \
          "contact_order, contact_project_role,\n contact_name_prefix, contact_name_first, contact_name_middle," \
          " contact_name_last,\n contact_name_suffix, contact_title, contact_org_affiliation, contact_address_street1," \
          " contact_address_street2,\n contact_address_city, contact_address_county, contact_address_state, " \
          "contact_address_province, contact_address_zip,\n contact_address_country, contact_fax, contact_email," \
          " contact_phone, created_user_id, created_date, created_ip)\nvalues\n" \
          "(gms_gg_key_contact_seq.nextval, (%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, (%s), sysdate, '@connector.name')" \
          "\n"%(select_gms_gg_key_contact_form_id(gov_tracking_no), key_contact.contact_order, key_contact.project_role,
                key_contact.prefix_name, key_contact.first_name, key_contact.middle_name,
                key_contact.last_name, key_contact.suffix_name, key_contact.contact_title,
                key_contact.org_affil, key_contact.street1, key_contact.street2,
                key_contact.city, key_contact.county, key_contact.state, key_contact.province, 
                key_contact.zip_code, key_contact.country, key_contact.fax, key_contact.email, key_contact.phone, select_gms_user_str)

def select_gms_gg_key_contact_form_id(gov_tracking_no):
    return "select gms_gg_key_contact_form_id from gms_gg_key_contact_form" \
           " where gms_gg_form_id = (%s)"%(select_gms_gg_form_id(gov_tracking_no))

def select_gms_gg_form_id(gov_tracking_no):
    return "select gms_gg_form_id from gms_gg_form where gms_gg_application_id =\n" \
          "(select gms_gg_application_id from gms_gg_application where gms_application_id = \n" \
          "(select gms_application_id from gmsg2k.gms_application where gov_tracking_no='%s'))\n" \
          " and ref_code_id_gg_form_type = (select ref_code_id from ref_code where code = 'KEY_CONTACT_FORM'\n and ref_code_type_id=" \
          " (select ref_code_type_id from ref_code_type where code_type='GG_FORM_TYPE'))"%(gov_tracking_no)

def create_assurances_form(gov_tracking_no, representative_name, representative_title, applicant_org, submitted_date):
    print "insert into gms_gg_assurances_form (gms_gg_assurances_form_id, gms_gg_form_id, representatitve_name,\n"\
          "representative_title, applicant_orginization, submitted_date, created_user_id, created_date, created_ip)\nvalues\n"\
          "(gms_gg_assurances_form_seq.nextval, (%s),\n%s, %s, %s, %s,\n(%s), sysdate, " \
          "'@connector.name')\n"%(select_gms_gg_form_id(gov_tracking_no), representative_name, representative_title, applicant_org,
                                submitted_date, select_gms_user(gov_tracking_no))
 
def create_disc_lobby_form(gov_tracking_no, dlf):
    print "insert into gms_gg_disc_lobby_act_form (gms_gg_disc_lobby_act_form_id, gms_gg_form_id,"\
          "type_federal_action, status_federal_action, report_type, material_change_year, material_change_qtr,"\
          "last_report_date, re_is_prime, prime_re_org_name, prime_re_address_street1, prime_re_address_street2"\
          "prime_re_address_city, prime_re_address_state, prime_re_address_zip, prime_re_cong_dist, "\
          "fdrl_agency_dept, fdrl_program_name, fdrl_program_desc, cfda_number,"\
          "fdrl_action_number, award_amount, lobby_reg_name_prefix, lobby_reg_name_first, lobby_reg_name_middle, lobby_reg_name_last"\
          "lobby_reg_name_suffix, lobby_reg_address_street1, lobby_reg_address_street2, lobby_reg_address_city, lobby_reg_address_state,"\
          "lobby_reg_address_zip, sig_blk_name_prefix, sig_blk_name_first, sig_blk_name_middle, sig_blk_name_last,"\
          "sig_blk_name_suffix, sig_blk_phone, sig_blk_date, created_user_id, created_date, created_ip"\
          ")\nvalues\n"\
          "(gms_gg_disc_lobby_act_form_seq.nextval, (%s),\n%s, %s, %s, %s, %s, "\
          "%s, %s, %s, %s,\n%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\n%s, %s, %s,"\
          "%s, %s, %s, %s, %s, %s, %s,\n%s, %s, %s, %s,\n%s, %s, %s, (%s), %s, %s"\
          "%s)"%(select_gms_gg_form_id(gov_tracking_no), dlf.type_federal_action, dlf.status_federal_action,
                 dlf.report_type, dlf.material_change_year, dlf.material_change_qtr, dlf.last_report_date,
                 dlf.re_is_prime, dlf.prime_re_org_name, dlf.prime_re_address_street1, dlf.prime_re_address_street2,
                 dlf.prime_re_address_city, dlf.prime_re_address_state, dlf.prime_re_address_zip,
                 dlf.prime_re_cong_dist, dlf.fdrl_agency_dept, dlf.fdrl_program_name, dlf.fdrl_program_desc,
                 dlf.cfda_number, dlf.fdrl_action_number, dlf.award_amount, dlf.lobby_reg_name_prefix,
                 dlf.lobby_reg_name_first, dlf.lobby_reg_name_middle, dlf.lobby_reg_name_last, dlf.lobby_reg_name_suffix,
                 dlf.lobby_reg_address_street1, dlf.lobby_reg_address_street2, dlf.lobby_reg_address_city,
                 dlf.lobby_reg_address_state, dlf.lobby_reg_address_zip, dlf.sig_blk_name_prefix,
                 dlf.sig_blk_name_first, dlf.sig_blk_name_middle, dlf.sig_blk_name_last, dlf.sig_blk_name_suffix,
                 dlf.sig_blk_phone, dlf.sig_blk_date, select_gms_user(gov_tracking_no), "'sysdate'", "'@connector.name'")

def create_lobby_perf_srvc(lps, gov_tracking_no):
    print "insert into gms_gg_lobby_perf_srvc"\
    "(gms_gg_lobby_perf_srvc_id, gms_gg_disc_lobby_act_form_id,\n"\
        "perf_srvc_name_prefix, perf_srvc_name_first, perf_srvc_name_middle,\n"\
        "perf_srvc_name_last, perf_srvc_name_suffix, perf_srvc_address_street1,\n"\
        "perf_srvc_address_street2, perf_srvc_address_city, perf_srvc_address_state,\n"\
        "perf_srvc_address_zip, created_user_id, created_date,\n"\
        "created_ip)\n"\
    "values\n"\
    "(gms_gg_lobby_perf_srvc_seq.nextval, (), %s, %s, %s, %s, %s, %s, %s, %s, %s,"\
    "%s, %s, %s, %s)"%(select_disc_lobby_form_id(gov_tracking_no), lps.perf_serv_name_prefix,
                       lps.perf_serv_name_first, lps.perf_serv_name_middle, lps.perf_serv_name_last,
                       lps.perf_serv_name_suffix, lps.perf_serv_address_street1, lps.perf_serv_address_street2,
                       lps.perf_serv_address_city, lps.perf_serv_address_state, lps.perf_serv_address_zip,
                       select_gms_user(gov_tracking_no), "'sysdate'", "'@connector.name'")

def select_disc_lobby_form_id(gov_tracking_no):
    print "select gms_gg_disc_lobby_form_id from gms_gg_disc_lobby_form where"\
          " gms_gg_form_id = (%s)"%(select_gms_gg_form_id(gov_tracking_no))

def create_lobby_form(gov_tracking_no):
    pass

def extract_text(xpath, root_node, ns):
    node = root_node.find(xpath, ns)
    if node is not None:
        return node.text.replace('\n', '')

def extract_form_xml(form_xml_file, xml_begin_tag, xml_end_tag):
    form_xml = '<?xml version="1.0" encoding="UTF-8"?>'
    with open(form_xml_file) as f:
        build_string = False 
        for line in f:
            key_contact_begin = line.find(xml_begin_tag)
            if key_contact_begin != -1:
                build_string = True
            key_contact_end = line.find(xml_end_tag)
            if key_contact_end > -1:
                form_xml += line + ' '
                break
            if build_string:
                form_xml += line
        return form_xml.replace('\n', '')
        # todo: may have to replace amp&; and such with actual values before inserting

def get_report_entity_text():
    return get_lobbying_activities_disc_text() + get_sflll_1_2_ns_text() + 'ReportEntity'

def get_reporting_entity_text():
    return get_report_entity_text() + get_sflll_1_2_ns_text() + 'ReportingEntity'

def get_reporting_entity_address_text():
    return get_reporting_entity_text() + get_sflll_1_2_ns_text() + 'Address'

def get_lobby_reg_text():
    return get_lobbying_activities_disc_text() + get_sflll_1_2_ns_text() + 'LobbyingRegistrant'

def get_sub_awd_text():
    return get_lobbying_activities_disc_text() + get_sflll_1_2_ns_text() + 'ReportEntity' + get_sflll_1_2_ns_text() + 'SubAwardee'

def get_sig_block_text():
    return get_lobbying_activities_disc_text() + get_sflll_1_2_ns_text() + 'SignatureBlock'

def get_signature_block_name_text():
    return get_sig_block_text() + get_sflll_1_2_ns_text() + 'Name' 

def get_lobbying_activities_disc_text():
    return 'grant:Forms' + get_sflll_1_2_ns_text() + 'LobbyingActivitiesDisclosure_1_2'

def get_federal_program_name_text():
    return get_sflll_1_2_ns_text() + 'FederalProgramName'

def get_sflll_1_2_ns_text():
    return '/SFLLL_1_2:'

def get_glob_lib_text():
    return '/globLib:'

def get_ind_per_serv_text():
    return get_lobbying_activities_disc_text() + get_sflll_1_2_ns_text() + 'IndividualsPerformingServices'

def get_ind_per_serv_indv_text():
    return 'SFLLL_1_2:Individual'

def get_ind_per_serv_address_text():
    return 'SFLLL_1_2:Address'

def get_ind_name_text():
    return get_ind_per_serv_indv_text() + get_sflll_1_2_ns_text() + 'Name'

def get_lob_reg_address_text():
    return get_lobby_reg_text() + get_sflll_1_2_ns_text() + 'Address'

def get_lob_reg_name_text():
    return get_lobby_reg_text() + get_sflll_1_2_ns_text() + 'IndividualName'