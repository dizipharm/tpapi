from src.commons.utils import field_setter
from src.models.base_model import Field, BaseModel


class Product(BaseModel):
    TABLE = "Product"
    #Need to add the fields to be excluded from hashing

    fields = {
        "id": Field(key=True, type="str", setter=field_setter),
        "trading_party_id": Field(key=False, type="int", setter=field_setter),
        "brand_name": Field(key=True, type="str", setter=field_setter),
        "product_name": Field(key=True, type="str", setter=field_setter),
        "product_desription": Field(key=True, type="str", setter=field_setter),
        "container_type_id": Field(key=True, type="int", setter=field_setter),
        "product_code": Field(key=True, type="str", setter=field_setter),
        "product_image_url": Field(key=True, type="str", setter=field_setter),
        "product_code_type": Field(key=True, type="str", setter=field_setter),
        "source_system": Field(key=True, type="str", setter=field_setter),
        "product_category_id": Field(key=True, type="int", setter=field_setter),
        "item_dimensions_id": Field(key=True, type="int", setter=field_setter),
        "dosage_form_id": Field(key=True, type="int", setter=field_setter),
        "container_size": Field(key=True, type="str", setter=field_setter),
        "controlled_drug": Field(key=True, type="int", setter=field_setter),
        "manufacturer": Field(key=True, type="str", setter=field_setter),
        "brand_owner": Field(key=True, type="str", setter=field_setter),
        "labler_name": Field(key=True, type="str", setter=field_setter),
        "proprietary_name": Field(key=True, type="str", setter=field_setter),
        "rx_nonproprietary_name": Field(key=True, type="str", setter=field_setter),
        "market_holder_name": Field(key=True, type="str", setter=field_setter),
        "product_ndc": Field(key=True, type="str", setter=field_setter),
        "created_datetime": Field(key=True, type="str", setter=field_setter),
        "activation_date": Field(key=True, type="str", setter=field_setter),
        "deactivation_date": Field(key=True, type="str", setter=field_setter),
        "last_updated_datetime": Field(key=True, type="str", setter=field_setter),
        "is_active": Field(key=True, type="int", setter=field_setter),
    }

