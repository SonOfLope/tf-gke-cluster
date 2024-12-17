import grpc
from flask import Flask, jsonify

import logging
import demo_pb2
import demo_pb2_grpc

app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

CART_SERVICE_ADDRESS = "otel-shop-demo-cartservice.default.svc.cluster.local:8080"

@app.route("/<user_id>")
def get_cart(user_id):
    logger.info(f"Getting cart for user {user_id}")
    with grpc.insecure_channel(CART_SERVICE_ADDRESS) as channel:
        stub = demo_pb2_grpc.CartServiceStub(channel)
        request = demo_pb2.GetCartRequest(user_id=user_id)
        
        response = stub.GetCart(request)
        
        cart_dict = {
            "user_id": response.user_id,
            "items": [
                {"product_id": item.product_id, "quantity": item.quantity}
                for item in response.items
            ]
        }
        
        return jsonify(cart_dict), 200

@app.route("/")
def hello():
    logger.info("root endpoint was reached")
    return "Python demo app", 200 

@app.route('/error')
def error():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("An error occurred: Division by zero")
    return jsonify(error="An error occurred"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
