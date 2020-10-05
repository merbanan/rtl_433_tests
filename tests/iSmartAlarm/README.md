iSmartAlarm Sensors

They operate on the 908M frequency in North America

Additional Information https://blog.seekintoo.com/diy-smart-home-security-meh/

From the above link, someone already attempted to decode it/receive code using rfcat_receiver.  
Here is the config used:

def ConfigureD(d, freq):
    d.setModeIDLE()
    d.setMdmModulation(MOD_GFSK)
    d.setFreq(freq)
    d.setMdmDeviatn(19042.969)
    d.setMdmChanBW(101562.5)
    d.setMdmDRate(38383.5)
    d.setMdmChanSpc(199951.172)
    d.setMdmChanSpc(51000)
    d.setMdmSyncWord(0xd391)
    d.setMdmSyncMode(SYNCM_CARRIER)
    d.setEnablePktCRC(1)
    d.setEnablePktDataWhitening(0)
    d.setEnablePktAppendStatus(0)
    d.makePktFLEN(0xff)
    d.makePktVLEN()
    d.printRadioConfig()
