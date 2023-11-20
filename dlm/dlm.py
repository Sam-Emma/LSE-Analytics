import openai
import os
import json
from dlm.seckey import openapi_key
os.environ["OPENAI_API_KEY"]= openapi_key



import datetime

#query=input("query")

symbols= [{'symbol': '3IN', 'symbol_name': '3I GRP.'},
 {'symbol': 'AAF', 'symbol_name': '3I INF. ORD'},
 {'symbol': 'AAL', 'symbol_name': '4IMPRINT GRP.'},
 {'symbol': 'ABDN', 'symbol_name': 'A.B.FOOD'},
 {'symbol': 'ABF', 'symbol_name': 'ABERFTH.SMLL.CO'},
 {'symbol': 'ADM', 'symbol_name': 'ABRDN PLC'},
 {'symbol': 'AGR', 'symbol_name': 'ABRDN PVT EQUIT'},
 {'symbol': 'AGT', 'symbol_name': 'ADMIRAL GRP'},
 {'symbol': 'AHT', 'symbol_name': 'AIRTEL AFRICA'},
 {'symbol': 'AJB', 'symbol_name': 'AJ BELL'},
 {'symbol': 'AML', 'symbol_name': 'ALLIANCE TRUST'},
 {'symbol': 'ANTO', 'symbol_name': 'ALLIANZ TECH'},
 {'symbol': 'APAX', 'symbol_name': 'ANGLO AMERICAN'},
 {'symbol': 'APEO', 'symbol_name': 'ANTOFAGASTA'},
 {'symbol': 'ASC', 'symbol_name': 'APAX GLB'},
 {'symbol': 'ASCL', 'symbol_name': 'ASCENTIAL'},
 {'symbol': 'ASHM', 'symbol_name': 'ASHMORE'},
 {'symbol': 'ASL', 'symbol_name': 'ASHTEAD GRP.'},
 {'symbol': 'ATG', 'symbol_name': 'ASOS'},
 {'symbol': 'ATST', 'symbol_name': 'ASSURA'},
 {'symbol': 'ATT', 'symbol_name': 'ASTON MARTIN'},
 {'symbol': 'AUTO', 'symbol_name': 'ASTRAZENECA'},
 {'symbol': 'AV.', 'symbol_name': 'AUCTION TECH'},
 {'symbol': 'AZN', 'symbol_name': 'AUTO TRAD'},
 {'symbol': 'BA.', 'symbol_name': 'AVI GLOBAL TST'},
 {'symbol': 'BAB', 'symbol_name': 'AVIVA'},
 {'symbol': 'BAG', 'symbol_name': 'B&M EUROPEAN'},
 {'symbol': 'BAKK', 'symbol_name': 'BABCOCK INTL'},
 {'symbol': 'BARC', 'symbol_name': 'BAE SYS.'},
 {'symbol': 'BATS', 'symbol_name': 'BAILLIE G.JAP.'},
 {'symbol': 'BBGI', 'symbol_name': 'BAKKAVOR'},
 {'symbol': 'BBH', 'symbol_name': 'BALANCED CPT LD'},
 {'symbol': 'BBOX', 'symbol_name': 'BALFOUR B.'},
 {'symbol': 'BBY', 'symbol_name': 'BALTIC'},
 {'symbol': 'BCG', 'symbol_name': 'BANK OF GEORGIA'},
 {'symbol': 'BCPT', 'symbol_name': 'BANKERS INV.TST'},
 {'symbol': 'BDEV', 'symbol_name': 'BARCLAYS'},
 {'symbol': 'BEZ', 'symbol_name': 'BARR (A.G.)'},
 {'symbol': 'BGEO', 'symbol_name': 'BARRATT DEVEL.'},
 {'symbol': 'BGFD', 'symbol_name': 'BBGI GLB INF'},
 {'symbol': 'BHMG', 'symbol_name': 'BEAZLEY'},
 {'symbol': 'BKG', 'symbol_name': 'BELLEVUE HEALTH'},
 {'symbol': 'BLND', 'symbol_name': 'BELLWAY'},
 {'symbol': 'BME', 'symbol_name': 'BERKELEY GP.HLD'},
 {'symbol': 'BNKR', 'symbol_name': 'BH MACRO GBP'},
 {'symbol': 'BNZL', 'symbol_name': 'BIG YELLOW GRP'},
 {'symbol': 'BOY', 'symbol_name': 'BLACKROCK GREAT'},
 {'symbol': 'BP.', 'symbol_name': 'BLACKROCK SML'},
 {'symbol': 'BPT', 'symbol_name': 'BLACKROCK WLD'},
 {'symbol': 'BRBY', 'symbol_name': 'BLUEFIELD SOLAR'},
 {'symbol': 'BRGE', 'symbol_name': 'BODYCOTE'},
 {'symbol': 'BRSC', 'symbol_name': 'BP'},
 {'symbol': 'BRWM', 'symbol_name': 'BR.AMER.TOB.'},
 {'symbol': 'BSIF', 'symbol_name': 'BR.LAND'},
 {'symbol': 'BT.A', 'symbol_name': 'BR.THROG.TRUST'},
 {'symbol': 'BVIC', 'symbol_name': 'BRIDGEPOINT'},
 {'symbol': 'BWY', 'symbol_name': 'BRITVIC'},
 {'symbol': 'BYG', 'symbol_name': 'BT GROUP'},
 {'symbol': 'BYIT', 'symbol_name': 'BUNZL'},
 {'symbol': 'CBG', 'symbol_name': 'BURBERRY GRP'},
 {'symbol': 'CCC', 'symbol_name': 'BYTES TECH'},
 {'symbol': 'CCH', 'symbol_name': 'C&C GRP'},
 {'symbol': 'CCL', 'symbol_name': 'CALEDONIA INV.'},
 {'symbol': 'CCR', 'symbol_name': 'CAPITA GROUP'},
 {'symbol': 'CEY', 'symbol_name': 'CAPITAL GEARING'},
 {'symbol': 'CGT', 'symbol_name': 'CAPRICORN ENERG'},
 {'symbol': 'CHG', 'symbol_name': 'CARNIVAL'},
 {'symbol': 'CKN', 'symbol_name': 'CENTAMIN'},
 {'symbol': 'CLDN', 'symbol_name': 'CENTRICA'},
 {'symbol': 'CLI', 'symbol_name': 'CHEMRING GRP.'},
 {'symbol': 'CMCX', 'symbol_name': 'CITY LON.'},
 {'symbol': 'CNA', 'symbol_name': 'CLARKSON'},
 {'symbol': 'CNE', 'symbol_name': 'CLOSE BR.GRP.'},
 {'symbol': 'COA', 'symbol_name': 'CLS HDGS'},
 {'symbol': 'CPG', 'symbol_name': 'CMC MKTS'},
 {'symbol': 'CPI', 'symbol_name': 'COATS GROUP'},
 {'symbol': 'CRDA', 'symbol_name': 'COCACOLA HBC AG'},
 {'symbol': 'CRH', 'symbol_name': 'COMPASS GROUP'},
 {'symbol': 'CRST', 'symbol_name': 'COMPUTACENTER'},
 {'symbol': 'CTEC', 'symbol_name': 'CONVATEC'},
 {'symbol': 'CTY', 'symbol_name': 'CRANSWICK'},
 {'symbol': 'CURY', 'symbol_name': 'CREST NICHOLSON'},
 {'symbol': 'CWK', 'symbol_name': 'CRH'},
 {'symbol': 'DARK', 'symbol_name': 'CRODA INTL.'},
 {'symbol': 'DCC', 'symbol_name': 'CURRYS PLC'},
 {'symbol': 'DEC', 'symbol_name': 'DARKTRACE'},
 {'symbol': 'DGE', 'symbol_name': 'DCC'},
 {'symbol': 'DGI9', 'symbol_name': 'DECHRA PHARM'},
 {'symbol': 'DLG', 'symbol_name': 'DERWENT LONDON'},
 {'symbol': 'DLN', 'symbol_name': 'DIAGEO'},
 {'symbol': 'DNLM', 'symbol_name': 'DIGITAL 9'},
 {'symbol': 'DOCS', 'symbol_name': 'DIPLOMA'},
 {'symbol': 'DOM', 'symbol_name': 'DIRECT LINE'},
 {'symbol': 'DPH', 'symbol_name': 'DISCOVERIE GRP.'},
 {'symbol': 'DPLM', 'symbol_name': 'DIVERSIFIED EN'},
 {'symbol': 'DRX', 'symbol_name': "DOMINO'S PIZZA"},
 {'symbol': 'DSCV', 'symbol_name': 'DOWLAIS GROUP'},
 {'symbol': 'DWL', 'symbol_name': 'DR.MARTENS'},
 {'symbol': 'EBOX', 'symbol_name': 'DRAX'},
 {'symbol': 'EDIN', 'symbol_name': 'DUNELM'},
 {'symbol': 'EDV', 'symbol_name': 'EASYJET'},
 {'symbol': 'ELM', 'symbol_name': 'EDIN.INV.TST.'},
 {'symbol': 'EMG', 'symbol_name': 'EDIN.WWIDE INV'},
 {'symbol': 'ENOG', 'symbol_name': 'ELEMENTIS'},
 {'symbol': 'ENT', 'symbol_name': 'EMPIRIC'},
 {'symbol': 'EOT', 'symbol_name': 'ENDEAVOUR MIN'},
 {'symbol': 'ESCT', 'symbol_name': 'ENERGEAN'},
 {'symbol': 'ESNT', 'symbol_name': 'ENTAIN'},
 {'symbol': 'ESP', 'symbol_name': 'ESSENTRA'},
 {'symbol': 'EWI', 'symbol_name': 'EURO OPPS TR.'},
 {'symbol': 'EXPN', 'symbol_name': 'EUROPEAN SMALL.'},
 {'symbol': 'EZJ', 'symbol_name': 'EXPERIAN'},
 {'symbol': 'FAN', 'symbol_name': 'F &C IV.TST'},
 {'symbol': 'FCIT', 'symbol_name': 'FDM GROUP HLDG'},
 {'symbol': 'FCSS', 'symbol_name': 'FERREXPO'},
 {'symbol': 'FDM', 'symbol_name': 'FID.SP.VAL.'},
 {'symbol': 'FEML', 'symbol_name': 'FIDELITY CHINA'},
 {'symbol': 'FEV', 'symbol_name': 'FIDELITY E.M.LD'},
 {'symbol': 'FGP', 'symbol_name': 'FIDELITY EUROPE'},
 {'symbol': 'FGT', 'symbol_name': 'FINSBURY GTH.'},
 {'symbol': 'FLTR', 'symbol_name': 'FIRSTGROUP'},
 {'symbol': 'FOUR', 'symbol_name': 'FLUTTER ENT'},
 {'symbol': 'FRAS', 'symbol_name': 'FORESIGHT SOLAR'},
 {'symbol': 'FRES', 'symbol_name': 'FRASERS GRP'},
 {'symbol': 'FSFL', 'symbol_name': 'FRESNILLO'},
 {'symbol': 'FSV', 'symbol_name': 'FUTURE'},
 {'symbol': 'FUTR', 'symbol_name': 'GAMES WORKSHOP'},
 {'symbol': 'FXPO', 'symbol_name': 'GCP INFRA.'},
 {'symbol': 'GAW', 'symbol_name': 'GENUIT GRP PLC'},
 {'symbol': 'GCP', 'symbol_name': 'GENUS'},
 {'symbol': 'GEN', 'symbol_name': 'GLB SML CO TRST'},
 {'symbol': 'GFTU', 'symbol_name': 'GLENCORE'},
 {'symbol': 'GLEN', 'symbol_name': 'GR.PORTLAND'},
 {'symbol': 'GNS', 'symbol_name': 'GRAFTON GRP.UTS'},
 {'symbol': 'GPE', 'symbol_name': 'GRAINGER'},
 {'symbol': 'GRG', 'symbol_name': 'GREENCOAT UK'},
 {'symbol': 'GRI', 'symbol_name': 'GREGGS'},
 {'symbol': 'GROW', 'symbol_name': 'GSK'},
 {'symbol': 'GSCT', 'symbol_name': 'HALEON'},
 {'symbol': 'GSK', 'symbol_name': 'HALMA'},
 {'symbol': 'HAS', 'symbol_name': 'HAMMERSON'},
 {'symbol': 'HBR', 'symbol_name': 'HARBOUR ENERGY'},
 {'symbol': 'HFG', 'symbol_name': 'HARBOURVEST'},
 {'symbol': 'HGT', 'symbol_name': 'HARGREAVES LANS'},
 {'symbol': 'HICL', 'symbol_name': 'HAYS'},
 {'symbol': 'HIK', 'symbol_name': 'HELIOS TOWERS'},
 {'symbol': 'HILS', 'symbol_name': 'HEND.SMALL COS.'},
 {'symbol': 'HL.', 'symbol_name': 'HERALD INV.'},
 {'symbol': 'HLMA', 'symbol_name': 'HG CAPITAL'},
 {'symbol': 'HLN', 'symbol_name': 'HICL INFRASTRU.'},
 {'symbol': 'HMSO', 'symbol_name': 'HIKMA'},
 {'symbol': 'HRI', 'symbol_name': 'HILL & SMITH'},
 {'symbol': 'HSBA', 'symbol_name': 'HILTON FOOD'},
 {'symbol': 'HSL', 'symbol_name': 'HIPGNOSIS SONG.'},
 {'symbol': 'HSX', 'symbol_name': 'HISCOX'},
 {'symbol': 'HTG', 'symbol_name': 'HOWDEN JOINERY'},
 {'symbol': 'HTWS', 'symbol_name': 'HSBC HLDGS.UK'},
 {'symbol': 'HVPE', 'symbol_name': 'HUNTING'},
 {'symbol': 'HWDN', 'symbol_name': 'IBSTOCK'},
 {'symbol': 'IAG', 'symbol_name': 'ICG ENT TRST'},
 {'symbol': 'IBST', 'symbol_name': 'IG GROUP'},
 {'symbol': 'ICGT', 'symbol_name': 'IMI'},
 {'symbol': 'ICP', 'symbol_name': 'IMP.BRANDS'},
 {'symbol': 'IDS', 'symbol_name': 'IMPAX ENV.MKT'},
 {'symbol': 'IEM', 'symbol_name': 'INCHCAPE'},
 {'symbol': 'IGG', 'symbol_name': 'INDIVIOR'},
 {'symbol': 'IHG', 'symbol_name': 'INFORMA'},
 {'symbol': 'IHP', 'symbol_name': 'INT.CAP.GRP'},
 {'symbol': 'III', 'symbol_name': 'INTERCON. HOTEL'},
 {'symbol': 'IMB', 'symbol_name': 'INTERTEK GROUP'},
 {'symbol': 'IMI', 'symbol_name': 'INTGRAFIN HLDG'},
 {'symbol': 'INCH', 'symbol_name': 'INTL CONSOL AIR'},
 {'symbol': 'INDV', 'symbol_name': 'INTL DIST SERV'},
 {'symbol': 'INF', 'symbol_name': 'INTL PUBLIC'},
 {'symbol': 'INPP', 'symbol_name': 'INVESTEC'},
 {'symbol': 'INVP', 'symbol_name': 'IP GROUP'},
 {'symbol': 'IPO', 'symbol_name': 'ITHACA ENERGY'},
 {'symbol': 'ITH', 'symbol_name': 'ITV'},
 {'symbol': 'ITRK', 'symbol_name': 'IWG'},
 {'symbol': 'ITV', 'symbol_name': 'JD SPORTS'},
 {'symbol': 'IWG', 'symbol_name': 'JLEN ENV'},
 {'symbol': 'JAM', 'symbol_name': 'JOHNSON MATTHEY'},
 {'symbol': 'JD.', 'symbol_name': 'JPMOR INDIAN'},
 {'symbol': 'JDW', 'symbol_name': 'JPMOR.AMER.'},
 {'symbol': 'JEDT', 'symbol_name': 'JPMORG.EUR'},
 {'symbol': 'JFJ', 'symbol_name': 'JPMORG.GBL.G&I'},
 {'symbol': 'JGGI', 'symbol_name': 'JPMORGAN EMERG'},
 {'symbol': 'JII', 'symbol_name': 'JPMORGAN JAPAN.'},
 {'symbol': 'JLEN', 'symbol_name': 'JTC PLC'},
 {'symbol': 'JMAT', 'symbol_name': 'JUPITER FND'},
 {'symbol': 'JMG', 'symbol_name': 'JUST GROUP'},
 {'symbol': 'JTC', 'symbol_name': 'KAINOS GROUP'},
 {'symbol': 'JUP', 'symbol_name': 'KELLER GRP.'},
 {'symbol': 'JUST', 'symbol_name': 'KINGFISHER'},
 {'symbol': 'KGF', 'symbol_name': 'LANCASHIRE'},
 {'symbol': 'KLR', 'symbol_name': 'LAND SECS.'},
 {'symbol': 'KNOS', 'symbol_name': 'LAW.DEB.CORP'},
 {'symbol': 'LAND', 'symbol_name': 'LEGAL&GEN.'},
 {'symbol': 'LGEN', 'symbol_name': 'LIONTRUST A.M.'},
 {'symbol': 'LIO', 'symbol_name': 'LLOYDS GRP.'},
 {'symbol': 'LLOY', 'symbol_name': 'LON.STK.EXCH'},
 {'symbol': 'LMP', 'symbol_name': 'LONDONMETRIC'},
 {'symbol': 'LRE', 'symbol_name': 'LXI REIT'},
 {'symbol': 'LSEG', 'symbol_name': 'M&G PLC'},
 {'symbol': 'LWDB', 'symbol_name': 'MAN GROUP'},
 {'symbol': 'LXI', 'symbol_name': 'MARKS & SP.'},
 {'symbol': 'MAB', 'symbol_name': 'MARSHALLS'},
 {'symbol': 'MCG', 'symbol_name': 'ME GROUP INTL.'},
 {'symbol': 'MDC', 'symbol_name': 'MEDICLINIC'},
 {'symbol': 'MEGP', 'symbol_name': 'MELROSE IND'},
 {'symbol': 'MGAM', 'symbol_name': 'MERCANTILE INV.'},
 {'symbol': 'MGNS', 'symbol_name': 'MERCHANTS TST'},
 {'symbol': 'MKS', 'symbol_name': 'MITCHELLS & BUT'},
 {'symbol': 'MNDI', 'symbol_name': 'MITIE GRP.'},
 {'symbol': 'MNG', 'symbol_name': 'MOBICO GRP'},
 {'symbol': 'MNKS', 'symbol_name': 'MOLTEN VENTURES'},
 {'symbol': 'MONY', 'symbol_name': 'MONDI'},
 {'symbol': 'MRC', 'symbol_name': 'MONEYSUP.'},
 {'symbol': 'MRCH', 'symbol_name': 'MONKS INV.TST.'},
 {'symbol': 'MRO', 'symbol_name': 'MORGAN ADVANCED'},
 {'symbol': 'MSLH', 'symbol_name': 'MORGN SINDL GRP'},
 {'symbol': 'MTO', 'symbol_name': 'MURRAY INC.TST.'},
 {'symbol': 'MUT', 'symbol_name': 'MURRAY INTL.TST'},
 {'symbol': 'MYI', 'symbol_name': 'NAT.EXPRESS'},
 {'symbol': 'N91', 'symbol_name': 'NATIONAL GRID'},
 {'symbol': 'NAS', 'symbol_name': 'NATWEST GRP'},
 {'symbol': 'NBPE', 'symbol_name': 'NB PRIV. EQTY'},
 {'symbol': 'NESF', 'symbol_name': 'NETWORK INTL'},
 {'symbol': 'NETW', 'symbol_name': 'NEXT'},
 {'symbol': 'NEX', 'symbol_name': 'NEXTENERGY SOL.'},
 {'symbol': 'NG.', 'symbol_name': 'NINETY ONE PLC'},
 {'symbol': 'NWG', 'symbol_name': 'NORTH ATL.SMLR'},
 {'symbol': 'NXT', 'symbol_name': 'OCADO'},
 {'symbol': 'OCDO', 'symbol_name': 'OCTOPUS RENEW.'},
 {'symbol': 'ORIT', 'symbol_name': 'OSB GROUP'},
 {'symbol': 'OSB', 'symbol_name': 'OXFORD INSTRMNT'},
 {'symbol': 'OXIG', 'symbol_name': 'PACIFIC HORIZON'},
 {'symbol': 'PAG', 'symbol_name': 'PAGEGROUP'},
 {'symbol': 'PAGE', 'symbol_name': 'PANTHEON INT.'},
 {'symbol': 'PCT', 'symbol_name': 'PARAGON GRP.'},
 {'symbol': 'PETS', 'symbol_name': 'PEARSON'},
 {'symbol': 'PFD', 'symbol_name': 'PENNON GROUP'},
 {'symbol': 'PHI', 'symbol_name': 'PERSHING SQUARE'},
 {'symbol': 'PHLL', 'symbol_name': 'PERSIMMON'},
 {'symbol': 'PHNX', 'symbol_name': 'PERSONAL ASSETS'},
 {'symbol': 'PHP', 'symbol_name': 'PETERSHILL'},
 {'symbol': 'PIN', 'symbol_name': 'PETS AT HOME'},
 {'symbol': 'PLUS', 'symbol_name': 'PHOENIX GRP HDG'},
 {'symbol': 'PNL', 'symbol_name': 'PLAYTECH'},
 {'symbol': 'PNN', 'symbol_name': 'PLUS500'},
 {'symbol': 'PRTC', 'symbol_name': 'POLAR CAP.'},
 {'symbol': 'PRU', 'symbol_name': 'PREM FOODS'},
 {'symbol': 'PSH', 'symbol_name': 'PRIMARY HEALTH'},
 {'symbol': 'PSN', 'symbol_name': 'PRUDENTIAL'},
 {'symbol': 'PSON', 'symbol_name': 'PURETECH'},
 {'symbol': 'PTEC', 'symbol_name': 'PZ CUSSONS'},
 {'symbol': 'PZC', 'symbol_name': 'QINETIQ'},
 {'symbol': 'QLT', 'symbol_name': 'QUILTER PLC'},
 {'symbol': 'QQ.', 'symbol_name': 'RATHBONES GROUP'},
 {'symbol': 'RAT', 'symbol_name': 'RECKITT BEN. GP'},
 {'symbol': 'RCP', 'symbol_name': 'REDDE NORTHGATE'},
 {'symbol': 'RDW', 'symbol_name': 'REDROW'},
 {'symbol': 'REDD', 'symbol_name': 'RELX'},
 {'symbol': 'REL', 'symbol_name': 'RENEWABLES'},
 {'symbol': 'RHIM', 'symbol_name': 'RENISHAW'},
 {'symbol': 'RICA', 'symbol_name': 'RENTOKIL INITL.'},
 {'symbol': 'RIO', 'symbol_name': 'RHI MAGNESITA'},
 {'symbol': 'RKT', 'symbol_name': 'RIGHTMOVE'},
 {'symbol': 'RMV', 'symbol_name': 'RIO TINTO'},
 {'symbol': 'ROR', 'symbol_name': 'RIT CAPITAL'},
 {'symbol': 'RR.', 'symbol_name': 'ROLLS-ROYCE HLG'},
 {'symbol': 'RS1', 'symbol_name': 'ROTORK'},
 {'symbol': 'RSW', 'symbol_name': 'RS GROUP'},
 {'symbol': 'RTO', 'symbol_name': 'RUFFER INV. CO.'},
 {'symbol': 'SAFE', 'symbol_name': 'SAFESTORE'},
 {'symbol': 'SAIN', 'symbol_name': 'SAGE GRP.'},
 {'symbol': 'SBRY', 'symbol_name': 'SAINSBURY(J)'},
 {'symbol': 'SCT', 'symbol_name': 'SAVILLS'},
 {'symbol': 'SDP', 'symbol_name': 'SCHRODER ASIA'},
 {'symbol': 'SDR', 'symbol_name': 'SCHRODER ORIENT'},
 {'symbol': 'SEIT', 'symbol_name': 'SCHRODERS'},
 {'symbol': 'SEQI', 'symbol_name': 'SCOT.AMER.INV.'},
 {'symbol': 'SGE', 'symbol_name': 'SCOTTISH MORT'},
 {'symbol': 'SGRO', 'symbol_name': 'SDCL ENERGY EF.'},
 {'symbol': 'SHC', 'symbol_name': 'SEGRO'},
 {'symbol': 'SHED', 'symbol_name': 'SENIOR'},
 {'symbol': 'SHEL', 'symbol_name': 'SEQUOIA ECO'},
 {'symbol': 'SKG', 'symbol_name': 'SERCO GRP.'},
 {'symbol': 'SMDS', 'symbol_name': 'SEVERN TRENT'},
 {'symbol': 'SMIN', 'symbol_name': 'SHAFTESBURY CAP'},
 {'symbol': 'SMT', 'symbol_name': 'SHELL PLC'},
 {'symbol': 'SMWH', 'symbol_name': 'SIRIUS R E.'},
 {'symbol': 'SN.', 'symbol_name': 'SMITH&NEPHEW'},
 {'symbol': 'SNR', 'symbol_name': 'SMITH(DS)'},
 {'symbol': 'SOI', 'symbol_name': 'SMITHS GROUP'},
 {'symbol': 'SONG', 'symbol_name': 'SMITHSON INVEST'},
 {'symbol': 'SPI', 'symbol_name': 'SMURFIT KAP.'},
 {'symbol': 'SPT', 'symbol_name': 'SOFTCAT'},
 {'symbol': 'SPX', 'symbol_name': 'SPECTRIS'},
 {'symbol': 'SRE', 'symbol_name': 'SPIRAX-SARCO'},
 {'symbol': 'SRP', 'symbol_name': 'SPIRE HEALTH'},
 {'symbol': 'SSE', 'symbol_name': 'SPIRENT'},
 {'symbol': 'SSON', 'symbol_name': 'SSE'},
 {'symbol': 'SSPG', 'symbol_name': 'SSP GRP'},
 {'symbol': 'STAN', 'symbol_name': "ST.JAMES'S PLAC"},
 {'symbol': 'STEM', 'symbol_name': 'STAND.CHART.'},
 {'symbol': 'STJ', 'symbol_name': 'STHREE'},
 {'symbol': 'SUPR', 'symbol_name': 'SUPERMARKET INC'},
 {'symbol': 'SVS', 'symbol_name': 'SYNCONA'},
 {'symbol': 'SVT', 'symbol_name': 'SYNTHOMER'},
 {'symbol': 'SXS', 'symbol_name': 'TARGET HEALTHC.'},
 {'symbol': 'SYNC', 'symbol_name': 'TATE & LYLE'},
 {'symbol': 'SYNT', 'symbol_name': 'TAYLOR WIMPEY'},
 {'symbol': 'TATE', 'symbol_name': 'TBC BANK GP'},
 {'symbol': 'TBCG', 'symbol_name': 'TELECOM PLUS'},
 {'symbol': 'TCAP', 'symbol_name': 'TEMPLE BAR'},
 {'symbol': 'TEM', 'symbol_name': 'TEMPLETON EMRG.'},
 {'symbol': 'TEP', 'symbol_name': 'TESCO'},
 {'symbol': 'TFIF', 'symbol_name': 'TI FLUID'},
 {'symbol': 'THRG', 'symbol_name': 'TP ICAP GRP.'},
 {'symbol': 'THRL', 'symbol_name': 'TR PROP.INV.TST'},
 {'symbol': 'TIFS', 'symbol_name': 'TRAINLINE'},
 {'symbol': 'TLW', 'symbol_name': 'TRAVIS PERKINS.'},
 {'symbol': 'TMPL', 'symbol_name': 'TRITAX BIG BOX'},
 {'symbol': 'TPK', 'symbol_name': 'TRITAX EURO. £'},
 {'symbol': 'TRIG', 'symbol_name': 'TUI AG'},
 {'symbol': 'TRN', 'symbol_name': 'TULLOW OIL'},
 {'symbol': 'TRY', 'symbol_name': 'TWENTYFOUR INC'},
 {'symbol': 'TSCO', 'symbol_name': 'TYMAN'},
 {'symbol': 'TUI', 'symbol_name': 'UK COMM PROP'},
 {'symbol': 'TW.', 'symbol_name': 'UNILEVER'},
 {'symbol': 'TYMN', 'symbol_name': 'UNITE GROUP'},
 {'symbol': 'UKCM', 'symbol_name': 'URBAN LO'},
 {'symbol': 'UKW', 'symbol_name': 'UTD. UTILITIES'},
 {'symbol': 'ULVR', 'symbol_name': 'VANQUIS BANKING'},
 {'symbol': 'UTG', 'symbol_name': 'VESUVIUS'},
 {'symbol': 'UU.', 'symbol_name': 'VICTREX'},
 {'symbol': 'VANQ', 'symbol_name': 'VIDENDUM PLC'},
 {'symbol': 'VCT', 'symbol_name': 'VIETNAM ENT'},
 {'symbol': 'VEIL', 'symbol_name': 'VINACAP VIET OP'},
 {'symbol': 'VID', 'symbol_name': 'VIRGIN MONEY UK'},
 {'symbol': 'VMUK', 'symbol_name': 'VISTRY GRP'},
 {'symbol': 'VOD', 'symbol_name': 'VODAFONE GRP.'},
 {'symbol': 'VOF', 'symbol_name': 'VOLUTION'},
 {'symbol': 'VSVS', 'symbol_name': 'WAG PAYMENT'},
 {'symbol': 'VTY', 'symbol_name': 'WAREHOUSE REIT'},
 {'symbol': 'WEIR', 'symbol_name': 'WATCHES SWITZ'},
 {'symbol': 'WG.', 'symbol_name': 'WEIR GRP.'},
 {'symbol': 'WHR', 'symbol_name': 'WETHERSPOON(JD)'},
 {'symbol': 'WIZZ', 'symbol_name': 'WH SMITH'},
 {'symbol': 'WKP', 'symbol_name': 'WHITBREAD'},
 {'symbol': 'WOSG', 'symbol_name': 'WITAN INV TST'},
 {'symbol': 'WPP', 'symbol_name': 'WIZZ AIR'},
 {'symbol': 'WPS', 'symbol_name': 'WOOD GRP(J)'},
 {'symbol': 'WTAN', 'symbol_name': 'WORKSPACE GRP.'},
 {'symbol': 'WTB', 'symbol_name': 'WORLDWIDE HC'},
 {'symbol': 'WWH', 'symbol_name': 'WPP'}]


def symbol_name_prompt(query,symbols):
    symbol_name_prompt = """"
            RESPONSE FORMAT =
        
             {
             "symbol_name": "YourSymbolName"
             }
             """
    symbol_names = '\n'.join([f"'{data['symbol_name']}'" for data in symbols])
    symbol_name = f"""

             

             QUESTION: {query}

             You are building a stock trading bot to assistant traders on company shares they want to trade on. From the user query, extract the symbol name mentioned.
             Possible symbol names are, the symbol name is usually the comany name in the query:
             Here is a list of the possible symbole names:{symbol_names}
             
             {symbol_name_prompt}
             
             What is the symbol name mentioned in the query? Provide the response with the RESPONSE FORMAT as dictionary.
            return blank response if information not found. Your input can be a json and test extract the required information from the text
            if not provided extract from the json.
             """
    return symbol_name


def symbol_prompt_extract(query, symbols):
    symbol_prompt = """"
            RESPONSE FORMAT =
             {
             "symbol": "YourSymbol"
             }
            """
    symbols = '\n'.join([f"'{data['symbol_name']}' - '{data['symbol']}'" for data in symbols])

    symbol = f"""

             You are building a stock trading bot to assistant traders on company shares they want to trade on. Using the symbol name (company name) provided in the query, provide the symbol by searching through the list.
            In the list the symbol and symbol name are in a dictionary. Go through all the dictionaries in the list to identify the symbol that represents the symbol name in the query.
            The list is contained in {symbols}
             
             
             
             {symbol_prompt}

             QUESTION: {query}

             What is the symbol mentioned in the query? Provide the response with the RESPONSE FORMAT as dictionary..
            return blank response if information not found. Your input can be a json and test extract the required information from the text
            if not provided extract from the json.
             """
    return symbol

def type_prompt(query):
    type_prompt = """
        RESPONSE FORMAT =
        {
            "type": "YourIndicatorType"
        }
    """
    type_question = f"""
        You are building a stock trading bot to assist traders in their stock dealings. From the user query, extract the strategy details including the type of indicator used. Output the result in the given response format as a dictionary. The output should only contain the 'type'. The response should be in the given format. 
        Examples of types include: Moving Average (MA), Exponential Moving Average (EMA), Relative Strength Index (RSI), Fibonacci Retracement, Volume (as an indicator).
        QUESTION: {query}
        What is the stock trading strategy type mentioned in the query? Provide the response with the RESPONSE FORMAT {type_prompt}
        
    """
    return type_question


def timeframe_num_prompt(query):
    timeframe_num_prompt = """
        RESPONSE FORMAT =
        {
            "timeframe_num": "Timeframe Num"
        }
    """
    timeframe_num_ = f"""
        You are building a stock trading bot to assist traders in their stock dealings. From the user query, extract the strategy details including the numeric timeframe mentioned. 
        Output the result in the given response format as a dictionary. 
        The output should only contain the 'timeframe_num'. The response should be in the given format {timeframe_num_prompt}
        QUESTION: {query}
        What is the stock trading strategy timeframe (numeric value) mentioned in the query? Provide the response with the RESPONSE FORMAT {timeframe_num_prompt}.
    """
    return timeframe_num_


def timeframe_prompt(query):
    timeframe_prompt = """
        RESPONSE FORMAT =
        {
            "timeframe": "YourTimeframe"
        }
    """
    timeframe= f"""
        You are building a stock trading bot to assist traders in their stock dealings. From the user query, extract the strategy details including the timeframe mentioned (e.g., day, week, month represented as D, W, M respectively). Output the result in the given response format as a dictionary. The output should only contain the 'timeframe'. The response should be in the given format.
        QUESTION: {query}
        What is the timeframe for the stock trading information mentioned in the query? Provide the response with the RESPONSE FORMAT as a dictionary {timeframe_prompt}.
    """
    return timeframe


def buy_condition_prompt(query):
    buy_condition_prompt = """
        RESPONSE FORMAT =
        {
            "buy_condition": "YourBuyCondition"
        }
    """
    buy_condition = f"""
        You are building a stock trading bot to assist traders in their stock dealings. From the user query, extract the strategy details including the buy condition mentioned. Output the result in the given response format as a dictionary. The output should only contain the 'buy_condition'. The response should be in the given format.
        QUESTION: {query}
        What is the stock trading strategy buy condition mentioned in the query? Provide the response with the RESPONSE FORMAT 
        {buy_condition_prompt}
    """
    return buy_condition


def sell_condition_prompt(query):
    sell_condition_prompt = """
        RESPONSE FORMAT =
        {
            "sell_condition": "YourSellCondition"
        }
        """
    sell_condition= f"""
        You are building a stock trading bot to assist traders in their stock dealings. From the user query, extract the strategy details including the sell condition mentioned. Output the result in the given response format as a dictionary. The output should only contain the 'sell_condition'. The response should be in the given format.
        QUESTION: {query}
        What is the stock trading strategy sell condition mentioned in the query? Provide the response with the RESPONSE FORMAT {sell_condition_prompt}
    """
    return sell_condition


def algorithm_modules_prompt(query):
    algorithm_modules_prompt = """
    RESPONSE FORMAT:
    {
        "algorithm_module": "YourAlgorithmModule"
    }
    """

    algorithm_modules = f"""
    You are building a stock trading bot to assistant traders on company shares they want to trade on. Extract the stock trading strategy based on popular Algorithmic Modules. The common algorithm modules in stock traging are:
    1. Moving Average Crossover
    2. Mean Reversion
    3. Momentum stock trading
    4. Pairs stock trading
    6. Market Making
    7. Trend Following
    8. Sentiment Analysis
    10. High-Frequency stock trading (HFT)
    11. Breakout stock trading
    12. Swing stock trading
    13. Volume-Weighted Average Price (VWAP)
    14. Time-Weighted Average Price (TWAP)
    16. Dollar Cost Averaging
    17. Relative Strength Index (RSI)
    18. Bollinger Bands
    19. Fibonacci Retracement
    20. Ich

    {algorithm_modules_prompt}

    QUESTION: {query}

    What Algorithmic Module is mentioned in the query? Provide the response with the RESPONSE FORMAT as a dictionary.
    """
    return algorithm_modules



def quantity_prompt(query):
    quantity_prompt = """"
            RESPONSE FORMAT =
             
             {
             "quantity": YourQuantity
             }
             """
    quantity = f"""

             You are building a stock trading bot to assistant traders on company shares they want to trade on. From the user query, extract the quantity mentioned.

             {quantity_prompt}

             QUESTION: {query}

             What is the quantity mentioned in the query? Provide the response with the RESPONSE FORMAT as dictionary..
            return blank response if information not found. Your input can be a json and test extract the required information from the text
            if not provided extract from the json.
             """
    return quantity



def response(query):
    os.environ["OPENAI_API_KEY"]= openapi_key
    openai.api_key=openapi_key
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role":"system", "content":f"{query}"}],
        temperature=0.5,
        max_tokens=1000,   
    )
    content = response['choices'][0]['message']['content']
    #print("Raw Content:", content)
    # Remove leading/trailing newlines and extra spaces for clean JSON content
    #content_strip = content.strip()

    # Parse the JSON content
    #content_json = json.loads(content)

    # Print the extracted content in JSON format
    return content




def create_trade_dict(query):

    # Extract individual components
    try:
        symbol_name = json.loads(response(symbol_name_prompt(query,symbols)))
    except json.JSONDecodeError:
        symbol_name = None

    try:
        symbol_result = json.loads(response(symbol_prompt_extract(query,symbols)))
    except json.JSONDecodeError:
        symbol_result = None

    # Extract type prompt
    try:
        type_result = json.loads(response(type_prompt(query)))
    except json.JSONDecodeError:
        type_result = None

    # Extract timeframe_num prompt
    try:
        timeframe_num_result = json.loads(response(timeframe_num_prompt(query)))
    except json.JSONDecodeError:
        timeframe_num_result = None

    # Extract timeframe prompt
    try:
        
        timeframe_result = json.loads(response(timeframe_prompt(query)))
    except json.JSONDecodeError:
        timeframe_result = None

    # Extract buy_condition prompt
    try:
       buy_condition_result = json.loads(response(buy_condition_prompt(query)))
    except json.JSONDecodeError:
        buy_condition_result = None

    # Extract sell_condition prompt
    try:
        sell_condition_result = json.loads(response(sell_condition_prompt(query)))
    except json.JSONDecodeError:
        sell_condition_result = None

    try:
        quantity_result = json.loads(response(quantity_prompt(query)))
    except json.JSONDecodeError:
        quantity_result = None

    try:
        algorithm_result = json.loads(response(algorithm_modules_prompt(query)))
    except json.JSONDecodeError:
        algorithm_result = None

    # Replace None with "null"
    symbol_name = symbol_name["symbol_name"] if symbol_name else "null"
    symbol = symbol_result["symbol"] if symbol_result else "null"
    type_ = type_result["type"] if type_result else "null"
    timeframe_num = timeframe_num_result["timeframe_num"] if timeframe_num_result else "null"
    timeframe = timeframe_result["timeframe"] if timeframe_result else "null"
    buy_condition = buy_condition_result["buy_condition"] if buy_condition_result else "null"
    sell_condition = sell_condition_result["sell_condition"] if sell_condition_result else "null"
    algorithm_module= algorithm_result["algorithm_module"] if algorithm_result else "null"
    quantity = quantity_result["quantity"] if quantity_result else "null"
    print(symbol_name)
    # Combine results into the final dictionary
    trade_dict = {
        "symbol_name": symbol_name,
        "symbol": symbol,
        "strategy": {
            "type": type_,
            "timeframe_num": timeframe_num,
            "timeframe": timeframe,
            "buy_condition": buy_condition,
            "sell_condition": sell_condition
        },
        "algorithm_module":algorithm_module,
        "quantity": quantity
    }

    return trade_dict


#print(create_trade_dict(query))



