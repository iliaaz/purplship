""" DHL Native Types """
from enum import Enum, Flag


class Dimension(Enum):
    CM = "C"
    IN = "I"


class WeightUnit(Enum):
    KG = "K"
    LB = "L"


class DeliveryType(Enum):
    door_to_door = "DD"
    door_to_airport = "DA"
    airport_to_airport = "AA"
    door_to_door_c = "DC"


class DCTPackageType(Enum):
    flyer_smalls = "FLY"
    parcels_conveyables = "COY"
    non_conveyables = "NCY"
    pallets = "PAL"
    double_pallets = "DBL"
    parcels = "BOX"

    """ Unified Packaging type mapping """
    sm = flyer_smalls
    box = parcels
    pc = non_conveyables
    pal = pallets


class NetworkType(Enum):
    both_time_and_day_definite = "AL"
    day_definite = "DD"
    time_definite = "TD"


class PackageType(Flag):
    jumbo_document = "BD"
    jumbo_parcel = "BP"
    customer_provided = "CP"
    document = "DC"
    dhl_flyer = "DF"
    domestic = "DM"
    express_document = "ED"
    dhl_express_envelope = "EE"
    freight = "FR"
    jumbo_box = "JB"
    jumbo_junior_document = "JD"
    junior_jumbo_box = "JJ"
    jumbo_junior_parcel = "JP"
    other_dhl_packaging = "OD"
    parcel = "PA"
    your_packaging = "YP"

    """ Unified Packaging type mapping """
    sm = document
    box = parcel
    pc = your_packaging
    pal = freight


class Product(Enum):
    logistics_services = "LOGISTICS SERVICES"
    domestic_express_12_00_doc = "DOMESTIC EXPRESS 12:00 DOC"
    b2_c_doc = "B2C DOC"
    b2_c_nondoc = "B2C NONDOC"
    jetline = "JETLINE"
    sprintline = "SPRINTLINE"
    express_easy_doc = "EXPRESS EASY DOC"
    express_easy_nondoc = "EXPRESS EASY NONDOC"
    europack_doc = "EUROPACK DOC"
    auto_reversals = "AUTO REVERSALS"
    breakbulk_express_doc = "BREAKBULK EXPRESS DOC"
    medical_express_doc = "MEDICAL EXPRESS DOC"
    express_worldwide_doc = "EXPRESS WORLDWIDE DOC"
    express_9_00_nondoc = "EXPRESS 9:00 NONDOC"
    freight_worldwide_nondoc = "FREIGHT WORLDWIDE NONDOC"
    domestic_economy_select_doc = "DOMESTIC ECONOMY SELECT DOC"
    economy_select_nondoc = "ECONOMY SELECT NONDOC"
    domestic_express_9_00_doc = "DOMESTIC EXPRESS 9:00 DOC"
    jumbo_box_nondoc = "JUMBO BOX NONDOC"
    express_9_00_doc = "EXPRESS 9:00 DOC"
    express_10_30_doc = "EXPRESS 10:30 DOC"
    express_10_30_nondoc = "EXPRESS 10:30 NONDOC"
    domestic_express_doc = "DOMESTIC EXPRESS DOC"
    domestic_express_10_30_doc = "DOMESTIC EXPRESS 10:30 DOC"
    express_worldwide_nondoc = "EXPRESS WORLDWIDE NONDOC"
    medical_express_nondoc = "MEDICAL EXPRESS NONDOC"
    globalmail_business_doc = "GLOBALMAIL BUSINESS DOC"
    same_day_doc = "SAME DAY DOC"
    express_12_00_doc = "EXPRESS 12:00 DOC"
    express_worldwide_ecx_doc = "EXPRESS WORLDWIDE DOC"
    europack_nondoc = "EUROPACK NONDOC"
    economy_select_doc = "ECONOMY SELECT DOC"
    express_envelope_doc = "EXPRESS ENVELOPE DOC"
    express_12_00_nondoc = "EXPRESS 12:00 NONDOC"
    destination_charges = "Destination Charges"


class ProductCode(Enum):
    logistics_services = "0"
    domestic_express_12_00_doc = "1"
    b2_c_doc = "2"
    b2_c_nondoc = "3"
    jetline = "4"
    sprintline = "5"
    express_easy_doc = "7"
    express_easy_nondoc = "8"
    europack_doc = "9"
    auto_reversals = "A"
    breakbulk_express_doc = "B"
    medical_express_doc = "C"
    express_worldwide_doc = "D"
    express_9_00_nondoc = "E"
    freight_worldwide_nondoc = "F"
    domestic_economy_select_doc = "G"
    economy_select_nondoc = "H"
    domestic_express_9_00_doc = "I"
    jumbo_box_nondoc = "J"
    express_9_00_doc = "K"
    express_10_30_doc = "L"
    express_10_30_nondoc = "M"
    domestic_express_doc = "N"
    domestic_express_10_30_doc = "O"
    express_worldwide_nondoc = "P"
    medical_express_nondoc = "Q"
    globalmail_business_doc = "R"
    same_day_doc = "S"
    express_12_00_doc = "T"
    express_worldwide_ecx_doc = "U"
    europack_nondoc = "V"
    economy_select_doc = "W"
    express_envelope_doc = "X"
    express_12_00_nondoc = "Y"
    destination_charges = "Z"


class PayorType(Enum):
    sender = "S"
    recipient = "R"
    third_party = "T"


class ServiceCode(Flag):
    logistics_services = "0A"
    mailroom_management = "0B"
    pallet_administration = "0C"
    warehousing = "0D"
    express_logistics_centre = "0E"
    strategic_parts_centre = "0F"
    local_distribution_centre = "0G"
    terminal_handling = "0H"
    cross_docking = "0I"
    inventory_management = "0J"
    loading_unloading = "0K"
    product_kitting = "0L"
    priority_account_desk = "0M"
    document_archiving = "0N"
    saturday_delivery = "AA"
    saturday_pickup = "AB"
    holiday_delivery = "AC"
    holiday_pickup = "AD"
    domestic_saturday_delivery = "AG"
    standard = "BA"
    globalmail_item = "BB"
    letter = "BC"
    packet = "BD"
    letter_plus = "BE"
    packet_plus = "BF"
    elevated_risk = "CA"
    restricted_destination = "CB"
    security_validation = "CC"
    secure_protection = "CD"
    proof_of_identity = "CE"
    secure_storage = "CF"
    diplomatic_material = "CG"
    smart_sensor = "CH"
    visa_program = "CI"
    onboard_courier = "CJ"
    secure_safebox = "CK"
    smart_sentry = "CL"
    split_duties_and_tax = "DC"
    duties_and_taxes_paid = "DD"
    receiver_paid = "DE"
    duties_and_taxes_unpaid = "DS"
    import_billing = "DT"
    importer_of_record = "DU"
    go_green_carbon_neutral = "EA"
    go_green_carbon_footprint = "EB"
    go_green_carbon_estimate = "EC"
    fuel_surcharge_b = "FB"
    fuel_surcharge_c = "FC"
    fuel_surcharge_f = "FF"
    smartphone_box = "GA"
    laptop_box = "GB"
    bottle_box = "GC"
    repacking = "GD"
    tablet_box = "GE"
    filler_material = "GF"
    packaging = "GG"
    diplomatic_bag = "GH"
    pallet_box = "GI"
    lock_box = "GJ"
    lithium_ion_pi965_section_ii = "HB"
    dry_ice_un1845 = "HC"
    lithium_ion_pi965_966_section_ii = "HD"
    dangerous_goods = "HE"
    perishable_cargo = "HG"
    excepted_quantity = "HH"
    spill_cleaning = "HI"
    consumer_commodities = "HK"
    limited_quantities_adr = "HL"
    lithium_metal_pi969_section_ii = "HM"
    adr_load_exemption = "HN"
    lithium_ion_pi967_section_ii = "HV"
    lithium_metal_pi970_section_ii = "HW"
    biological_un3373 = "HY"
    extended_liability = "IB"
    contract_insurance = "IC"
    shipment_insurance = "II"
    delivery_notification = "JA"
    pickup_notification = "JC"
    proactive_tracking = "JD"
    performance_reporting = "JE"
    prealert_notification = "JY"
    change_of_billing = "KA"
    cash_on_delivery = "KB"
    printed_invoice = "KD"
    waybill_copy = "KE"
    import_paperwork = "KF"
    payment_on_pickup = "KY"
    shipment_intercept = "LA"
    shipment_redirect = "LC"
    storage_at_facility = "LE"
    cold_storage = "LG"
    specific_routing = "LH"
    service_recovery = "LV"
    alternative_address = "LW"
    hold_for_collection = "LX"
    address_correction_a = "MA"
    address_correction_b = "MB"
    neutral_delivery = "NN"
    remote_area_pickup = "OB"
    remote_area_delivery_c = "OC"
    out_of_service_area = "OE"
    remote_area_delivery_o = "OO"
    shipment_preparation = "PA"
    shipment_labeling = "PB"
    shipment_consolidation = "PC"
    relabeling_data_entry = "PD"
    preprinted_waybill = "PE"
    piece_labelling = "PS"
    data_staging_03 = "PT"
    data_staging_06 = "PU"
    data_staging_12 = "PV"
    data_staging_24 = "PW"
    standard_pickup = "PX"
    scheduled_pickup = "PY"
    dedicated_pickup = "QA"
    early_pickup = "QB"
    late_pickup = "QD"
    residential_pickup = "QE"
    loading_waiting = "QF"
    bypass_injection = "QH"
    direct_injection = "QI"
    drop_off_at_facility = "QY"
    delivery_signature = "SA"
    content_signature = "SB"
    named_signature = "SC"
    adult_signature = "SD"
    contract_signature = "SE"
    alternative_signature = "SW"
    no_signature_required = "SX"
    dedicated_delivery = "TA"
    early_delivery = "TB"
    time_window_delivery = "TC"
    evening_delivery = "TD"
    delivery_on_appointment = "TE"
    return_undeliverable = "TG"
    swap_delivery = "TH"
    unloading_waiting = "TJ"
    residential_delivery = "TK"
    repeat_delivery = "TN"
    alternative_date = "TT"
    no_partial_delivery = "TU"
    service_point_24_7 = "TV"
    pre_9_00 = "TW"
    pre_10_30 = "TX"
    pre_12_00 = "TY"
    thermo_packaging = "UA"
    ambient_vialsafe = "UB"
    ambient_non_insulated = "UC"
    ambient_insulated = "UD"
    ambient_extreme = "UE"
    chilled_box_s = "UF"
    chilled_box_m = "UG"
    chilled_box_l = "UH"
    frozen_no_ice_s = "UI"
    frozen_no_ice_m = "UJ"
    frozen_no_ice_l = "UK"
    frozen_ice_sticks_s = "UL"
    frozen_ice_sticks_m = "UM"
    frozen_ice_sticks_l = "UN"
    frozen_ice_plates_s = "UO"
    frozen_ice_plates_m = "UP"
    frozen_ice_plates_l = "UQ"
    combination_no_ice = "UR"
    combination_dry_ice = "US"
    frozen_ice_sticks_e = "UT"
    frozen_ice_plates_e = "UV"
    customer_tcp_1 = "UW"
    thermo_accessories = "VA"
    absorbent_sleeve = "VB"
    cooland_wrap = "VC"
    dry_ice_supplies = "VD"
    pressure_bag_s = "VE"
    pressure_bag_m = "VF"
    pressure_bag_l = "VG"
    informal_clearance = "WA"
    formal_clearance = "WB"
    payment_deferment = "WC"
    clearance_authorization = "WD"
    multiline_entry = "WE"
    post_clearance_modification = "WF"
    handover_to_broker = "WG"
    physical_intervention = "WH"
    bio_phyto_veterinary_controls = "WI"
    obtaining_permits_and_licences = "WJ"
    bonded_storage = "WK"
    bonded_transit_documents = "WL"
    temporary_import_export = "WM"
    under_bond_guarantee = "WN"
    export_declaration = "WO"
    exporter_validation = "WP"
    certificate_of_origin = "WQ"
    document_translation = "WR"
    personal_effects = "WS"
    paperless_trade = "WY"
    import_export_taxes = "XB"
    unrecoverable_origin_tax = "XC"
    quarantine_inspection = "XD"
    merchandise_process = "XE"
    domestic_postal_tax = "XF"
    tier_two_tax = "XG"
    tier_three_tax = "XH"
    import_penalty = "XI"
    cargo_zone_process = "XJ"
    import_export_duties = "XX"
    premium_09_00 = "Y1"
    premium_10_30 = "Y2"
    premium_12_00 = "Y3"
    over_sized_piece_b = "YB"
    over_handled_piece_c = "YC"
    multipiece_shipment = "YE"
    over_weight_piece_f = "YF"
    over_sized_piece_g = "YG"
    over_handled_piece_h = "YH"
    premium_9_00_i = "YI"
    premium_10_30_j = "YJ"
    premium_12_00_k = "YK"
    paket_shipment = "YV"
    breakbulk_mother = "YW"
    breakbulk_baby = "YX"
    over_weight_piece_y = "YY"
    customer_claim = "ZA"
    damage_compensation = "ZB"
    loss_compensation = "ZC"
    customer_rebate = "ZD"
    e_com_discount = "ZE"

    """ Unified Option type mapping """
    insurance = shipment_insurance


class CountryRegion(Enum):
    AD = "EU"
    AE = "AP"
    AF = "AP"
    AG = "AM"
    AI = "AM"
    AL = "AP"
    AM = "AP"
    AN = "AM"
    AO = "AP"
    AR = "AM"
    AS = "AM"
    AT = "EU"
    AU = "AP"
    AW = "AM"
    AZ = "AM"
    BA = "AP"
    BB = "AM"
    BD = "AP"
    BE = "EU"
    BF = "AP"
    BG = "EU"
    BH = "AP"
    BI = "AP"
    BJ = "AP"
    BM = "AM"
    BN = "AP"
    BO = "AM"
    BR = "AM"
    BS = "AM"
    BT = "AP"
    BW = "AP"
    BY = "AP"
    BZ = "AM"
    CA = "AM"
    CD = "AP"
    CF = "AP"
    CG = "AP"
    CH = "EU"
    CI = "AP"
    CK = "AP"
    CL = "AM"
    CM = "AP"
    CN = "AP"
    CO = "AM"
    CR = "AM"
    CU = "AM"
    CV = "AP"
    CY = "AP"
    CZ = "EU"
    DE = "EU"
    DJ = "AP"
    DK = "EU"
    DM = "AM"
    DO = "AM"
    DZ = "AP"
    EC = "AM"
    EE = "EU"
    EG = "AP"
    ER = "AP"
    ES = "EU"
    ET = "AP"
    FI = "EU"
    FJ = "AP"
    FK = "EU"
    FM = "AM"
    FO = "AM"
    FR = "EU"
    GA = "AP"
    GB = "EU"
    GD = "AM"
    GE = "AM"
    GF = "AM"
    GG = "EU"
    GH = "AP"
    GI = "EU"
    GL = "AM"
    GM = "AP"
    GN = "AP"
    GP = "AM"
    GQ = "AP"
    GR = "EU"
    GT = "AM"
    GU = "AM"
    GW = "AP"
    GY = "AP"
    HK = "AP"
    HN = "AM"
    HR = "AP"
    HT = "AM"
    HU = "EU"
    IC = "EU"
    ID = "AP"
    IE = "EU"
    IL = "AP"
    IN = "AP"
    IQ = "AP"
    IR = "AP"
    IS = "EU"
    IT = "EU"
    JE = "EU"
    JM = "AM"
    JO = "AP"
    JP = "AP"
    KE = "AP"
    KG = "AP"
    KH = "AP"
    KI = "AP"
    KM = "AP"
    KN = "AM"
    KP = "AP"
    KR = "AP"
    KV = "AM"
    KW = "AP"
    KY = "AM"
    KZ = "AP"
    LA = "AP"
    LB = "AP"
    LC = "AM"
    LI = "AM"
    LK = "AP"
    LR = "AP"
    LS = "AP"
    LT = "EU"
    LU = "EU"
    LV = "EU"
    LY = "AP"
    MA = "AP"
    MC = "AM"
    MD = "AP"
    ME = "AM"
    MG = "AP"
    MH = "AM"
    MK = "AP"
    ML = "AP"
    MM = "AP"
    MN = "AP"
    MO = "AP"
    MP = "AM"
    MQ = "AM"
    MR = "AP"
    MS = "AM"
    MT = "AP"
    MU = "AP"
    MV = "AP"
    MW = "AP"
    MX = "AM"
    MY = "AP"
    MZ = "AP"
    NA = "AP"
    NC = "AP"
    NE = "AP"
    NG = "AP"
    NI = "AM"
    NL = "EU"
    NO = "EU"
    NP = "AP"
    NR = "AP"
    NU = "AP"
    NZ = "AP"
    OM = "AP"
    PA = "AM"
    PE = "AM"
    PF = "AP"
    PG = "AP"
    PH = "AP"
    PK = "AP"
    PL = "EU"
    PR = "AM"
    PT = "EU"
    PW = "AM"
    PY = "AM"
    QA = "AP"
    RE = "AP"
    RO = "EU"
    RS = "AP"
    RU = "AP"
    RW = "AP"
    SA = "AP"
    SB = "AP"
    SC = "AP"
    SD = "AP"
    SE = "EU"
    SG = "AP"
    SH = "AP"
    SI = "EU"
    SK = "EU"
    SL = "AP"
    SM = "EU"
    SN = "AP"
    SO = "AM"
    SR = "AM"
    SS = "AP"
    ST = "AP"
    SV = "AM"
    SY = "AP"
    SZ = "AP"
    TC = "AM"
    TD = "AP"
    TG = "AP"
    TH = "AP"
    TJ = "AP"
    TL = "AP"
    TN = "AP"
    TO = "AP"
    TR = "AP"
    TT = "AM"
    TV = "AP"
    TW = "AP"
    TZ = "AP"
    UA = "AP"
    UG = "AP"
    US = "AM"
    UY = "AM"
    UZ = "AP"
    VA = ""
    VC = "AM"
    VE = "AM"
    VG = "AM"
    VI = "AM"
    VN = "AP"
    VU = "AP"
    WS = "AP"
    XB = "AM"
    XC = "AM"
    XE = "AM"
    XM = "AM"
    XN = "AM"
    XS = "AP"
    XY = "AM"
    YE = "AP"
    YT = "AP"
    ZA = "AP"
    ZM = "AP"
    ZW = "AP"
