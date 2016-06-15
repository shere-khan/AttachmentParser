import xml.etree.ElementTree as ET

import Forms

import AttachmentParser as AP

if __name__ == '__main__':
    # xml_file = 'c:\\Users\\barryjus\\Documents\\ggc\\prod_attachment_data\\test_data2_key_contacts.xml'
    xml_file = 'C:\\Users\\barryjus\\Documents\\ggc\\prod_attachment_data\\attachments\\GRANT12175496_file_xml.xml'
    tree = ET.parse(xml_file);
    root = tree.getroot();
    
    # create XML namespaces dictionary to be passed to XML parsing library 
    ns = {'grant': 'http://apply.grants.gov/system/MetaGrantApplication',
          'globLib': 'http://apply.grants.gov/system/GlobalLibrary-V2.0',
          'glob': 'http://apply.grants.gov/system/Global-V1.0',
          'att': 'http://apply.grants.gov/system/Attachments-V1.0',
          'header': 'http://apply.grants.gov/system/Header-V1.0',
          'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
          'SF424_2_1': 'http://apply.grants.gov/forms/SF424_2_1-V2.1',
          'Budget': 'http://apply.grants.gov/forms/Budget-V1.1',
          'Project':'http://apply.grants.gov/forms/Project-V1.1',
          'SFLLL_1_2': 'http://apply.grants.gov/forms/SFLLL_1_2-V1.2',
          'Other': 'http://apply.grants.gov/forms/Other-V1.1',
          'ns1': 'http://apply.grants.gov/system/Global-V1.0',
          'Key_Contacts': 'http://apply.grants.gov/forms/Key_Contacts-V1.0',
          'footer': 'http://apply.grants.gov/system/Footer-V1.0',
          'SF424B': 'http://apply.grants.gov/forms/SF424B-V1.1',
          'ProtectionofHumanSubjects': 'http://apply.grants.gov/forms/ProtectionofHumanSubjects-V1.1',
          'SFLLL': 'http://apply.grants.gov/forms/SFLLL-V1.1',
          'SFLLL_1_2': 'http://apply.grants.gov/forms/SFLLL_1_2-V1.2'}

    # Create GMS_GG_FORM_RECORD
    # Get GMS_APPLCIATION_ID 
    gov_tracking_no = AP.extract_text('footer:GrantSubmissionFooter/footer:Grants_govTrackingNumber', root, ns)

    # Extract Key Contact Form XML data
    key_contact_xml = AP.extract_form_xml(xml_file, '<Key_Contacts:Key_Contacts', '</Key_Contacts:Key_Contacts')

    # Print GMS_GG_FORM Sql insert statement
    AP.create_gms_gg_form(gov_tracking_no, 'KEY_CONTACT_FORM', key_contact_xml)

    # Get APPLICANT_ORG_NAME text value
    app_org_name = AP.extract_text('grant:Forms/Key_Contacts:Key_Contacts/Key_Contacts:ApplicantOrganizationName', root, ns)

    AP.create_gg_key_contact_form(gov_tracking_no, app_org_name)

    # Create GMS_GG_KEY_CONTACT_FORM record
    contact_order = 0
    for elem in root.findall('grant:Forms/Key_Contacts:Key_Contacts/Key_Contacts:RoleOnProject', ns):
        key_contact = Forms.KeyContact()

        key_contact.set_contact_order(contact_order)

        key_contact.set_project_role(AP.extract_text('Key_Contacts:ContactProjectRole', elem, ns))
        key_contact.set_first_name(AP.extract_text('Key_Contacts:ContactName/globLib:FirstName', elem, ns))
        key_contact.set_middle_name(AP.extract_text('Key_Contacts:ContactName/globLib:MiddleName', elem, ns))
        key_contact.set_last_name(AP.extract_text('Key_Contacts:ContactName/globLib:LastName', elem, ns))
        key_contact.set_suffix_name(AP.extract_text('Key_Contacts:ContactName/globLib:SuffixName', elem, ns))
        key_contact.set_prefix_name(AP.extract_text('Key_Contacts:ContactName/globLib:PrefixName', elem, ns))
        key_contact.set_contact_title(AP.extract_text('Key_Contacts:ContactTitle', elem, ns))
        key_contact.set_org_affil(AP.extract_text('Key_Contacts:ContactOrganizationalAffiliation', elem, ns))
        key_contact.set_street1(AP.extract_text('Key_Contacts:ContactAddress/globLib:Street1', elem, ns))
        key_contact.set_street2(AP.extract_text('Key_Contacts:ContactAddress/globLib:Street2', elem, ns))
        key_contact.set_city(AP.extract_text('Key_Contacts:ContactAddress/globLib:City', elem, ns))
        key_contact.set_state(AP.extract_text('Key_Contacts:ContactAddress/globLib:State', elem, ns))
        key_contact.set_zip_code(AP.extract_text('Key_Contacts:ContactAddress/globLib:ZipPostalCode', elem, ns))
        key_contact.set_country(AP.extract_text('Key_Contacts:ContactAddress/globLib:Country', elem, ns))
        key_contact.set_county(AP.extract_text('Key_Contacts:ContactAddress/globLib:County', elem, ns))
        key_contact.set_province(AP.extract_text('Key_Contacts:ContactAddress/globLib:Province', elem, ns))
        key_contact.set_fax(AP.extract_text('Key_Contacts:ContactAddress/globLib:Fax', elem, ns))
        key_contact.set_phone(AP.extract_text('Key_Contacts:ContactPhone', elem, ns))
        key_contact.set_email(AP.extract_text('Key_Contacts:ContactEmail', elem, ns))

        # Create GMS_GG_KEY_CONTACT records
        AP.create_gg_key_contact(gov_tracking_no, key_contact)
        contact_order+=1
    
    # Extract Assurances Form XML string
    assurances_form_xml = AP.extract_form_xml(xml_file, '<SF424B:Assurances', '</SF424B:Assurances>')

    AP.create_gms_gg_form(gov_tracking_no, 'ASSURANCES_FORM', assurances_form_xml)

    # Extract Assurances form data
    rep_title = AP.extract_text('grant:Forms/SF424B:Assurances/SF424B:AuthorizedRepresentative/SF424B:RepresentativeTitle', root, ns)
    rep_name = AP.extract_text('grant:Forms/SF424B:Assurances/SF424B:AuthorizedRepresentative/SF424B:RepresentativeName', root, ns)
    app_org_name = AP.extract_text('grant:Forms/SF424B:Assurances/SF424B:ApplicantOrganizationName', root, ns)
    submitted_date = AP.extract_text('grant:Forms/SF424B:Assurances/SF424B:SubmittedDate', root, ns)
    
    # Create Assurances form SQL
    AP.create_assurances_form(gov_tracking_no, rep_name, rep_title, app_org_name, submitted_date)

    # Extract Human Subject Form XML String
    human_sub_form_xml = AP.extract_form_xml(xml_file, '<ProtectionofHumanSubjects:ProtectionofHumanSubjects',
                                            '</ProtectionofHumanSubjects:ProtectionofHumanSubjects>')

    AP.create_gms_gg_form(gov_tracking_no, 'HUMAN_SUBJECT_FORM', human_sub_form_xml)

    # Extract Disc Lobby Form XML String
    disc_lobby_form_xml = AP.extract_form_xml(xml_file, '<SFLLL_1_2:LobbyingActivitiesDisclosure',
                                              '</SFLLL_1_2:LobbyingActivitiesDisclosure')
    # If null, search for other form of tag
    if disc_lobby_form_xml is None:
        disc_lobby_form_xml = AP.extract_form_xml(xml_file, '<SFLLL:LobbyingActivitiesDisclosure',
                                                  '</SFLLL:LobbyingActivitiesDisclosure')
        

    AP.create_gms_gg_form(gov_tracking_no, 'LOBBY_FORM', disc_lobby_form_xml)
    
    fed_action_type = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/SFLLL_1_2:FederalActionType', root, ns) 
    award_amount = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/SFLLL_1_2:AwardAmount', root, ns)
    cfda_number = AP.extract_text(AP.get_lobbying_activities_disc_text() + AP.get_federal_program_name_text() + '/CFDANumber', root, ns)
    fdrl_action_number = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/SFLLL_1_2:FederalActionNumber', root, ns)
    fdrl_agency_dept = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/SFLLL_1_2:FederalAgencyDepartment', root, ns)
    fdrl_program_desc = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/SFLLL_1_2:FederalProgramName/FederalProgramDescription', root, ns)
    fdrl_program_name = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/FederalProgramName/FederalProgramName', root, ns)
    last_report_date = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/MaterialChangeSupplement/LastReportDate', root, ns)
    lobby_reg_address_city = AP.extract_text(AP.get_lobby_reg_text() + '/City', root, ns)
    lobby_reg_address_state = AP.extract_text(AP.get_lobby_reg_text() + '/State', root, ns)
    lobby_reg_address_street1 = AP.extract_text(AP.get_lobby_reg_text() + '/Street1', root, ns)
    lobby_reg_address_street2 = AP.extract_text(AP.get_lobby_reg_text() + '/Street2', root, ns)
    lobby_reg_address_zip = AP.extract_text(AP.get_lobby_reg_text() + 'ZipPostalCode', root, ns)
    lobby_reg_name_first = AP.extract_text(AP.get_lobby_reg_text() + '/FirstName', root, ns)
    lobby_reg_name_last = AP.extract_text(AP.get_lobby_reg_text() + '/LastName', root, ns)
    lobby_reg_name_middle = AP.extract_text(AP.get_lobby_reg_text() + '/MiddleName', root, ns)
    lobby_reg_name_prefix = AP.extract_text(AP.get_lobby_reg_text() + '/PrefixName', root, ns)
    lobby_reg_name_suffix = AP.extract_text(AP.get_lobby_reg_text() + '/SuffixName', root, ns)
    material_change_qtr = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/MaterialChangeSupplement/MaterialChangeQuarter', root, ns)
    material_change_year = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/MaterialChangeSupplement/MaterialChangeYear"', root, ns)
    prime_re_address_city = AP.extract_text(AP.get_prime_text() + '/City', root, ns)
    prime_re_address_state = AP.extract_text(AP.get_prime_text() + '/State', root, ns)
    prime_re_address_street1 = AP.extract_text(AP.get_prime_text() + '/Street1', root, ns)
    prime_re_address_street2 = AP.extract_text(AP.get_prime_text() + '/Street2', root, ns)
    prime_re_address_zip = AP.extract_text(AP.get_prime_text() + '/ZipPostalCode', root, ns)
    prime_re_cong_dist = AP.extract_text(AP.get_prime_text() + '/CongressionalDistrict', root, ns)
    prime_re_org_name = AP.extract_text(AP.get_prime_text() + '/OrganizationName', root, ns)
    re_is_prime = AP.extract_text(AP.get_prime_text() + '/ReportEntityIsPrime', root, ns)
    report_type = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/ReportType', root, ns)
    sig_blk_date = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_name_first = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_name_last = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_name_middle = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_name_prefix = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_name_suffix = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_phone = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_signature = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    sig_blk_title = AP.extract_text(AP.get_sig_block_text() + '', root, ns)
    status_federal_action = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/FederalActionStatus', root, ns)
    tier_value = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/ReportEntity/Tier/TierValue', root, ns)
    type_federal_action = AP.extract_text(AP.get_lobbying_activities_disc_text() + '/FederalActionType', root, ns)
    sub_awd_re_address_city = AP.extract_text(AP.get_sub_awd_text() + '/City', root, ns)
    sub_awd_re_address_state = AP.extract_text(AP.get_sub_awd_text() + '/State', root, ns)
    sub_awd_re_address_street1 = AP.extract_text(AP.get_sub_awd_text() + '/Street1', root, ns)
    sub_awd_re_address_street2 = AP.extract_text(AP.get_sub_awd_text() + '/Street2', root, ns)
    sub_awd_re_address_zip = AP.extract_text(AP.get_sub_awd_text() + '/ZipPostalCode', root, ns)
    sub_awd_re_cong_dist = AP.extract_text(AP.get_sub_awd_text() + '/CongressionalDistrict', root, ns)
    sub_awd_re_org_name = AP.extract_text(AP.get_sub_awd_text() + '/OrganizationName', root, ns)
    # Forms.DiscLobbyForm.set_report_type(self, report_type)
    # create_disc_lobby_form(gov_tracking_no)

    # Extract Lobby Form XML String
    # lobby_form_xml = extract_form_xml(xml_file, '<:', '</:>')

    # create_gms_gg_form(gov_tracking_no, 'LOBBY_FORM', lobby_form_xml)
    
    # create_lobby_form(gov_tracking_no)