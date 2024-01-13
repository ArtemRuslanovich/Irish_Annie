import random
import string

class CouponManager:
    def __init__(self):
        self.used_coupons = set()

    def generate_coupon(self):
        coupon_code = self._generate_random_code()
        while coupon_code in self.used_coupons:
            coupon_code = self._generate_random_code()

        return coupon_code

    def use_coupon(self, coupon_code):
        self.used_coupons.add(coupon_code)

    def is_coupon_used(self, coupon_code):
        return coupon_code in self.used_coupons

    def _generate_random_code(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

coupon_manager = CouponManager()