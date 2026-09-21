#rapid-struct definition file
#github.com/lh-dd/rapid-struct

VerKey, "Version check key", 0x702aec, str(32)
dwProtocolVer, "ProtocolVer check key", 0x147987, hex(4)
@group "CritErrorIP"
CritErrorIP, "Octet_1", 1426974, u8
CritErrorIP, "Octet_2", 1426975, u8
CritErrorIP, "Octet_3", 1426976, u8
CritErrorIP, "Octet_4", 1426977, u8
@endgroup
CritErrorPort, "Port", 1426992, u16