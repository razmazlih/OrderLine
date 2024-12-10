
# OrderLine API

---

## Introduction
The `OrderLine` API is a FastAPI-based project designed to manage orders, order items, and order statuses for a food ordering system. It supports real-time updates via WebSockets for order status changes.

---

## Features

1. **Order Management**:
   - Create, read, update, and delete orders.
   - Retrieve a paginated list of orders.

2. **Order Item Management**:
   - Add items to orders.
   - Update or delete items in an order.
   - Retrieve all items in a specific order.

3. **Order Status Management**:
   - Track status updates for orders.
   - Notify clients about real-time status changes via WebSocket.

4. **Real-Time Communication**:
   - Use WebSocket connections to broadcast order status changes to connected clients.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/razmazlih/OrderLine.git
   cd OrderLine
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   fastapi dev main.py
   ```

---

## API Endpoints

### Orders
- `POST /orders/`: Create a new order.
- `GET /orders/`: Retrieve a paginated list of orders.
- `GET /orders/{order_id}/`: Retrieve details of a specific order.
- `PUT /orders/{order_id}/`: Update an existing order.
- `DELETE /orders/{order_id}/`: Delete an order.

### Order Items
- `POST /order-item/`: Add an item to an order.
- `GET /order-item/{order_id}/`: Retrieve all items in a specific order.
- `PUT /order-item/{order_item_id}/`: Update an order item.
- `DELETE /order-item/{order_item_id}/`: Delete an order item.

### Order Status
- `POST /order-status/`: Add a new status to an order and notify clients.
- `GET /order-status/{order_id}/`: Retrieve all statuses for a specific order.

### WebSocket
- `GET /ws/order-status/{order_id}`: Connect to receive real-time updates for order statuses.

---

## Usage Example

### Sending Order Status Updates
1. Establish a WebSocket connection:
   ```javascript
   const socket = new WebSocket("ws://localhost:8000/ws/order-status/1");

   socket.onmessage = (event) => {
       console.log("Order status update:", event.data);
   };
   ```

2. Add a new status to an order via `POST /order-status/`:
   ```json
   {
       "order_id": 1,
       "status": "Preparing"
   }
   ```

   All connected WebSocket clients will receive a message: `Order 1 status updated to Preparing`.

---

## Models

### Order
- `id` (int): Primary key.
- `user_id` (int): Reference to the user placing the order.
- `restaurant_id` (int): Reference to the restaurant.
- `ordered_at` (datetime): Timestamp of order creation.

### Order Item
- `id` (int): Primary key.
- `order_id` (int): Foreign key to the order.
- `name` (str): Item name.
- `quantity` (int): Quantity of the item.
- `price` (float): Price per unit.

### Order Status
- `id` (int): Primary key.
- `order_id` (int): Foreign key to the order.
- `status` (str): Status description (e.g., "Preparing", "Delivered").
- `updated_at` (datetime): Timestamp of status update.

---

## Contribution

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
