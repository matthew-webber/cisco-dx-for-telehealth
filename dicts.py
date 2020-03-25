xml_dict = dict(
    headers= {'Content-Type': 'application/xml'},
    DX=dict(
        commands=dict(
            alert='<Command><UserInterface><Message><Alert><Display><Duration>$1</Duration><Text>$2</Text><Title>$3</Title></Display></Alert></Message></UserInterface></Command>',
            prompt='<Command><UserInterface><Message><Prompt><Display><FeedbackId>$feedbackid</FeedbackId><Option.1>$option1</Option.1><Option.2>$option2</Option.2><Option.3>$option3</Option.3><Option.4>$option4</Option.4><Option.5>$option5</Option.5><Text>$text</Text><Title>$title</Title></Display></Prompt></Message></UserInterface></Command>',
            reboot='<Command><SystemUnit><Boot><Action>Restart</Action></Boot></SystemUnit></Command>',
        ),

    ),
    SX=dict(
        commands=dict(
            reboot='<Command><Boot><Action>Restart</Action></Boot></Command>'
        ),
    ),
    commands= dict(
        call= '<Command><Dial><Number>{{}}</Number></Dial></Command>',
        delete_callhistory= '<Command><CallHistory><DeleteAll><Filter>All</Filter></DeleteAll></CallHistory></Command>',
        disconnect= '<Command><Call><Disconnect></Disconnect></Call></Command>',
        accept= '<Command><Call><Accept></Accept></Call></Command>',
        ignore= '<Command><Call><Ignore><CallId></CallId></Ignore></Call></Command>',
        reject= '<Command><Call><Reject></Reject></Call></Command>',
        disconnect_all= '<Command><Call><DisconnectAll></DisconnectAll></Call></Command>',
        play_ringtone='<Command><Audio><SoundsAndAlerts><Ringtone><Play><RingTone>{{}}</RingTone></Play></Ringtone></SoundsAndAlerts></Audio></Command>',
        play_sound='<Command><Audio><Sound><Play><Sound>{{}}</Sound></Play></Sound></Audio></Command>',
        stop_sound='<Command><Audio><Sound><Stop></Stop></Sound></Audio></Command>',
        set_volume='<Command><Audio><Volume><Set><Level>{{}}</Level></Set></Volume></Audio></Command>',
        # phonebook_search='<Command><Phonebook><Search><ContactType>$contact_type</ContactType><Recursive>True</Recursive><Limit>$limit</Limit><Offset>0</Offset><SearchString>$search_str</SearchString><PhonebookType>Local</PhonebookType><PhonebookId></PhonebookId></Search></Phonebook></Command>',
        phonebook_search='<Command><Phonebook><Search><ContactType>$contact_type</ContactType><Recursive>True</Recursive><Limit>$limit</Limit><Offset>0</Offset><PhonebookType>Local</PhonebookType><PhonebookId></PhonebookId></Search></Phonebook></Command>',
        contact_add='<Command><Phonebook><Contact><Add><Tag>$tag</Tag><Device>$device</Device><CallType>$call_type</CallType><CallRate>$call_rate</CallRate><Protocol>$protocol</Protocol><Number>$number</Number><Title></Title><ImageURL></ImageURL><FolderId></FolderId><Name>$name</Name></Add></Contact></Phonebook></Command>',
        contact_delete='<Command><Phonebook><Contact><Delete><ContactId>$contact_id</ContactId></Delete></Contact></Phonebook></Command>',
    ),
    configuration= dict(
        ring_volume='<Configuration><Audio><SoundsAndAlerts><RingVolume>{{}}</RingVolume></SoundsAndAlerts></Audio></Configuration>',
        external_manager='<Configuration><Provisioning><ExternalManager><Address>{{}}</Address></ExternalManager></Provisioning></Configuration>',
        provisioning_mode='<Configuration><Provisioning><Mode>{{}}</Mode></Provisioning></Configuration>',
    ),
    status= dict(
        ip_address='Status/Network/IPv4/Address',
        call_string='Status/SIP/Registration/URI',
        device_name='Status/UserInterface/ContactInfo/Name',

    ),
)

url_dict = dict(
    login='http://{{}}/web/signin/open',
    post_xml='http://{{}}/putxml',
    get_xml='http://{{}}/getxml?location=',
)

# http://128.23.200.189/getxml?location=/Status/SIP/Registration/URI

#