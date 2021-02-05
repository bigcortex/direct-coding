from enum import Enum


class ProductType(Enum):
    Digital = 1
    Package = 2
    Promotional = 3


class Product:

    def __init__(self, type_of_product, number_of_assets, discount, free):
        self._type = type_of_product
        self._number_of_assets = number_of_assets
        self._discount = discount
        self._free = free

    def price(self):
        if self._type == ProductType.Digital:
            return self._base_price()
        if self._type == ProductType.Package:
            if self._number_of_assets > 2:
                return self._base_price() * self._number_of_assets * self._discount_factor()
            else:
                return max([100, self._base_price() * self._number_of_assets])
        if self._type == ProductType.Promotional:
            if self._free:
                return 0
            else:
                return self._calculate_base_price_with_discount(self._discount)

        raise ValueError("should be unreachable")

    def _calculate_base_price_with_discount(self, discount):
        return max([500, self._base_price() - self._base_price() * discount/100.0])

    def _discount_factor(self):
        return 0.9

    def _base_price(self):
        return 1000
