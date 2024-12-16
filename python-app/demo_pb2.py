# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\x12\x08oteldemo\"0\n\x08\x43\x61rtItem\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"C\n\x0e\x41\x64\x64ItemRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12 \n\x04item\x18\x02 \x01(\x0b\x32\x12.oteldemo.CartItem\"#\n\x10\x45mptyCartRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"!\n\x0eGetCartRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x04\x43\x61rt\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.oteldemo.CartItem\"\x07\n\x05\x45mpty\"B\n\x1aListRecommendationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0bproduct_ids\x18\x02 \x03(\t\"2\n\x1bListRecommendationsResponse\x12\x13\n\x0bproduct_ids\x18\x01 \x03(\t\"\x81\x01\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12\"\n\tprice_usd\x18\x05 \x01(\x0b\x32\x0f.oteldemo.Money\x12\x12\n\ncategories\x18\x06 \x03(\t\";\n\x14ListProductsResponse\x12#\n\x08products\x18\x01 \x03(\x0b\x32\x11.oteldemo.Product\"\x1f\n\x11GetProductRequest\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x15SearchProductsRequest\x12\r\n\x05query\x18\x01 \x01(\t\"<\n\x16SearchProductsResponse\x12\"\n\x07results\x18\x01 \x03(\x0b\x32\x11.oteldemo.Product\"X\n\x0fGetQuoteRequest\x12\"\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x11.oteldemo.Address\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.oteldemo.CartItem\"5\n\x10GetQuoteResponse\x12!\n\x08\x63ost_usd\x18\x01 \x01(\x0b\x32\x0f.oteldemo.Money\"Y\n\x10ShipOrderRequest\x12\"\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x11.oteldemo.Address\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.oteldemo.CartItem\"(\n\x11ShipOrderResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\"a\n\x07\x41\x64\x64ress\x12\x16\n\x0estreet_address\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\x10\n\x08zip_code\x18\x05 \x01(\t\"<\n\x05Money\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\x03\x12\r\n\x05nanos\x18\x03 \x01(\x05\"8\n\x1eGetSupportedCurrenciesResponse\x12\x16\n\x0e\x63urrency_codes\x18\x01 \x03(\t\"K\n\x19\x43urrencyConversionRequest\x12\x1d\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0f.oteldemo.Money\x12\x0f\n\x07to_code\x18\x02 \x01(\t\"\x90\x01\n\x0e\x43reditCardInfo\x12\x1a\n\x12\x63redit_card_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63redit_card_cvv\x18\x02 \x01(\x05\x12#\n\x1b\x63redit_card_expiration_year\x18\x03 \x01(\x05\x12$\n\x1c\x63redit_card_expiration_month\x18\x04 \x01(\x05\"_\n\rChargeRequest\x12\x1f\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x0f.oteldemo.Money\x12-\n\x0b\x63redit_card\x18\x02 \x01(\x0b\x32\x18.oteldemo.CreditCardInfo\"(\n\x0e\x43hargeResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\"L\n\tOrderItem\x12 \n\x04item\x18\x01 \x01(\x0b\x32\x12.oteldemo.CartItem\x12\x1d\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x0f.oteldemo.Money\"\xb6\x01\n\x0bOrderResult\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x1c\n\x14shipping_tracking_id\x18\x02 \x01(\t\x12&\n\rshipping_cost\x18\x03 \x01(\x0b\x32\x0f.oteldemo.Money\x12+\n\x10shipping_address\x18\x04 \x01(\x0b\x32\x11.oteldemo.Address\x12\"\n\x05items\x18\x05 \x03(\x0b\x32\x13.oteldemo.OrderItem\"S\n\x1cSendOrderConfirmationRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12$\n\x05order\x18\x02 \x01(\x0b\x32\x15.oteldemo.OrderResult\"\x9d\x01\n\x11PlaceOrderRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x15\n\ruser_currency\x18\x02 \x01(\t\x12\"\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x11.oteldemo.Address\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12-\n\x0b\x63redit_card\x18\x06 \x01(\x0b\x32\x18.oteldemo.CreditCardInfo\":\n\x12PlaceOrderResponse\x12$\n\x05order\x18\x01 \x01(\x0b\x32\x15.oteldemo.OrderResult\"!\n\tAdRequest\x12\x14\n\x0c\x63ontext_keys\x18\x01 \x03(\t\"\'\n\nAdResponse\x12\x19\n\x03\x61\x64s\x18\x01 \x03(\x0b\x32\x0c.oteldemo.Ad\"(\n\x02\x41\x64\x12\x14\n\x0credirect_url\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\":\n\x04\x46lag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"\x1e\n\x0eGetFlagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"/\n\x0fGetFlagResponse\x12\x1c\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x0e.oteldemo.Flag\"G\n\x11\x43reateFlagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"2\n\x12\x43reateFlagResponse\x12\x1c\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x0e.oteldemo.Flag\"2\n\x11UpdateFlagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\x14\n\x12UpdateFlagResponse\"\x12\n\x10ListFlagsRequest\"1\n\x11ListFlagsResponse\x12\x1c\n\x04\x66lag\x18\x01 \x03(\x0b\x32\x0e.oteldemo.Flag\"!\n\x11\x44\x65leteFlagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x12\x44\x65leteFlagResponse2\xb8\x01\n\x0b\x43\x61rtService\x12\x36\n\x07\x41\x64\x64Item\x12\x18.oteldemo.AddItemRequest\x1a\x0f.oteldemo.Empty\"\x00\x12\x35\n\x07GetCart\x12\x18.oteldemo.GetCartRequest\x1a\x0e.oteldemo.Cart\"\x00\x12:\n\tEmptyCart\x12\x1a.oteldemo.EmptyCartRequest\x1a\x0f.oteldemo.Empty\"\x00\x32}\n\x15RecommendationService\x12\x64\n\x13ListRecommendations\x12$.oteldemo.ListRecommendationsRequest\x1a%.oteldemo.ListRecommendationsResponse\"\x00\x32\xf1\x01\n\x15ProductCatalogService\x12\x41\n\x0cListProducts\x12\x0f.oteldemo.Empty\x1a\x1e.oteldemo.ListProductsResponse\"\x00\x12>\n\nGetProduct\x12\x1b.oteldemo.GetProductRequest\x1a\x11.oteldemo.Product\"\x00\x12U\n\x0eSearchProducts\x12\x1f.oteldemo.SearchProductsRequest\x1a .oteldemo.SearchProductsResponse\"\x00\x32\x9e\x01\n\x0fShippingService\x12\x43\n\x08GetQuote\x12\x19.oteldemo.GetQuoteRequest\x1a\x1a.oteldemo.GetQuoteResponse\"\x00\x12\x46\n\tShipOrder\x12\x1a.oteldemo.ShipOrderRequest\x1a\x1b.oteldemo.ShipOrderResponse\"\x00\x32\xab\x01\n\x0f\x43urrencyService\x12U\n\x16GetSupportedCurrencies\x12\x0f.oteldemo.Empty\x1a(.oteldemo.GetSupportedCurrenciesResponse\"\x00\x12\x41\n\x07\x43onvert\x12#.oteldemo.CurrencyConversionRequest\x1a\x0f.oteldemo.Money\"\x00\x32O\n\x0ePaymentService\x12=\n\x06\x43harge\x12\x17.oteldemo.ChargeRequest\x1a\x18.oteldemo.ChargeResponse\"\x00\x32\x62\n\x0c\x45mailService\x12R\n\x15SendOrderConfirmation\x12&.oteldemo.SendOrderConfirmationRequest\x1a\x0f.oteldemo.Empty\"\x00\x32\\\n\x0f\x43heckoutService\x12I\n\nPlaceOrder\x12\x1b.oteldemo.PlaceOrderRequest\x1a\x1c.oteldemo.PlaceOrderResponse\"\x00\x32\x42\n\tAdService\x12\x35\n\x06GetAds\x12\x13.oteldemo.AdRequest\x1a\x14.oteldemo.AdResponse\"\x00\x32\xff\x02\n\x12\x46\x65\x61tureFlagService\x12@\n\x07GetFlag\x12\x18.oteldemo.GetFlagRequest\x1a\x19.oteldemo.GetFlagResponse\"\x00\x12I\n\nCreateFlag\x12\x1b.oteldemo.CreateFlagRequest\x1a\x1c.oteldemo.CreateFlagResponse\"\x00\x12I\n\nUpdateFlag\x12\x1b.oteldemo.UpdateFlagRequest\x1a\x1c.oteldemo.UpdateFlagResponse\"\x00\x12\x46\n\tListFlags\x12\x1a.oteldemo.ListFlagsRequest\x1a\x1b.oteldemo.ListFlagsResponse\"\x00\x12I\n\nDeleteFlag\x12\x1b.oteldemo.DeleteFlagRequest\x1a\x1c.oteldemo.DeleteFlagResponse\"\x00\x42\x13Z\x11genproto/oteldemob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021genproto/oteldemo'
  _globals['_CARTITEM']._serialized_start=24
  _globals['_CARTITEM']._serialized_end=72
  _globals['_ADDITEMREQUEST']._serialized_start=74
  _globals['_ADDITEMREQUEST']._serialized_end=141
  _globals['_EMPTYCARTREQUEST']._serialized_start=143
  _globals['_EMPTYCARTREQUEST']._serialized_end=178
  _globals['_GETCARTREQUEST']._serialized_start=180
  _globals['_GETCARTREQUEST']._serialized_end=213
  _globals['_CART']._serialized_start=215
  _globals['_CART']._serialized_end=273
  _globals['_EMPTY']._serialized_start=275
  _globals['_EMPTY']._serialized_end=282
  _globals['_LISTRECOMMENDATIONSREQUEST']._serialized_start=284
  _globals['_LISTRECOMMENDATIONSREQUEST']._serialized_end=350
  _globals['_LISTRECOMMENDATIONSRESPONSE']._serialized_start=352
  _globals['_LISTRECOMMENDATIONSRESPONSE']._serialized_end=402
  _globals['_PRODUCT']._serialized_start=405
  _globals['_PRODUCT']._serialized_end=534
  _globals['_LISTPRODUCTSRESPONSE']._serialized_start=536
  _globals['_LISTPRODUCTSRESPONSE']._serialized_end=595
  _globals['_GETPRODUCTREQUEST']._serialized_start=597
  _globals['_GETPRODUCTREQUEST']._serialized_end=628
  _globals['_SEARCHPRODUCTSREQUEST']._serialized_start=630
  _globals['_SEARCHPRODUCTSREQUEST']._serialized_end=668
  _globals['_SEARCHPRODUCTSRESPONSE']._serialized_start=670
  _globals['_SEARCHPRODUCTSRESPONSE']._serialized_end=730
  _globals['_GETQUOTEREQUEST']._serialized_start=732
  _globals['_GETQUOTEREQUEST']._serialized_end=820
  _globals['_GETQUOTERESPONSE']._serialized_start=822
  _globals['_GETQUOTERESPONSE']._serialized_end=875
  _globals['_SHIPORDERREQUEST']._serialized_start=877
  _globals['_SHIPORDERREQUEST']._serialized_end=966
  _globals['_SHIPORDERRESPONSE']._serialized_start=968
  _globals['_SHIPORDERRESPONSE']._serialized_end=1008
  _globals['_ADDRESS']._serialized_start=1010
  _globals['_ADDRESS']._serialized_end=1107
  _globals['_MONEY']._serialized_start=1109
  _globals['_MONEY']._serialized_end=1169
  _globals['_GETSUPPORTEDCURRENCIESRESPONSE']._serialized_start=1171
  _globals['_GETSUPPORTEDCURRENCIESRESPONSE']._serialized_end=1227
  _globals['_CURRENCYCONVERSIONREQUEST']._serialized_start=1229
  _globals['_CURRENCYCONVERSIONREQUEST']._serialized_end=1304
  _globals['_CREDITCARDINFO']._serialized_start=1307
  _globals['_CREDITCARDINFO']._serialized_end=1451
  _globals['_CHARGEREQUEST']._serialized_start=1453
  _globals['_CHARGEREQUEST']._serialized_end=1548
  _globals['_CHARGERESPONSE']._serialized_start=1550
  _globals['_CHARGERESPONSE']._serialized_end=1590
  _globals['_ORDERITEM']._serialized_start=1592
  _globals['_ORDERITEM']._serialized_end=1668
  _globals['_ORDERRESULT']._serialized_start=1671
  _globals['_ORDERRESULT']._serialized_end=1853
  _globals['_SENDORDERCONFIRMATIONREQUEST']._serialized_start=1855
  _globals['_SENDORDERCONFIRMATIONREQUEST']._serialized_end=1938
  _globals['_PLACEORDERREQUEST']._serialized_start=1941
  _globals['_PLACEORDERREQUEST']._serialized_end=2098
  _globals['_PLACEORDERRESPONSE']._serialized_start=2100
  _globals['_PLACEORDERRESPONSE']._serialized_end=2158
  _globals['_ADREQUEST']._serialized_start=2160
  _globals['_ADREQUEST']._serialized_end=2193
  _globals['_ADRESPONSE']._serialized_start=2195
  _globals['_ADRESPONSE']._serialized_end=2234
  _globals['_AD']._serialized_start=2236
  _globals['_AD']._serialized_end=2276
  _globals['_FLAG']._serialized_start=2278
  _globals['_FLAG']._serialized_end=2336
  _globals['_GETFLAGREQUEST']._serialized_start=2338
  _globals['_GETFLAGREQUEST']._serialized_end=2368
  _globals['_GETFLAGRESPONSE']._serialized_start=2370
  _globals['_GETFLAGRESPONSE']._serialized_end=2417
  _globals['_CREATEFLAGREQUEST']._serialized_start=2419
  _globals['_CREATEFLAGREQUEST']._serialized_end=2490
  _globals['_CREATEFLAGRESPONSE']._serialized_start=2492
  _globals['_CREATEFLAGRESPONSE']._serialized_end=2542
  _globals['_UPDATEFLAGREQUEST']._serialized_start=2544
  _globals['_UPDATEFLAGREQUEST']._serialized_end=2594
  _globals['_UPDATEFLAGRESPONSE']._serialized_start=2596
  _globals['_UPDATEFLAGRESPONSE']._serialized_end=2616
  _globals['_LISTFLAGSREQUEST']._serialized_start=2618
  _globals['_LISTFLAGSREQUEST']._serialized_end=2636
  _globals['_LISTFLAGSRESPONSE']._serialized_start=2638
  _globals['_LISTFLAGSRESPONSE']._serialized_end=2687
  _globals['_DELETEFLAGREQUEST']._serialized_start=2689
  _globals['_DELETEFLAGREQUEST']._serialized_end=2722
  _globals['_DELETEFLAGRESPONSE']._serialized_start=2724
  _globals['_DELETEFLAGRESPONSE']._serialized_end=2744
  _globals['_CARTSERVICE']._serialized_start=2747
  _globals['_CARTSERVICE']._serialized_end=2931
  _globals['_RECOMMENDATIONSERVICE']._serialized_start=2933
  _globals['_RECOMMENDATIONSERVICE']._serialized_end=3058
  _globals['_PRODUCTCATALOGSERVICE']._serialized_start=3061
  _globals['_PRODUCTCATALOGSERVICE']._serialized_end=3302
  _globals['_SHIPPINGSERVICE']._serialized_start=3305
  _globals['_SHIPPINGSERVICE']._serialized_end=3463
  _globals['_CURRENCYSERVICE']._serialized_start=3466
  _globals['_CURRENCYSERVICE']._serialized_end=3637
  _globals['_PAYMENTSERVICE']._serialized_start=3639
  _globals['_PAYMENTSERVICE']._serialized_end=3718
  _globals['_EMAILSERVICE']._serialized_start=3720
  _globals['_EMAILSERVICE']._serialized_end=3818
  _globals['_CHECKOUTSERVICE']._serialized_start=3820
  _globals['_CHECKOUTSERVICE']._serialized_end=3912
  _globals['_ADSERVICE']._serialized_start=3914
  _globals['_ADSERVICE']._serialized_end=3980
  _globals['_FEATUREFLAGSERVICE']._serialized_start=3983
  _globals['_FEATUREFLAGSERVICE']._serialized_end=4366
# @@protoc_insertion_point(module_scope)