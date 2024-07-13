from dataclasses import dataclass

@dataclass
class Hotspot:
    OBJECTID : int
    Borough : str
    Type : str
    Provider : str
    Name : str
    Location : str
    Latitude : float
    Longitude: float
    X: float
    Y: float
    Location_T : str
    Remarks : str
    City : str
    SSID : str
    SourceID : str
    Activated : str
    BoroCode : int
    BoroName : str
    NTACode : str
    NTAName : str
    CounDist: float
    Postcode : int
    BoroCD: float
    CT2010: float
    BCTCB2010: float
    BIN: float
    BBL: float
    DOITT_ID : int
    Location_Lat_Long : str

    def __hash__(self):
        return hash((self.OBJECTID))

    def __str__(self):
        return f"{self.OBJECTID}"