import grpc
from flask import Flask, jsonify

import demo_pb2
import demo_pb2_grpc

app = Flask(__name__)

CART_SERVICE_ADDRESS = "otel-shop-demo-cartservice.default.svc.cluster.local:8080"

@app.route("/<user_id>")
def get_cart(user_id):
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
    return "Python app", 200 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
