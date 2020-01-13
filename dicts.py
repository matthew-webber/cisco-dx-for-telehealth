xml_dict = dict(
    headers= {'Content-Type': 'application/xml'},
    DX=dict(
        commands=dict(
            alert='<Command><UserInterface><Message><Alert><Display><Duration>$1</Duration><Text>$2</Text><Title>$3</Title></Display></Alert></Message></UserInterface></Command>',
            prompt='<Command><UserInterface><Message><Prompt><Display><FeedbackId>$feedbackid</FeedbackId><Option.1>$option1</Option.1><Option.2>$option2</Option.2><Option.3>$option3</Option.3><Option.4>$option4</Option.4><Option.5>$option5</Option.5><Text>$text</Text><Title>$title</Title></Display></Prompt></Message></UserInterface></Command>',
            reboot='<Command><SystemUnit><Boot><Action>Restart</Action></Boot></SystemUnit></Command>'
        ),

    ),
    SX=dict(
        commands=dict(
            reboot='<Command><Boot><Action>Restart</Action></Boot></Command>'
        ),
    ),
    commands= dict(
        call= '<Command><Dial><Number>{{}}</Number></Dial></Command>',
        disconnect= '<Command><Call><Disconnect></Disconnect></Call></Command>',
        accept= '<Command><Call><Accept></Accept></Call></Command>',
        ignore= '<Command><Call><Ignore><CallId></CallId></Ignore></Call></Command>',
        reject= '<Command><Call><Reject></Reject></Call></Command>',
        disconnect_all= '<Command><Call><DisconnectAll></DisconnectAll></Call></Command>',
        play_ringtone='<Command><Audio><SoundsAndAlerts><Ringtone><Play><RingTone>{{}}</RingTone></Play></Ringtone></SoundsAndAlerts></Audio></Command>'
    ),
    configuration= dict(
        ring_volume='<Configuration><Audio><SoundsAndAlerts><RingVolume>{{}}</RingVolume></SoundsAndAlerts></Audio></Configuration>'
    ),
    ringtones= dict(
        a='Sunrise',
        b='Mischief',
    )
)

url_dict = dict(
    login='http://{{}}/web/signin/open',
    post_xml='http://{{}}/putxml',
)