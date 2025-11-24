# Multi-stage build for Next.js client
FROM node:18 AS client-build

WORKDIR /app

# Install dependencies and build the Next.js app
COPY client/package.json client/package-lock.json ./
RUN npm install
COPY client/ ./
RUN npm run build

# Base image for serving the Next.js app
FROM node:18 AS client
WORKDIR /app
COPY --from=client-build /app/ .

# Expose the port and start the Next.js app
EXPOSE 3000
CMD ["npm", "start"]

# Python backend
FROM python:3.10 AS backend

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY mcp/ ./mcp
COPY toolbox/ ./toolbox
COPY utils/ ./utils

# Expose the port and start the backend server
EXPOSE 8000
CMD ["python", "-m", "mcp.server"]