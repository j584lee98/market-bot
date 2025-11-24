# Market Bot

## Overview
Market Bot is a web-based application that provides real-time stock market insights and tools. It features a Next.js client for the frontend and a Python backend for handling data processing and API interactions.

## Requirements
- Node.js (v18 or higher)
- Python (v3.10 or higher)
- Docker (optional, for containerized deployment)

## Installation

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/j584lee98/market-bot.git
   cd market-bot
   ```

2. Install dependencies for the client:
   ```bash
   cd client
   npm install
   ```

3. Install dependencies for the backend:
   ```bash
   cd ..
   pip install -r requirements.txt
   ```

### Using Docker
1. Build and start the services:
   ```bash
   docker-compose up --build
   ```

2. Access the client at `http://localhost:3000` and the backend at `http://localhost:8000`.

## Deployment

### Local Deployment
1. Start the backend server:
   ```bash
   python -m mcp.server
   ```

2. Start the Next.js client:
   ```bash
   cd client
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:3000`.

### Docker Deployment
1. Ensure Docker is installed and running.
2. Use the following command to start the services:
   ```bash
   docker-compose up -d
   ```

### Vercel Deployment
1. Ensure you have a [Vercel](https://vercel.com/) account and the Vercel CLI installed:
   ```bash
   npm install -g vercel
   ```

2. Deploy the Next.js client:
   ```bash
   cd client
   vercel
   ```

3. Follow the prompts to configure your project. Once deployed, you will receive a live URL for your application.

4. For backend deployment, consider using a cloud provider or hosting service that supports Python applications.

## Features
- Real-time stock market data visualization.
- Interactive chat interface for market insights.
- Markdown support for rich text responses.