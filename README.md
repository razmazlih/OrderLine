
# OrderLine API

## Introduction
The `OrderLine` API is a FastAPI-based project for managing orders, order items, and order statuses in a food ordering system. It supports real-time updates using WebSockets for order status changes.

---

## Features
1. **Order Management**:
   - Create, read, update, and delete orders.
   - Retrieve paginated lists of orders.

2. **Order Item Management**:
   - Add, update, or remove items in an order.
   - Retrieve all items for a specific order.

3. **Order Status Management**:
   - Track and update the status of orders.
   - Notify clients of real-time updates using WebSocket.

4. **Docker Integration**:
   - Fully containerized using Docker and Docker Compose for easy setup and scalability.

5. **PostgreSQL Database**:
   - The system uses PostgreSQL for persistent data storage.

---

## Installation

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Optional: Python 3.12 if running locally without Docker.

### Setup with Docker
1. Clone the repository:
   ```bash
   git clone https://github.com/razmazlih/OrderLine.git
   cd OrderLine
   ```

2. Create a `.env` file in the project root:
   ```env
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=your_database_name
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

3. Start the services with Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Access the API at `http://localhost:8003/docs`.

---

## Local Development (Without Docker)
1. Clone the repository and navigate to the project directory:
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

4. Set environment variables:
   ```bash
   export POSTGRES_USER=your_username
   export POSTGRES_PASSWORD=your_password
   export POSTGRES_DB=your_database_name
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5432
   ```

5. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. Access the API at `http://localhost:8000/docs`.

---

## File Structure
- **`main.py`**: Entry point for the FastAPI application.
- **`database.py`**: Database connection and session setup using SQLAlchemy.
- **`models.py`**: ORM models for orders, items, and statuses.
- **`routers/`**: API route definitions.
- **`docker-compose.yml`**: Docker Compose configuration for the app and PostgreSQL.
- **`Dockerfile`**: Docker image setup for the FastAPI backend.

---

## API Endpoints
### Orders
- `POST /orders/`: Create a new order.
- `GET /orders/`: Retrieve a paginated list of orders.
- `GET /orders/{order_id}/`: Retrieve details of a specific order.
- `PUT /orders/{order_id}/`: Update an order.
- `DELETE /orders/{order_id}/`: Delete an order.

### Order Items
- `POST /order-item/`: Add an item to an order.
- `GET /order-item/{order_id}/`: Retrieve all items for an order.
- `PUT /order-item/{item_id}/`: Update an order item.
- `DELETE /order-item/{item_id}/`: Delete an order item.

### Order Status
- `POST /order-status/`: Add a new status to an order.
- `GET /order-status/{order_id}/`: Retrieve statuses for an order.

### WebSocket
- `GET /ws/order-status/{order_id}`: Real-time order status updates.

---

## Usage Example

### WebSocket Client Example
Connect to the WebSocket for real-time order status updates:
```javascript
const socket = new WebSocket("ws://localhost:8003/ws/order-status/1");

socket.onmessage = (event) => {
    console.log("Order status updated:", event.data);
};
```

### Adding a New Status
Send a `POST` request to `/order-status/`:
```json
{
    "order_id": 1,
    "status": "Preparing"
}
```

The WebSocket clients will receive a notification: `Order 1 status updated to Preparing`.

---

## Docker Configuration
- **`docker-compose.yml`**:
  - Includes two services: `db` (PostgreSQL) and `backend` (FastAPI app).
  - Configures a health check for the database.
  - Defines a shared network for communication between containers.

- **`Dockerfile`**:
  - Uses Python 3.12 as the base image.
  - Installs dependencies from `requirements.txt`.
  - Runs the FastAPI app on port `8000`.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
