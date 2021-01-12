# import theater_module # 모듈 가져오는 법1)
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv #모듈 가져오는 법2)
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

from theater_module import * #모듈 가져오는 법3)
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 필요한 함수만 가져오는 법
price(3)
price_morning(4)