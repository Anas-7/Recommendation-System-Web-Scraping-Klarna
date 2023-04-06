HOMEPAGE_URL = "https://www.klarna.com/us/"

SHOPPING_CATEGORY_CLASS = "BaseLink__StyledLink-sc-1rp08tz-0 kKRApF Link__StyledLink-sc-1ojsrhb-0 kIbLAR InlineNav__StyledLink-sc-evjeut-3 kemcvW menu-item"
SHOPPING_CATEGORY_CLASS = SHOPPING_CATEGORY_CLASS.split(" ")
new_str = ""
for i in SHOPPING_CATEGORY_CLASS:
    new_str += (i+".")
SHOPPING_CATEGORY_CLASS = new_str[:-1]
