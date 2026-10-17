from pydantic import BaseModel  # type: ignore[reportMissingImports]
from typing import Optional, List, Union


# Nested model ka matlab: ek Pydantic model ke field ka type
# koi doosra Pydantic model hona.
#
# Pydantic input dictionary ko validate karke automatically nested
# Address object bana dega.
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    # Address dena optional hai. Agar address na mile, value None hogi.
    # Agar dictionary mile, to Pydantic us dictionary ko Address model me
    # convert karke validate karega.
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    # Employee ke paas Company object ho sakta hai, ya company missing hone
    # par None ho sakta hai.
    company: Optional[Company] = None


class TextContent(BaseModel):
    # `type` ka default value "text" hai. Input me type na dene par
    # Pydantic automatically type="text" set karega.
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    # ImageContent me type na dene par type="image" set hoga.
    type: str = "image"
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    # `sections` ek list hai.
    # List ke har item ko TextContent ya ImageContent hona chahiye.
    #
    # Union ka matlab: ek value diye gaye types me se kisi ek type ki ho sakti
    # hai. Pydantic har item ko validate karke appropriate nested model banata hai.
    sections: List[Union[TextContent, ImageContent]]


# ============================================================
# Deeply nested models
# ============================================================
#
# Yahan nesting ka structure kuch aisa hai:
#
# Organization
#   └── head_quarters: AddressWithCity
#         └── city: City
#               └── state: State
#                     └── country: Country
#
# Matlab ek Organization ke andar address, address ke andar city,
# city ke andar state aur state ke andar country hai.
class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    # `country` simple string nahi, balki Country model ka object hoga.
    country: Country


class City(BaseModel):
    name: str
    # City ke andar poora State model nested hai.
    state: State


class AddressWithCity(BaseModel):
    street: str
    # Address ke andar City model nested hai. City ke andar State aur
    # State ke andar Country model hoga.
    city: City
    postal_code: str


class Organization(BaseModel):
    name: str
    # Organization ka head office AddressWithCity model hoga.
    head_quarters: AddressWithCity

    # `brances` me multiple AddressWithCity objects ki list aa sakti hai.
    # Har dictionary item ko Pydantic AddressWithCity object me convert karega.
    # Note: field ka naam existing code ke hisaab se `brances` hai.
    brances: List[AddressWithCity] = []


# ============================================================
# Data kaise nested models me convert hota hai
# ============================================================
#
# organization_data me dictionaries hain, lekin Organization banne ke baad
# Pydantic inhe nested model objects me convert aur validate karta hai:
#
# organization = Organization(**organization_data)
#
# organization.head_quarters.city.state.country.name
# is expression se deeply nested Country ka name mil sakta hai.
#
# Agar kisi required field ka naam missing ho, ya value ka type invalid ho,
# to Pydantic ValidationError raise karega.
#
# Example input ka shape:
#
# organization_data = {
#     "name": "Tech Company",
#     "head_quarters": {
#         "street": "MG Road",
#         "city": {
#             "name": "Delhi",
#             "state": {
#                 "name": "Delhi",
#                 "country": {
#                     "name": "India",
#                     "code": "IN",
#                 },
#             },
#         },
#         "postal_code": "110001",
#     },
#     "brances": [],
# }

